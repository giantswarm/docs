---
title: Advanced ingress configuration
description: Here we describe how you can customize and enable specific features for the ingress nginx controller.
weight: 10
menu:
  principal:
    parent: tutorials-connectivity-ingress
    identifier: tutorials-connectivity-ingress-configuration
user_questions:
  - How can I allow only certain IPs for ingress access?
  - How can I assign requests to different services, based on the address path?
  - How can I configure ingress to use HTTPS when connecting to my internal service?
  - How can I configure basic authentication in an ingress resource?
  - How can I configure ingress to prevent DDoS attacks?
  - How can I configure request address rewrites in the ingress resource?
  - How can I configure ingress so requests of one session reach the same backend?
  - How can I connect several services in one ingress, based on the address path?
  - How can I define several ingresses in one ingress resource?
  - How can I disable the redirect to HTTPS in the ingress configuration?
  - How can I enable CORS headers in the ingress resource?
  - How can I enable TLS passthrough in ingress?
  - How can I let the ingress controller do TLS termination?
  - How can I rate-limit ingress requests?
  - How can I confgiure a different connection timeout for my ingress?
  - How can I change the ingress nginx controller configmap?
  - How can I use ingress nginx controller as a Web Application Firewall?
  - How can I protect my workload from malicious requests?
  - How can I enable & configure ModSecurity inside of the ingress nginx controller?
last_review_date: 2024-08-26
aliases:
  - /advanced/connectivity/ingress/configuration
  - /guides/advanced-ingress-configuration/
  - /advanced/ingress/configuration/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

The [ingress nginx controller](https://github.com/kubernetes/ingress-nginx) has additional configuration options and features that can be customized. The functionality is split into two categories:

- [Per-service options](#yaml) in each ingress' YAML definition either directly or via [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) ([Complete list of supported Annotations](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/)).
- [Global options](#configmap) that influence all ingresses of a cluster via a ConfigMap ([Complete list of ConfigMap options](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/)).

__Note__: Giant Swarm clusters don't come with an ingress controller pre-installed. See our [guide on how to install an ingress controller from the Giant Swarm catalog]({{< relref "/getting-started/install-an-application#install-ingress-controller" >}}).

## Per-Service options {#yaml}

### Aggregating ingresses

You can aggregate multiple ingress rules into a single ingress definition like following:

```yaml
apiVersion: networking.k8s.io/v1
kind: ingress
metadata:
  name: INGRESS_NAME
spec:
  ingressClassName: nginx
  rules:
  - host: YOUR_CHOICE_1.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: SERVICE_1_NAME
            port:
              number: SERVICE_1_PORT
  - host: YOUR_CHOICE_2.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: SERVICE_2_NAME
            port:
              number: SERVICE_2_PORT
```

__Note__: If you are using TLS you also need each of the hosts in the `tls` section (see below) of the YAML.

### Path Based Fan-out

You can route an ingress to different Services based on the path:

```yaml
apiVersion: networking.k8s.io/v1
kind: ingress
metadata:
  name: INGRESS_NAME
spec:
  ingressClassName: nginx
  rules:
  - host: YOUR_CHOICE_1.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /foo
        pathType: Prefix
        backend:
          service:
            name: SERVICE_1_NAME
            port:
              number: SERVICE_1_PORT
      - path: /bar
        pathType: Prefix
        backend:
          service:
            name: SERVICE_2_NAME
            port:
              number: SERVICE_2_PORT
```

__Note__: Your applications need to be capable of running on a non-root path either by default or by setting the base path in their configuration.

### Encryption

It's possible to configure TLS encryption in your ingress objects. You can either terminate TLS in your application by enabling SSL passthrough or let the ingress controller terminate it for you.

#### SSL passthrough

__Warning__: This feature was disabled by default in the ingress nginx controller managed by Giant Swarm. Reason is a potential [crash](https://github.com/kubernetes/ingress-nginx/issues/2354) of internal TCP proxy. We recommend to [terminate TLS in ingress controller](#terminating-tls-in-ingress-controller) instead.

For SSL passthrough you need to set an annotation and enable TLS for the host:

```yaml
apiVersion: networking.k8s.io/v1
kind: ingress
metadata:
  name: INGRESS_NAME
  annotations:
    nginx.ingress.kubernetes.io/ssl-passthrough: "true"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - YOUR_CHOICE.CLUSTER_ID.k8s.gigantic.io
  rules:
  - host: YOUR_CHOICE.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: SERVICE_NAME
            port:
              number: SERVICE_PORT
```

__Note__: SSL passthrough can't work with path based routing based on the nature of SSL.

#### Terminating TLS in the ingress controller

For terminating TLS in the ingress controller you first need to create a TLS secret containing your certificate and private key in the same namespace as the ingress object:

```yaml
apiVersion: v1
kind: Secret
type: kubernetes.io/tls
metadata:
  name: TLS_SECRET
data:
  tls.crt: BASE64_ENCODED_CERT
  tls.key: BASE64_ENCODED_KEY
```

__Note__: The data keys must be named `tls.crt` and `tls.key`!

Referencing this secret in an ingress will tell the ingress controller to secure the channel from the client to the ingress controller using TLS:

```yaml
apiVersion: networking.k8s.io/v1
kind: ingress
metadata:
  name: INGRESS_NAME
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - YOUR_CHOICE.CLUSTER_ID.k8s.gigantic.io
    secretName: TLS_SECRET
  rules:
  - host: YOUR_CHOICE.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: SERVICE_NAME
            port:
              number: SERVICE_PORT
```

__Note__: If you want to use [Let's Encrypt](https://letsencrypt.org/) certificates with your domains you can automate their creation and renewal with the help of [cert-manager](https://cert-manager.io/docs/). After configuring cert-manager there is only an annotation inside your ingresses needed and your web application will be secured by a valid TLS certificate. You can learn more about this behavior [here]({{< relref "/vintage/advanced/connectivity/tls-certificates" >}}).

### Authentication

The ingress controller includes support for adding authentication to an ingress rule. You have the choice between [Basic and Digest Access Authentication](https://datatracker.ietf.org/doc/html/rfc2617).

First, you need to create a file called `auth` containing your usernames and passwords (one per line). You can do this either by using the [`htpasswd`](https://httpd.apache.org/docs/current/programs/htpasswd.html) command line tool (like in the following example) or an online `htpasswd` generator.

```nohighlight
$ htpasswd -c auth foo1
New password: PASSWORD
New password:
Re-type new password:
Adding password for user foo1
```

You can add users to the same file with:

```nohighlight
$ htpasswd auth foo2
New password: PASSWORD
New password:
Re-type new password:
Adding password for user foo2
```

Next, we create a secret containing our `auth` file:

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: AUTH_SECRET
data:
  auth: BASE64_ENCODED_AUTH
```

Last, we create the ingress with the according annotations:

```yaml
apiVersion: networking.k8s.io/v1
kind: ingress
metadata:
  name: INGRESS_NAME
  annotations:
    # Authentication type [basic|digest]
    nginx.ingress.kubernetes.io/auth-type: basic
    # Name of the secret that contains the user/password definitions
    nginx.ingress.kubernetes.io/auth-secret: AUTH_SECRET
    # Message to display with an appropiate context why the authentication is required
    nginx.ingress.kubernetes.io/auth-realm: "Authentication Required - foo"
spec:
  ingressClassName: nginx
  rules:
  - host: YOUR_CHOICE.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: SERVICE_NAME
            port:
              number: SERVICE_PORT
```

### External Authentication

To use an existing service that provides authentication, the ingress rule can be annotated with `nginx.ingress.kubernetes.io/auth-url` to indicate the address where the HTTP request should be sent. Additionally, it's possible to set `nginx.ingress.kubernetes.io/auth-method` to specify the HTTP method (GET or POST).

This functionality is based on the [`auth_request`](https://nginx.org/en/docs/http/ngx_http_auth_request_module.html) module, which expects a `2xx` response code from the external service if the access is allowed and `401` or `403` if denied.

### Cross-Origin Resource Sharing

To enable Cross-Origin Resource Sharing (CORS) in an ingress rule add the annotation `nginx.ingress.kubernetes.io/enable-cors: "true"`.

### Rewrite

In some scenarios the exposed address in the backend service differs from the specified path in the ingress rule. Without a rewrite any request will return 404. To circumvent this you can set the annotation `nginx.ingress.kubernetes.io/rewrite-target` to the path expected by the service.

This can for example be used together with path based routing, when the application expects to be on `/`:

```yaml
apiVersion: networking.k8s.io/v1
kind: ingress
metadata:
  name: INGRESS_NAME
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: YOUR_CHOICE.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /foo
        pathType: Prefix
        backend:
          service:
            name: SERVICE_NAME
            port:
              number: SERVICE_PORT
```

### Rate limiting

The annotations `nginx.ingress.kubernetes.io/limit-connections` and `nginx.ingress.kubernetes.io/limit-rps` define a limit on the connections that can be opened by a single client IP address. This can be used to mitigate [DDoS Attacks](https://www.nginx.com/blog/mitigating-ddos-attacks-with-nginx-and-nginx-plus).

`nginx.ingress.kubernetes.io/limit-connections`: Number of concurrent connections allowed from a single IP address.

`nginx.ingress.kubernetes.io/limit-rps`: Number of connections that may be accepted from a given IP each second.

If you specify both annotations in a single ingress rule, `limit-rps` takes precedence.

### Secure backends

By default ingress nginx controller uses `http` to reach the services. Adding the annotation `nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"` in the ingress rule changes the protocol to `https`.

### Server-side HTTPS enforcement through redirect

By default the ingress nginx controller redirects (301) to `HTTPS` if TLS is enabled for that ingress. If you want to disable that behaviour, you can use the `nginx.ingress.kubernetes.io/ssl-redirect: "false"` annotation.

### Allowing list source range

You can specify the allowed client IP source ranges through the `nginx.ingress.kubernetes.io/allowlist-source-range` annotation. The value is a comma separated list of [CIDRs](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing), for example `10.0.0.0/24,172.10.0.1`.

__Note__: Adding an annotation to an ingress rule overrides any global restrictions set in the ingress nginx controller.

### Custom max body size

A 413 error will be returned to the client when the size in a request exceeds the maximum allowed size of the client request body. This size can be configured by the parameter [`client_max_body_size`](https://nginx.org/en/docs/http/ngx_http_core_module.html#client_max_body_size) and is set to `1m` (1 Megabyte) by default.

To configure this setting globally for all ingress rules, the `proxy-body-size` value may be set in the [ingress nginx controller ConfigMap](#configmap).

To use custom values in a specific ingress add following annotation:

```yaml
nginx.ingress.kubernetes.io/proxy-body-size: 8m
```

### Custom connection timeout

Ingress nginx controller allows you to define the timeout that waits to close a connection (`keepalive`) with your workload. You can define a value in the main [`configmap`](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#upstream-keepalive-timeout). The default value is `60` and it's measured in seconds.

Many other timeouts can be customized when configuring an ingress. Take a look at the [official docs](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#custom-timeouts).

__Warning__: When running in cloud provider environments, you may often rely on integrated services like AWS NLBs or Azure LBs. Those intermediate Load Balancers could have their own settings which can be in the request path conflicting with values defined in ingress Resources. [Read how to configure ingress nginx controller in cloud environments to avoid unexpected results]({{< relref "/vintage/advanced/connectivity/ingress/service-type-loadbalancer/index.md" >}}#other-aws-elb-configuration-options).

### Session affinity

The annotation `nginx.ingress.kubernetes.io/affinity` enables and sets the affinity type in all upstreams of an ingress. This way, a request will always be directed to the same upstream server.

#### Cookie affinity

If you use the `cookie` type you can also specify the name of the cookie that will be used to route the requests with the annotation `nginx.ingress.kubernetes.io/session-cookie-name`. The default is to create a cookie named `route`.

This feature is implemented by the third party module [nginx-sticky-module-ng](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng). The workflow used to define which upstream server will be used is explained in the [module documentation (PDF)](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng/raw/08a395c66e425540982c00482f55034e1fee67b6/docs/sticky.pdf).

### Configuration snippets

The ingress nginx controller creates an nginx configuration file. You can directly pass chunks of configuration, so-called _configuration snippets_, into any ingress manifest. These snippets will be added to the nginx configuration.

The _configuration snippets_ through ingress annotations is disabled by default. To enable parsing of _configuration snippets_, you must set `controller.allowSnippetAnnotations: true` in the [App configuration]({{< relref "/vintage/getting-started/app-platform/app-configuration/index.md" >}}).

__Warning__: We recommend enabling this option only if you TRUST users with permission to create ingress objects. Doing so may allow a user to add restricted configurations to the final `nginx.conf` file.

Here is an example of adding an `Expires` header to every response:

```yaml
apiVersion: networking.k8s.io/v1
kind: ingress
metadata:
  name: INGRESS_NAME
  annotations:
    nginx.ingress.kubernetes.io/configuration-snippet: |
      expires 24h;
spec:
  ingressClassName: nginx
  rules:
  - host: YOUR_CHOICE.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /foo
        pathType: Prefix
        backend:
          service:
            name: SERVICE_NAME
            port:
              number: SERVICE_PORT
```

Make sure to use the exact annotation scheme `nginx.ingress.kubernetes.io/configuration-snippet` in the `metadata` section of the manifest.

In case you want to set up a general HTTP snippet you can define it at [ingress nginx controller ConfigMap](#configmap) level.

## Global cluster options {#configmap}

Your Giant Swarm installation comes with a default configuration for the ingress controller.

You can override these defaults by setting your per-cluster configuration in a ConfigMap named `ingress-nginx-user-values` in the management cluster.

The page [App configuration reference]({{< relref "/vintage/getting-started/app-platform/app-configuration/index.md" >}}) contains more information on how to set user-defined configuration for the ingress nginx controller.

### Where's the user values ConfigMap

Given the cluster you are trying to configure has id: `123ab`

You will find the `ingress-nginx-user-values` ConfigMap on the management cluster in the `123ab` namespace:

```nohighlight
$ kubectl -n 123ab get configmap ingress-nginx-user-values
NAME                        DATA      AGE
ingress-nginx-user-values   0         11m
```

__Warning__:

Please don't edit any of the other ingress nginx controller related ConfigMaps.

Only the user ConfigMap is safe to edit.

---

### How to set configuration options using the user values ConfigMap

You are able to set any value from the [upstream documentation](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/) by including them in the user values ConfigMap under the `data.values` field like so:

```yaml
# On the management cluster
apiVersion: v1
kind: ConfigMap
metadata:
  name: ingress-nginx-user-values
  namespace: NAMESPACE
data:
  values: |
    controller:
      config:
        log-format-upstream: "MY EDITED LOG FORMAT - $status $body_bytes_sent $http_referer"
```

However keep in mind: With great power comes great responsibility!

If the ConfigMap doesn't exist, create it. In this case you'll need to reference it in the App CR of the ingress controller.

```yaml
# Add missing keys to the spec field of the App CR
spec:
  userConfig:
    configMap:
      name: ingress-nginx-user-values
      namespace: NAMESPACE
```

Any defaults we override are visible in the following `values.yaml` file under the `controller.config` key. Check this [`values.yaml`](https://github.com/giantswarm/ingress-nginx-app/blob/main/helm/ingress-nginx/values.yaml) as an example.

Don't copy all the defaults if you don't need to change them; that way, we can adjust them in case they need to be changed.

Please make sure you look at the right tag in that repository. When reading this file, check that the tag corresponds to the version of the ingress nginx controller running on your cluster.

### Configure proxy protocol

__Warning__:

We also allow setting `use-proxy-protocol: "true"/"false"`. This setting always applies globally for the ingress nginx controller.

#### Cluster API for AWS

The proxy protocol is enabled by default. It can be disabled by setting the `use-proxy-protocol` to `"false"`. For example:

```yaml
# On the management cluster
apiVersion: v1
kind: ConfigMap
metadata:
  name: ingress-nginx-user-values
  namespace: NAMESPACE
data:
  values: |
    controller:
      config:
        use-proxy-protocol: "false"
```

---

### Default certificate

When you want to have the default server on the ingress nginx controller support TLS you need to provide a certificate. This is configured using the flag `--default-ssl-certificate`. Now you can provide this value in the user values ConfigMap to force the component to be restarted with the provided certificate. The value of the property should be the namespace and secret name which holds the certificate content.

```yaml
data:
  values: |
    controller:
       extraArgs:
         default-ssl-certificate: <namespace>/<secret_name>
```

### Custom annotation prefix

By default we use the standard annotation prefix `nginx.ingress.kubernetes.io` in the ingress controller. In case you want to have a specific one this can be achieved via the user values ConfigMap:

```yaml
data:
  values: |
    controller:
      extraArgs:
        annotations-prefix: custom.prefix.io
```

### Web Application Firewall

The ingress nginx controller ships with the [ModSecurity](https://www.modsecurity.org) module, which can be used to enhance your ingress nginx controller deployment by Web Application Firewall capabilities to protect your workload against malicious requests.

While enabling those capabilities in the first step is easy, it might take some more effort to fine-tune it to your needs. Since, especially in blocking mode, even legal requests might get blocked; we recommend first running ModSecurity in the detection mode and observing its logs. At the same time, it already checks incoming traffic for malicious requests.

The included configuration is split into two parts: One is used for the basic setup of the ModSecurity module, and the other is the [OWASP ModSecurity Core Rule Set](https://coreruleset.org), which provides a collection of rules against common and well-known attack vectors. While both can be enabled in parallel, the former will keep the whole ModSecurity in the detection above mode by default until explicitly configured otherwise:

```yaml
data:
  values: |
    controller:
      config:
        # Enable ModSecurity.
        enable-modsecurity: "true"

        # Optional: Enable OWASP ModSecurity Core Rule Set.
        enable-owasp-modsecurity-crs: "true"
```

Adding your own configuration, like for activating the blocking mode, requires a configuration snippet which - at the moment of writing this - [removes the inclusion](https://github.com/kubernetes/ingress-nginx/blob/main/rootfs/etc/nginx/template/nginx.tmpl#L156-L171) of the basic ModSecurity configuration from the resulting nginx configuration (`nginx.conf`) inside your controller pods. Therefore we first need to re-include the default configuration before adding our own:

```yaml
data:
  values: |
    controller:
      config:
        # Enable ModSecurity.
        enable-modsecurity: "true"

        # Custom ModSecurity configuration.
        modsecurity-snippet: |-
          # Include defaults.
          Include /etc/nginx/modsecurity/modsecurity.conf

          # Enable rule engine. (Default: DetectionOnly)
          #SecRuleEngine On

          # Log to stdout. (Default: /var/log/modsec_audit.log)
          SecAuditLog /dev/stdout
          # Log serially. (Default: Concurrent)
          SecAuditLogType Serial
          # Log JSON. (Default: Native)
          #SecAuditLogFormat JSON

          # Disable rule 920350 due to false-positives on health checks.
          SecRuleRemoveById 920350

        # Optional: Enable OWASP ModSecurity Core Rule Set.
        enable-owasp-modsecurity-crs: "true"
```

The above configuration snippet makes ModSecurity send its logs to `/dev/stdout`, so you can process them like you're doing for access & error logs of the ingress nginx controller itself. Additionally, it disables [rule 920350](https://github.com/coreruleset/coreruleset/blob/v3.3/master/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L708-L736), which blocks direct access by IP, which is required for the Kubernetes probes to work. Without disabling this rule, your ingress nginx controller containers would start to get killed the moment you activate the blocking mode continuously. You would also see a lot of spam regarding this false positive in your logs, even in detection mode.

Suppose you don't want to maintain your ModSecurity configuration inside this snippet. In that case, you can also mount it as a volume into the ingress nginx controller pods and include it the same way we're including the default configuration above. In the following example, we first create a `ConfigMap` containing your custom configuration in the same namespace as the ingress nginx controller. This `ConfigMap` is then getting mounted into each of the ingress nginx controller pods by adding the `controller.extraVolumeMounts` user value:

```apacheconf
# modsecurity.conf
# Enable rule engine. (Default: DetectionOnly)
#SecRuleEngine On

# Log to stdout. (Default: /var/log/modsec_audit.log)
SecAuditLog /dev/stdout
# Log serially. (Default: Concurrent)
SecAuditLogType Serial
# Log JSON. (Default: Native)
#SecAuditLogFormat JSON

# Disable rule 920350 due to false-positives on health checks.
SecRuleRemoveById 920350
```

```sh
kubectl create configmap --namespace NAMESPACE ingress-nginx-controller-modsecurity --from-file modsecurity.conf
```

```yaml
data:
  values: |
    controller:
      # Additional volumes.
      extraVolumes:
      - name: modsecurity
        configMap:
          name: ingress-nginx-controller-modsecurity

      # Additional volume mounts.
      extraVolumeMounts:
      - name: modsecurity
        mountPath: /etc/nginx/modsecurity/custom/

      config:
        # Enable ModSecurity.
        enable-modsecurity: "true"

        # Custom ModSecurity configuration.
        modsecurity-snippet: |-
          # Include defaults.
          Include /etc/nginx/modsecurity/modsecurity.conf

          # Include custom configuration.
          Include /etc/nginx/modsecurity/custom/modsecurity.conf

        # Optional: Enable OWASP ModSecurity Core Rule Set.
        enable-owasp-modsecurity-crs: "true"
```

Last but not least and when you've tested all your workloads and fine-tuned ModSecurity to your needs, you can enable the blocking mode by enabling `SecRuleEngine` either in the configuration snippet or the configuration file mounted into the ingress nginx controller pods:

```apacheconf
# modsecurity.conf
# Enable rule engine. (Default: DetectionOnly)
SecRuleEngine On

# Log to stdout. (Default: /var/log/modsec_audit.log)
SecAuditLog /dev/stdout
# Log serially. (Default: Concurrent)
SecAuditLogType Serial
# Log JSON. (Default: Native)
#SecAuditLogFormat JSON

# Disable rule 920350 due to false-positives on health checks.
SecRuleRemoveById 920350
```

If you are currently writing ingress nginx controller access logs as JSON, you might also be interested in setting the `SecAuditLogFormat` to `JSON`, too. This directive is already included in the before shown configuration examples.

This section of the documentation is based on an article by Daniel Jimenez Garcia on System Weakness: [Kubernetes nginx ingress WAF with ModSecurity. From zero to hero!](https://systemweakness.com/nginx-ingress-waf-with-modsecurity-from-zero-to-hero-fa284cb6f54a)

## Further reading

- [Official Kubernetes documentation for the ingress Resource](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Configuration documentation for the ingress nginx controller](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/)
- [Official ingress nginx controller configuration snippets example](https://github.com/kubernetes/ingress-nginx/tree/main/docs/examples/customization/configuration-snippets)
