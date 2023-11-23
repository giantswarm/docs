---
linkTitle: Load balancer services
title: Services of type LoadBalancer
description: Learn how to expose services directly on cloud providers through services of type LoadBalancer.
weight: 30
menu:
  main:
    parent: advanced-ingress
user_questions:
  - How can I expose Services to the internet?
  - How do I configure an Ingress Controller behind an ELB for traffic between services within the VPC?
  - How do I configure an Ingress Controller behind an ELB that terminates SSL?
  - How do I configure an internal Load Balancer on AWS?
  - How do I configure an internal Load Balancer on Azure?
  - How do I configure an internal Load Balancer on GCP?
last_review_date: 2023-11-23
aliases:
  - /guides/services-of-type-loadbalancer-and-multiple-ingress-controllers/
  - /advanced/ingress/service-type-loadbalancer-multi-ic/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

Next to using the default Ingress NGINX Controller, on cloud providers (currently AWS, Azure and GCP), you can expose services directly outside your cluster by using Services of type `LoadBalancer`.

You can use this to [expose single Services](#service-of-type-lb) to the internet. It is also possible, to [install additional Ingress NGINX Controllers]({{< relref "/content/advanced/connectivity/ingress/multi-nginx-ic/index.md" >}}) to expose a subset of your Services with a different Ingress Controller configuration.

**Note** that this functionality cannot be used on premises (KVM).

## Exposing a single Service {#service-of-type-lb}

Setting the `type` field of your service to `LoadBalancer` will result in your Service being exposed by a dynamically provisioned load balancer.

You can do this with any Service within your cluster, including Services that expose several ports.

The actual creation of the load balancer happens asynchronously, and information about the provisioned balancer will be published in the Service’s `status.loadBalancer` field, like following:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: helloworld
  name: helloworld
spec:
  ports:
  - port: 8080
    targetPort: http
  selector:
    app: helloworld
  type: LoadBalancer
status:
  loadBalancer:
    ingress:
    - hostname: a54cae28bd42b11e7b2c7020a3f15370-27798109.eu-central-1.elb.amazonaws.com
```

The above YAML would expose port 8080 of our helloworld Pods on the http port of the provisioned ELB.

### Exposing on a non-HTTP port and protocol

You can change the port of the load balancer and protocol of the load balancer by changing the `targetPort` field and adding a `ports.protocol` field. This way you can expose TCP services directly without having to customize the Ingress Controller.

Following example would set the ELB to TCP and port `8888`:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: helloworld
  name: helloworld
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 8888
  selector:
    app: helloworld
  type: LoadBalancer
status:
  loadBalancer:
    ingress:
    - hostname: a54cae28bd42b11e7b2c7020a3f15370-27798109.eu-central-1.elb.amazonaws.com
```

### Customizing the external load balancer

This section will focus on the custom options you can set on AWS Load Balancers via a Service of type `LoadBalancer`, but when available will also explain the settings for Azure Load Balancers. You can configure these options by adding annotations to the service.

#### Internal load balancers

If you want the AWS ELB to be available only within your VPC (can be extended to other VPC by VPC peering) use the following annotation:

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-internal: "true"
```

On Azure you can configure internal Load Balancers like this.

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/azure-load-balancer-internal: "true"
```

On GCP, an internal Load Balancer can be requested using the following annotation:

```yaml
metadata:
  name: my-service
  annotations:
    networking.gke.io/load-balancer-type: "Internal"
```

#### SSL termination on AWS

There are three annotations you can set to configure SSL termination.

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012
```

The first one depicts the ARN of the certificate you want to use. You can either upload the certificate to IAM or create it within AWS Certificate Manager.

```yaml
service.beta.kubernetes.io/aws-load-balancer-backend-protocol: (https|http|ssl|tcp)
```

The second annotation specifies which protocol a pod speaks. For HTTPS and SSL, the ELB will expect the pod to authenticate itself over the encrypted connection.

Please note, setting `service.beta.kubernetes.io/aws-load-balancer-backend-protocol: http` requires changing `controller.service.targetPorts.https` to `http` in your Ingress NGINX Controller configuration.

HTTP and HTTPS will select layer 7 proxying: the ELB will terminate the connection with the user, parse headers and inject the `X-Forwarded-For` header with the user’s IP address (pods will only see the IP address of the ELB at the other end of its connection) when forwarding requests.

TCP and SSL will select layer 4 proxying: the ELB will forward traffic without modifying the headers.
In a mixed-use environment where some ports are secured and others are left unencrypted, the following annotations may be used:

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-backend-protocol: http
    service.beta.kubernetes.io/aws-load-balancer-ssl-ports: "443,8443"
```

In the above example, if the service contained three ports, `80`, `443`, and `8443`, then `443` and `8443` would use the SSL certificate, but `80` would just be proxied HTTP.

#### Access logs on AWS

Writing access logs to an S3 bucket is a standard feature of ELBs. For `LoadBalancer` Services this can also be configured using following annotations.

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-access-log-enabled: true
    # The interval for publishing the access logs (can be 5 or 60 minutes).
    service.beta.kubernetes.io/aws-load-balancer-access-log-emit-interval: "60"
    service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-name: my-logs-bucket
    service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-prefix: logs/prod
```

#### Connection draining on AWS

You can set classic ELBs to drain connections and configure a timeout (in seconds) for the draining like following.

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-connection-draining-enabled: "true"
    service.beta.kubernetes.io/aws-load-balancer-connection-draining-timeout: "60"
```

#### Other AWS ELB configuration options

There are more annotations to manage Classic ELBs that are described below.

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: "60"
    # The time, in seconds, that the connection is allowed to be idle (no data has
    # been sent over connection) before it is closed by the load balancer.
    service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled: "true"
    # Specifies whether cross-zone load balancing is enabled for the load balancer.
    service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags: "environment=prod,owner=devops"
    # A comma-separated list of key-value pairs which will be recorded as
    # additional tags in the ELB.
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-healthy-threshold: ""
    # The number of successive successful health checks required for a backend to
    # be considered healthy for traffic. Defaults to 2, must be between 2 and 10.
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-unhealthy-threshold: "3"
    # The number of unsuccessful health checks required for a backend to be
    # considered unhealthy for traffic. Defaults to 6, must be between 2 and 10.
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-interval: "20"
    # The approximate interval, in seconds, between health checks of an
    # individual instance. Defaults to 10, must be between 5 and 300.
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-timeout: "5"
    # The amount of time, in seconds, during which no response means a failed
    # health check. This value must be less than the service.beta.kubernetesaws-load-balancer-healthcheck-interval
    # value. Defaults to 5, must be between 2 and 60.
    service.beta.kubernetes.io/aws-load-balancer-extra-security-groups: "sg-53fae93f,sg-42efd82e"
    # A list of additional security groups to be added to the ELB.
```

#### AWS Network Load Balancers

AWS is in the process of replacing ELBs with NLBs (Network Load Balancers) and ALBs (Application Load Balancers). NLBs have a number of benefits over "classic" ELBs including scaling to many more requests.

To be able to fully controll all NLB features, we're strongly recommend installing [AWS Load Balancer Controller](https://github.com/giantswarm/aws-load-balancer-controller-app) as the Kubernetes in-tree AWS Load Balancer implementation only supports [annotations for classic ELBs](https://github.com/kubernetes/kubernetes/blob/v1.26.0/staging/src/k8s.io/legacy-cloud-providers/aws/aws.go#L105-L246).

The *AWS Load Balancer Controller* reconciles `Services` that have the `spec.loadBalancerClass` field defined:

```yaml
spec:
  loadBalancerClass: service.k8s.aws/nlb
```

Network load balancers use [Subnet Discovery](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.4/deploy/subnet_discovery/) to attach to a suitable subnet.

With the following [annotation](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.4/guide/service/annotations/#subnets) the subnet can be specified either by nameTag or subnetID:

```yaml
metadata:
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-subnets: subnet-xxxx, mySubnet
```

Multiple subnets can be specified but each has to be in its own availability zone.

#### Changing AWS NLBs configuration

Some parameters on AWS Load Balancers (LBs) cannot be updated gracefully. When these options are changed by updating the corresponding `Service` object in the Kubernetes cluster, the AWS Load Balancer controller has to re-create either the Target Group or the entire Load Balancer. The first case implies a disruption of traffic during the initialization process of the targets. In the latter scenario, a new LB means a new domain, which requires updating the DNS records or any external load balancer configurations.

To avoid downtime, we can create an additional Kubernetes `Service` of type `LoadBalancer`, with the required configuration. This will generate a new, temporary LB on AWS. Traffic is then rerouted to this temporary LB by switching the DNS entry. Once all sessions on the old LB have closed, the original `Service` can be replaced. The DNS entry is then switched back. Once the temporary AWS LB is drained, the corresponding `Service` can be deleted.

#### Process for updating parameters in LoadBalancer Services

1. **Identify the LoadBalancer Service:** Begin by identifying the Kubernetes Service of type LoadBalancer that requires parameter changes.

2. **Prepare a temporary replacement:** Clone the existing Service or create a new temporary Service with the required new configuration. The goal is to create a new LoadBalancer (LB) with its own DNS on the provider's infrastructure. The Ingress Controller (e.g., nginx-ingress-controller) is agnostic to the source of its requests, ensuring that this process does not disrupt ongoing operations.

3. **Redirect traffic to the temporary LoadBalancer service:** Once the temporary Service is set up and the new LoadBalancer can handle traffic, switch the DNS entry for the relevant domain to the new LoadBalancer. This seamlessly directs traffic originally intended for the old LoadBalancer to the new temporary one.

4. **Update the original Service:** Apply the configuration changes to the original Service in the Kubernetes cluster.

5. **Await propagation:** Allow time for this change to propagate through the provider's API.

6. **Switch back the DNS:** Now, revert the DNS entry back to the original LoadBalancer. This completes the process, ensuring that traffic is handled as expected and the immutable parameters have been successfully updated.

7. **Clean up:** Once the temporary LoadBalancer is drained and no traffic passes through it, remove the temporary Service.

Always ensure to closely monitor the system throughout this entire process to minimize any unforeseen disruptions. Additionally, remember to perform these tasks during a maintenance window or a period of low traffic to minimize the impact on end users.

#### Pitfalls and known limitations of AWS Network Load Balancers

There are several pitfalls and known limitations of AWS Network Load Balancers which can take a long time to troubleshoot.

##### Martian Packets when using internal AWS Network Load Balancers

When creating a service of type `LoadBalancer`, Kubernetes normally allocates node ports for each of the exposed ports. The cloud provider's load balancer then uses all your nodes in conjunction with those node ports in its target group to forward traffic into your cluster.

In this so called target type `instance` the AWS Network Load Balancer by default preserves the client IP. Together with `externalTrafficPolicy: Local` your service will be able to see the untouched source IP address of your client. This is - theoretically - possible, because the traffic back to your client passes the AWS network and the AWS Network Load Balancer is probably a part of this, so can keep track of responses and handle them.

This works perfectly fine for public client IP addresses, but gets a bit difficult especially for traffic egressing from nodes of the same cluster to internally addressed AWS Network Load Balancers:

Imagine a pod requesting your AWS Network Load Balancer. The packet hits the load balancer using the node's IP it is running on. This source IP is not getting changed. If the target pod of the service called is running on the same node, the traffic is passing the load balancer and getting sent back to the same node. This node then only sees traffic coming from "somewhere else" with its own IP address. Suspicious, isn't it? Indeed! And because of this the traffic is getting dropped. In the end the whole connection (if TCP) won't be established and simply times out on the client side (both TCP & UDP).

This whole circumstance is called "Martian Packets". If you are relying on accessing an internal AWS Network Load Balancer from inside the same cluster, you sadly need to disable the client IP preservation of your AWS Network Load Balancer by adding the following annotation:

```yaml
metadata:
  name: my-service
  annotations:
    # Disable AWS Network Load Balancer client IP preservation.
    service.beta.kubernetes.io/aws-load-balancer-target-group-attributes: preserve_client_ip.enabled=false
```

See [Target groups for your Network Load Balancers: Client IP preservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#client-ip-preservation) for more information about this whole feature.

##### Health Checks failing when using PROXY protocol and `externalTrafficPolicy: Local`

The before mentioned limitation directly leads us the next pitfall: One could think "well, if the integrated client IP preservation is not working, I can still use PROXY protocol". In theory and at least for the Kubernetes integrated Cloud Controller this should work. In theory.

In reality we need to step back and take a look at how health checks are being implemented with `externalTrafficPolicy: Local`: By default and with `externalTrafficPolicy: Cluster` the AWS Network Load Balancer sends its health check requests to the same port it's sending traffic to: The traffic ports defined in the Kubernetes service. From there they are getting answered by the pods backing your service.

Now, when enabling PROXY protocol, AWS assumes your service is able to understand PROXY protocol for both, traffic and health checks. And this is what happens for services using `externalTrafficPolicy: Cluster` with PROXY protocol enabled: AWS is using it for both the traffic and the health check because in the end and if not configured otherwise by using annotations, they end up on the same port.

But things change when using `externalTrafficPolicy: Local`: Local means the traffic hitting a node on the allocated traffic node port stays on the same node. Therefore only nodes running at least one pod of your service are eligible targets for the AWS Network Load Balancer's target group as other nodes fail to respond to its health checks.

Since the health check might get false negative when two pods are running on the same node and one of them is not healthy (anymore), Kubernetes allocates a separate health check node port and configures it in the AWS Network Load Balancer. This health check node port and requests hitting it is handled by `kube-proxy` or its replacement (Cilium in our case). Unfortunately both of them are not able to handle PROXY protocol and therefore all health checks will fail starting the moment you enable PROXY protocol in your AWS Network Load Balancer in conjunction with `externalTrafficPolicy: Local`.

At last this means there is currently no way of preserving the original client IP using internal AWS Network Load Balancers being accessed from inside the same cluster.

##### Security Group configuration on internal AWS Network Load Balancers

Last but not least there is one thing, you should take care of, left. If you are not accessing an internal AWS Network Load Balancer from inside your cluster and therefore can actually use the integrated client IP preservation, you might still want to access this load balancer from other internal sources, which is totally fine and working.

But since their source IP addresses are not getting changed, they are hitting your nodes with their original IP addresses. This can become a problem when using the default Security Group configuration for your nodes. By default an AWS Network Load Balancer adds exceptions for both its own IP addresses and, if public, the internet (0.0.0.0/0). Unfortunately and in the case of internal AWS Network Load Balancer with client IP preservation enabled, your traffic matches none of them. Therefore you might need to manually add the source IP addresses of your other internal services accessing the load balancer to the nodes' Security Group configuration.

---------------------------------------------------

## Further reading

- [Running Multiple Ingress NGINX Controllers]({{< relref "/content/advanced/connectivity/ingress/multi-nginx-ic/index.md" >}})
- [Services of type LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#type-loadbalancer)
- [AWS Load Balancer Controller - Annotations](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.4/guide/service/annotations/)
- [Running Multiple Ingress NGINX Controllers](https://github.com/kubernetes/ingress-nginx#running-multiple-ingress-controllers)
- [Deploying the Ingress NGINX Controller]({{< relref "/getting-started/ingress-controller/index.md" >}})
- [Google GCP LoadBalancer Service parameters](https://cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters)
