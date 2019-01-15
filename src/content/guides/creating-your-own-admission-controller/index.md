+++
title = "Creating your own admission controller"
description = "Tutorial on how to deploy Istio on a Giant Swarm Kubernetes cluster."
date = "2018-10-26"
type = "page"
weight = 50
tags = ["tutorial"]
+++

# Creating your own admission controller

The Kubernetes API is an amazing territory. Thanks to being built around the REST model, give us the possibility to manage all our workloads using HTTP requests. Tools like `kubectl` or `Kubernetes dashboard` take advantage of this helping to manage the different resources. But Kubernetes API is far more. Let's take a deeper look at how it is composed:

![](https://github.com/giantswarm/giantswarm/raw/master//src/static/img/api_components.png)

The picture highlights the different components living inside the API component. The request starts the API journey facing with the authentication controller. Once the request is authenticated, the authorization module dictates if the request issuer can perform or not the operation. After the request is properly authorized, the admission magic comes to place. 

There are two types of admission controllers in Kubernetes. They work slightly different. First one, it is the validating admission controller, which proxy the requests to the subscribed webhooks. The Kubernetes API register the webhooks based on the resource type and the request method. Every webhook runs some logic to validate the incoming resource and it replies to the API with a verdict. In case the validation webhook rejects the request, Kubernetes API returns a failed HTTP response to the user. Otherwise, it continues to the next admission.

Secondly, there is a mutation admission controller which modifies the resource submitted by the user, so you can make some defaults or force some schema. The cluster admins can attach mutation webhooks to the API to be run same way validation. Indeed mutation logic runs one step before than validation.

I would like to mention that Kubernetes API allows you to register custom resource objects too, called `Custom Resource Definition`. In adition to more, you can create an API extension server which listen to a new REST path. But in this guide, we focus exclusively on the admission functionality.

## Goal

Our goal here is to create a simple validation controller which will empower us to influence in the pod creation. Although there many more possibilities and the logic could be as complex as you want, the goal is just to create a basic version which makes a simple validation. The reader can always find more real examples in the links on the bottom.

Our example controller will be called `grumpy` and will reject all new pods with a name different than `smooth-app`. I recognize it is tempting sometimes deploy this controller in a real cluster ;).

## How API proxies requests

The Kubernetes API server needs to know when and where sending the incoming request to our admission controller. The Kubernetes nature advocates to use declarative state always and here it is not an exception. Below we define a `ValidationWebhookConfiguration` which gives the needed information to the API:

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

The configuration definition is pretty obvious. It can be observed there are two main parts to be considered. In the first one, `clientConfig`, we define where our service can be found (can be an external URL too), and the `path` which our validation server will listen. Also, you notice there is a `CA` to be defined. Since security is always important, adding the cert authority will tell Kubernetes API to use HTTPS and validate our server using the passed asset. In the next section, it will be explained how to generate all the certs needed.

The second part specifies which rules will follow the API to decide if a request should be forward for validation to `grumpy` or not. Here it is configured that only requests with method equal to `CREATE` and resource type `pod` will be forwarded. 

## Generate the certificates and the CA

Since the scope of this guide is not teaching how you can build a PKI bundle, we have created a script, `gen_cert.sh`, in the grumpy repository which generates a CA bundle and a keypair for our grumpy server. Also we need to provide the CA in the webhook displayed before, in order to allow the Kubernetes API to create a secure connection against our shiny controller.

__Node:__ Inside the aforementioned script there are comments explaining the commands executed in case you have interest what has be done under the hood.

Hence at this moment our validation webhook configuration must contain a encoded certify authority. The script besides create the certificates and the CA, inject the later in the manifest used to deploy our server.

```
$ cat manifest.yaml | grep caBundle
```

At the same time we need to create a secret to place the certificates. After we apply the manifest, the pod will be able to mount the secret files into a directory.

```
$ kubectl create secret generic grumpy \
        --from-file=key.pem=certs/grumpy-key.pem \
        --from-file=cert.pem=certs/grumpy-crt.pem
```

## Deploy validation controller

In order to deploy the server we will use a deployment with a single replica which mount the certs generated to expose a secure REST endpoint where the pod request will be submited. At the same time we expose the controller through a service to configure the DNS as we has defined in the webhook resource.

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

Let's try to create a simple pod with a non matching name.

```$bash
$ kubectl apply -f pod_wrong.yaml
Error from server: error when creating "pod_wrong.yaml": admission webhook "grumpy.giantswarm.org" denied the request: Keep calm and not add more crap in the cluster!
```

The admission control has intercepted the request, it checked the name and it did not matched with the expected value, so it rejected. 

To confirm it works, let's try now with a correct name.

```bash
$ kubectl apply -f pod_wrong.yaml
pod/smooth-app created
$ kubectl get pod   
smooth-app                    0/1     Completed   0          6s
```

## Explain validation logic

In this example we have chosen go-lang to create the admission controller just because is the Kubernetes de facto language, but you could use whatever language you prefer and it should work the same.

Let's start creating a HTTP server with the certs mounted from the secret. The server will listen the path `validate` as we defined in the webhook.

__Note:__ The code examples has been striped them out to make easier the understanding. For further look browse the [repository](github.com/gianstwarm/grumpy).

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

Inside the grumpy package we define a `serve` function which reads the request body, then it converts the data to a `Pod` data type and finally check if the resource name is valid.

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

In case the request name is not the expected one (`smooth-app`), our handler creates a response notifying the rejection. Otherwise it returns and Kubernetes API server will follow processing the request.

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

As you could observed here, it is quite easy to implement a simple admission controller. Obviously there are plenty of possiblities to make your cluster secure and harden (accept known registries, forbid latest tags, ...). 

At the same time, it encloses a great power, since it could influence in the key components running in the cluster. As an example, you could block the CNI plugin to run in case you commit an error which will lead to borked the entire cluster. So be careful and try to scope the admission logic to a namespace or a minor set of actions.

Also it is good to mention there are already some projects which leverages on that pattern to enable high order functionality. As example [gatekeeper](https://github.com/replicatedhq/gatekeeper/) uses admission webhooks to implement a policy engine ([OPA](https://www.openpolicyagent.org/)) to enforce policies over Cloud Native environments.

## Further reading

- [Official documentation](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
- [Go framework to create mutation/validation controllers](https://github.com/slok/kubewebhook/)
- [Mutation controller Tutorial](https://github.com/morvencao/kube-mutating-webhook-tutorial/)
