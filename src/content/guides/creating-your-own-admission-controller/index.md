+++
title = "Creating your own admission controller"
description = "Tutorial on how to deploy Istio on a Giant Swarm Kubernetes cluster."
date = "2018-10-26"
type = "page"
weight = 50
tags = ["tutorial"]
+++

# Creating your own admission controller

The Kubernetes API is an amazing territory. Thanks to being built around the REST model, it gives us the possibility to manage all our workloads using HTTP requests. Tools like `kubectl` or `Kubernetes dashboard` take advantage of this, helping to manage the different resources. But Kubernetes API is far more. Let's take a deeper look at how it is composed:

![](./src/static/img/api_components.png)

The picture highlights the different components living inside the API component. The request starts the API journey interfacing with the authentication controller. Once the request is authenticated, the authorization module dictates if the request issuer may perform the operation. After the request is properly authorized, the admission magic comes into play. 

There are two types of admission controllers in Kubernetes. They work slightly differently. The first one, it is the **validating admission controller**, which proxies the requests to the subscribed webhooks. The Kubernetes API registers the webhooks based on the resource type and the request method. Every webhook runs some logic to validate the incoming resource and it replies to the API with a verdict. In case the validation webhook rejects the request, Kubernetes API returns a failed HTTP response to the user. Otherwise, it continues to the next admission.

In the second, there is a **mutation admission controller** which modifies the resource submitted by the user, so you can make some defaults or force some schema. The cluster admins can attach mutation webhooks to the API to be run in the same way as validation. Indeed mutation logic runs one step before the validation.

__Note:__ I would like to mention that Kubernetes API allows you to register custom resource objects too, called `Custom Resource Definition`. In addition, you can create an API extension server which listens to a new REST path. But in this guide, we focus exclusively on the admission functionality.

## Goal

Our goal here is to create a simple validation controller which will empower us to influence the pod creation. Although there are many more possibilities and the logic can be as complex as you need. The goal is to create a basic version which makes a simple validation. You can find more real examples in the links at the bottom.

Our example controller will be called `grumpy` and will reject all new pods with a name different than `smooth-app`. I recognize it may be tempting to deploy this controller in a real cluster ;).

## How API proxies requests

The Kubernetes API server needs to know when to send the incoming request to our admission controller. The Kubernetes nature advocates the use of a declarative state always and this is no exception. Below we define a `ValidationWebhookConfiguration` which gives the needed information to the API:

```yaml
apiVersion: admissionregistration.k8s.io/v1beta1
kind: ValidatingWebhookConfiguration
metadata:
  name: grumpy
webhooks:
  - name: grumpy.giantswarm.io
    clientConfig:
      service:
        name: grumpy
        namespace: default
        path: "/validate"
      caBundle: "${CA_BUNDLE}"
    rules:
      - operations: ["CREATE"]
        apiGroups: [""]
        apiVersions: ["v1"]
        resources: ["pods"]
```

The configuration definition is pretty obvious. You can see there are two main parts to be considered. In the first one, `clientConfig`, we define where our service can be found (can be an external URL too), and the `path` which our validation server will listen. Also, you notice there is a `CA` to be defined. Since security is always important, adding the cert authority will tell Kubernetes API to use HTTPS and validate our server using the passed asset. In the next section, you will find an explanation on how to generate all the certs needed.

The second part specifies which rules will follow the API to decide if a request should be forwarded for validation to `grumpy` or not. Here it is configured that only requests with method equal to `CREATE` and resource type `pod` will be forwarded. 

## Generate the certificates and the CA

Since the scope of this guide is not teaching how to build a PKI bundle, we have created a script, `gen_cert.sh`, in the grumpy repository which generates a CA bundle and a key pair for our grumpy server. Also we need to provide the CA in the webhook displayed above, in order to allow the Kubernetes API to create a secure connection against our shiny controller.

__Note:__ Inside the aforementioned script there are comments explaining the commands executed in case you are interested in what was done under the hood.

For the purpose of this tutorial, our validation webhook configuration must contain an encoded certificate authority. Besides creating the certificates and the CA, the script later injects it into the manifest used to deploy our server.

```
$ cat manifest.yaml | grep caBundle
```

In the next step, we need to create a secret to place the certificates. After we apply the manifest, the pod will be able to mount the secret files into a directory.

```
$ kubectl create secret generic grumpy \
        --from-file=key.pem=certs/grumpy-key.pem \
        --from-file=cert.pem=certs/grumpy-crt.pem
```

## Deploy validation controller

In order to deploy the server, we will use a deployment with a single replica which mounts the certs generated to expose a secure REST endpoint where the pod request will be submitted. At the same time, we will expose the controller through the service to configure the DNS as we have defined in the webhook resource.

```yaml
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: grumpy
  namespace: default
spec:
  replicas: 1
  template:
    spec:
      containers:
        - name: webhook
          image: giantswarm/grumpy:1.0.0
          ...
          volumeMounts:
            - name: webhook-certs
              mountPath: /etc/certs
        ...
      volumes:
        - name: webhook-certs
          secret:
            secretName: grumpy
--- 
apiVersion: v1
kind: Service
metadata:
  name: grumpy
  namespace: default
spec:
  ports:
  - name: webhook
    port: 443
    targetPort: 8080
    ...
```

Applying the manifest should be enough. It also contains the webhook commented before.

```bash
$ kubectl apply -f manifest.yaml
```

Now the server should be running and ready to validate the creation of new pods.

## Verify validation controller works

Let's try to create a simple pod with a non-matching name.

```$bash
$ kubectl apply -f pod_wrong.yaml
Error from server: error when creating "pod_wrong.yaml": admission webhook "grumpy.giantswarm.org" denied the request: Keep calm and not add more crap in the cluster!
```

The admission control has intercepted the request, it checked the name and it did not match with the expected value, so it rejected it. 

To confirm it works, let's try now with a correct name.

```bash
$ kubectl apply -f smooth-app.yaml
pod/smooth-app created
$ kubectl get pod   
smooth-app                    0/1     Completed   0          6s
```

## Explain validation logic

In this example, we have chosen go-lang to create the admission controller just because it is the Kubernetes de facto language, but you could use whatever language you prefer and it should work in the same way.

Let's start creating an HTTP server with the certs mounted from the secret. The server will listen to the path `validate` as we defined in the webhook.

__Note:__ The code examples have been stripped out to make it easier to understand. For a more detailed look, browse the [repository](github.com/gianstwarm/grumpy).

```go

  // Read the certs from the convined path and convert it to a X509 keypair
  flag.StringVar(&tlscert, "tlsCertFile", "/etc/certs/cert.pem", "x509 Certificate for HTTPS.")
	flag.StringVar(&tlskey, "tlsKeyFile", "/etc/certs/key.pem", "x509 private key to --tlsCertFile.")
  certs, _ := tls.LoadX509KeyPair(tlscert, tlskey)

  // Create a secure http server
	server := &http.Server{
		Addr:      ":8080",
		TLSConfig: &tls.Config{Certificates: []tls.Certificate{certs}},
	}

	// Create a handler listening to the 'validate' path and start the server
	gs := GrumpyServerHandler{}
	mux.HandleFunc("/validate", gs.serve)
	server.ListenAndServeTLS("", "")

```

Inside the grumpy package, we define a `serve` function which reads the request body, then it converts the data to a `Pod` data type and finally checks if the resource name is valid.

```go
	// Convert raw data in a Pod data type
  raw := arRequest.Request.Object.Raw
	pod := v1.Pod{}
	json.Unmarshal(raw, &pod)

  // Actual validation logic
	if pod.Name != "smooth-app" {
		return
	}
```

In case the request name is not the expected one (`smooth-app`), our handler creates a response notifying of the rejection. Otherwise, it returns and Kubernetes API server will follow the processing the request.

```go
  // Create a response to return to the Kubernetes API
  ar := v1beta1.AdmissionReview{
		Response: &v1beta1.AdmissionResponse{
			Allowed: false,
			Result: &metav1.Status{
				Message: "Keep calm and not add more crap in the cluster!",
			},
		},
	}
	resp, err := json.Marshal(ar)
```

# Conclusion

As you can see from this tutorial, it is quite easy to implement a simple admission controller. Obviously, there is plenty of possibilities to make your cluster secure and harden it (accept known registries, forbid latest tags, ...). 

At the same time, it holds great power, since it can influence the key components running in the cluster. As an example, you could block the CNI plugin from running in case you commit an error which may lead to the entire cluster being borked. So be careful and try to scope the admission logic to a namespace or a minor set of actions.

Also, it is good to mention there are already some projects which leverage this pattern to enable high order functionality. As an example [gatekeeper](https://github.com/replicatedhq/gatekeeper/) uses admission webhooks to implement a policy engine ([OPA](https://www.openpolicyagent.org/)) to enforce policies over Cloud Native environments.

## Further reading

- [Official documentation](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
- [Go framework to create mutation/validation controllers](https://github.com/slok/kubewebhook/)
- [Mutation controller Tutorial](https://github.com/morvencao/kube-mutating-webhook-tutorial/)
