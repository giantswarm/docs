---
title: Services of type LoadBalancer
description: Learn how to expose services directly on cloud providers through Services of type LoadBalancer.
weight: 35
menu:
  main:
    parent: advanced-ingress
aliases:
  - /guides/services-of-type-loadbalancer-and-multiple-ingress-controllers/
  - /advanced/ingress/service-type-loadbalancer-multi-ic/
owner:
  - https://github.com/orgs/giantswarm/teams/team-halo
user_questions:
  - How can I expose Services to the internet?
  - How do I configure an Ingress Controller that is behind an internal ELB for traffic between services within the VPC (or a group of peered VPCs)?
  - How do I configure an Ingress Controller behind an ELB that already terminates SSL?
  - How do I configure an Ingress Controller with different functionality or performance?
---

# Services of type LoadBalancer

Next to using the default NGINX Ingress Controller, on cloud providers (currently AWS and Azure), you can expose services directly outside your cluster by using Services of type `LoadBalancer`.

You can use this to [expose single Services](#service-of-type-lb) to the internet. It is also possible, to [install additional NGINX Ingress Controllers]({{< relref "/content/advanced/ingress/multi-nginx-ic/index.md" >}}) to expose a subset of your Services with a different Ingress Controller configuration.

__Note__ that this functionality cannot be used on premises.

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
    service.beta.kubernetes.io/aws-load-balancer-internal: 0.0.0.0/0
```

On Azure you can configure internal Load Balancers like this.

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/azure-load-balancer-internal: "true"
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
    service.beta.kubernetes.io/aws-load-balancer-access-log-emit-interval: 60
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

#### AWS network load balancer

AWS is in the process of replacing ELBs with NLBs (Network Load Balancers) and ALBs (Application Load
Balancers). NLBs have a number of benefits over "classic" ELBs including scaling to many more requests.
Alpha support for NLBs was added in Kubernetes 1.9. As it's an alpha feature it's not yet recommended
for production workloads but you can start trying it out.

```yaml
metadata:
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
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

## Further reading

- [Running Multiple NGINX Ingress Controllers]({{< relref "/content/advanced/ingress/multi-nginx-ic/index.md" >}})
- [Services of type LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#type-loadbalancer)
- [Running Multiple Ingress Controllers](https://github.com/kubernetes/ingress-nginx#running-multiple-ingress-controllers)
- [Deploying the NGINX Ingress Controller](https://github.com/kubernetes/ingress-nginx/tree/master/deploy)
