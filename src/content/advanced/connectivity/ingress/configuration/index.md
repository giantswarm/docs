---
title: Advanced Ingress configuration
linkTitle: Advanced Ingress configuration
description: Here we describe how you can customize and enable specific features for the Ingress NGINX Controller.
weight: 10
menu:
  main:
    parent: advanced-ingress
user_questions:
  - How can I allow only certain IPs for Ingress access?
  - How can I assign requests to different services, based on the URL path?
  - How can I configure ingress to use HTTPS when connecting to my internal service?
  - How can I configure basic authentication in an Ingress resource?
  - How can I configure ingress to prevent DDoS attacks?
  - How can I configure request URL rewrites in the Ingress resource?
  - How can I configure ingress so requests of one session reach the same backend?
  - How can I connect several services in one Ingress, based on the URL path?
  - How can I define several ingresses in one Ingress resource?
  - How can I disable the redirect to HTTPS in the Ingress configuration?
  - How can I enable CORS headers in the Ingress resource?
  - How can I enable TLS passthrough in Ingress?
  - How can I let the Ingress Controller do TLS termination?
  - How can I rate-limit ingress requests?
  - How can I confgiure a different connection timeout for my ingress?
  - How can I change the Ingress NGINX Controller configmap?
  - How can I use Ingress NGINX Controller as a Web Application Firewall?
  - How can I protect my workload from malicious requests?
  - How can I enable & configure ModSecurity inside of the Ingress NGINX Controller?
last_review_date: 2023-11-07
aliases:
  - /guides/advanced-ingress-configuration/
  - /advanced/ingress/configuration/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

The [Ingress NGINX Controller](https://github.com/kubernetes/ingress-nginx) has additional configuration options and features that can be customized. The functionality is split into two categories:

- [Per-service options](#yaml) in each Ingress' YAML definition either directly or via [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) ([Complete list of supported Annotations](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/)).
- [Global options](#configmap) that influence all Ingresses of a cluster via a ConfigMap ([Complete list of ConfigMap options](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/)).

**Note**: Giant Swarm clusters do not come with an Ingress Controller pre-installed. See our [guide on how to install an Ingress Controller from the Giant Swarm Catalog]({{< relref "/getting-started/connectivity/ingress-controller" >}}).

## Per-Service options {#yaml}

### Aggregating Ingresses

You can aggregate multiple Ingress rules into a single Ingress definition like following:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
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

**Note:** If you are using TLS you also need each of the hosts in the `tls` section (see below) of the yaml.

### Path Based Fanout

You can route an Ingress to different Services based on the path:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
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

**Note:** Your applications need to be capable of running on a non-root path either by default or by setting the base path in their configuration.

### TLS

It is possible to configure TLS encryption in your Ingress objects. You can either terminate TLS in your application by enabling SSL passthrough or let the Ingress Controller terminate it for you.

#### SSL passthrough

**Warning:** This feature was disabled by default in the Ingress NGINX Controller managed by Giant Swarm. Reason is a potential [crash](https://github.com/kubernetes/ingress-nginx/issues/2354) of internal TCP proxier. We recommend to [terminate TLS in Ingress Controller](#terminating-tls-in-ingress-controller) instead.

For SSL passthrough you need to set an annotation and enable TLS for the host:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
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

**Note:** SSL passthrough cannot work with path based routing based on the nature of SSL.

#### Terminating TLS in the Ingress Controller

For terminating TLS in the Ingress Controller you first need to create a TLS secret containing your certificate and private key in the same namespace as the Ingress object:

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

**Note:** The data keys must be named `tls.crt` and `tls.key`!

Referencing this secret in an Ingress will tell the Ingress Controller to secure the channel from the client to the Ingress Controller using TLS:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
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

**Tip:** If you want to use [Let's Encrypt](https://letsencrypt.org/) certificates with your domains you can automate their creation and renewal with the help of [cert-manager](https://cert-manager.io/docs/). After configuring cert-manager there is only an annotation inside your Ingresses needed and your web application will be secured by a valid TLS certificate. You can learn more about this behavior [here]({{< relref "/advanced/connectivity/tls-certificates" >}}).

### Authentication

The Ingress Controller includes support for adding authentication to an Ingress rule. You have the choice between [Basic and Digest Access Authentication](https://datatracker.ietf.org/doc/html/rfc2617).

First, you need to create a file called `auth` containing your usernames and passwords (one per line). You can do this either by using the [`htpasswd`](https://httpd.apache.org/docs/current/programs/htpasswd.html) command line tool (like in the following example) or an online htpasswd generator.

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

Last, we create the Ingress with the according annotations:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
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

To use an existing service that provides authentication the Ingress rule can be annotated with `nginx.ingress.kubernetes.io/auth-url` to indicate the URL where the HTTP request should be sent. Additionally it is possible to set `nginx.ingress.kubernetes.io/auth-method` to specify the HTTP method to use (GET or POST).

This functionality is based on the [auth_request](https://nginx.org/en/docs/http/ngx_http_auth_request_module.html) module, which expects a `2xx` response code from the external service if the access is allowed and `401` or `403` if denied.

### CORS

To enable Cross-Origin Resource Sharing (CORS) in an Ingress rule add the annotation `ingress.kubernetes.io/enable-cors: "true"`.

### Rewrite

In some scenarios the exposed URL in the backend service differs from the specified path in the Ingress rule. Without a rewrite any request will return 404. To circumvent this you can set the annotation `ingress.kubernetes.io/rewrite-target` to the path expected by the service.

This can for example be used together with path based routing, when the application expects to be on `/`:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
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

If the application contains relative links it is possible to add an additional annotation `ingress.kubernetes.io/add-base-url` that will prepend a [`base` tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base) in the header of the returned HTML from the backend.

### Rate limiting

The annotations `ingress.kubernetes.io/limit-connections` and `ingress.kubernetes.io/limit-rps` define a limit on the connections that can be opened by a single client IP address. This can be used to mitigate [DDoS Attacks](https://www.nginx.com/blog/mitigating-ddos-attacks-with-nginx-and-nginx-plus).

`nginx.ingress.kubernetes.io/limit-connections`: Number of concurrent connections allowed from a single IP address.

`nginx.ingress.kubernetes.io/limit-rps`: Number of connections that may be accepted from a given IP each second.

If you specify both annotations in a single Ingress rule, `limit-rps` takes precedence.

### Secure backends

By default Ingress NGINX Controller uses `http` to reach the services. Adding the annotation `nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"` in the Ingress rule changes the protocol to `https`.

### Server-side HTTPS enforcement through redirect

By default the Ingress NGINX Controller redirects (301) to `HTTPS` if TLS is enabled for that Ingress. If you want to disable that behaviour, you can use the `nginx.ingress.kubernetes.io/ssl-redirect: "false"` annotation.

### Allowlist source range

You can specify the allowed client IP source ranges through the `nginx.ingress.kubernetes.io/allowlist-source-range` annotation. The value is a comma separated list of [CIDRs](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing), e.g. `10.0.0.0/24,172.10.0.1`.

**Note:** Adding an annotation to an Ingress rule overrides any global restrictions set in the Ingress NGINX Controller.

### Custom max body size

A 413 error will be returned to the client when the size in a request exceeds the maximum allowed size of the client request body. This size can be configured by the parameter [`client_max_body_size`](https://nginx.org/en/docs/http/ngx_http_core_module.html#client_max_body_size) and is set to `1m` (1 Megabyte) by default.

To configure this setting globally for all Ingress rules, the `proxy-body-size` value may be set in the [Ingress NGINX Controller ConfigMap](#configmap).

To use custom values in a specific Ingress add following annotation:

```yaml
nginx.ingress.kubernetes.io/proxy-body-size: 8m
```

### Custom connection timeout

Ingress NGINX Controller allows to define the timeout that waits to close a connection (`keepalive`) with your workload. You can define a value in the main [Config Map](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#upstream-keepalive-timeout). The default value is `60` and it is measured in seconds.

There are many other timeouts that can be customized when configuring an Ingress. Take a look at the [official docs](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#custom-timeouts).

**Warning**: When running in cloud provider environments you may often rely on integrated services like AWS NLBs or Azure LBs. Those intermediate Load Balancers could have their own settings which can be in the request path conflicting with values defined in Ingress Resources. [Read how to configure Ingress NGINX Controller in cloud environments to avoid unexpected results]({{< relref "/advanced/connectivity/ingress/service-type-loadbalancer/index.md" >}}#other-aws-elb-configuration-options).

### Session Affinity

The annotation `nginx.ingress.kubernetes.io/affinity` enables and sets the affinity type in all upstreams of an Ingress. This way, a request will always be directed to the same upstream server.

#### Cookie affinity

If you use the `cookie` type you can also specify the name of the cookie that will be used to route the requests with the annotation `nginx.ingress.kubernetes.io/session-cookie-name`. The default is to create a cookie named `route`.

The annotation `nginx.ingress.kubernetes.io/session-cookie-hash` defines which algorithm will be used to hash the used upstream. Default value is `md5` and possible values are `md5`, `sha1` and `index`.

The `index` option is not hashed, an in-memory index is used instead, it's quicker and the overhead is shorter. Warning: The matching against the upstream servers list is inconsistent. So, at reload, if upstreams servers have changed, index values are not guaranted to correspond to the same server as before! Use with caution and only if you need to!

This feature is implemented by the third party module [nginx-sticky-module-ng](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng). The workflow used to define which upstream server will be used is explained in the [module documentation (PDF)](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng/raw/08a395c66e425540982c00482f55034e1fee67b6/docs/sticky.pdf).

### Configuration snippets

The Ingress NGINX Controller creates an NGINX configuration file. You can directly pass chunks of configuration, so-called _configuration snippets_, into any Ingress manifest. These snippets will be added to the NGINX configuration.

The _configuration snippets_ through Ingress annotations is disabled by default. To enable parsing of _configuration snippets_, you'll need to set `controller.allowSnippetAnnotations: true` in the [App configuration]({{< relref "/getting-started/app-platform/app-configuration/index.md" >}}).

Warning: We recommend enabling this option only if you TRUST users with permission to create Ingress objects, as this may allow a user to add restricted configurations to the final `nginx.conf` file.

Here is an example adding an `Expires` header to every response:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
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

In case you want to set up a general http snippet you can define it at [Ingress NGINX Controller ConfigMap](#configmap) level.

## Global (per cluster) options {#configmap}

Your Giant Swarm installation comes with a default configuration for the Ingress Controller.

You can override these defaults by setting your per cluster configuration in the form of a ConfigMap named `ingress-nginx-user-values` in the management cluster.

The page [App configuration reference]({{< relref "/getting-started/app-platform/app-configuration/index.md" >}}) contains more information how to set user defined configuration for the Ingress NGINX Controller.

### Where is the user values ConfigMap

Given the cluster you are trying to configure has id: `123ab`

You will find the `ingress-nginx-user-values` ConfigMap on the management cluster in the `123ab` namespace:

```nohighlight
$ kubectl -n 123ab get configmap ingress-nginx-user-values
NAME                        DATA      AGE
ingress-nginx-user-values   0         11m
```

**Warning:**

Please do not edit any of the other Ingress NGINX Controller related ConfigMaps.

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

If the ConfigMap does not exist, create it. In this case you'll need to reference it in the App CR of the Ingress Controller.

```yaml
# Add missing keys to the spec field of the App CR
spec:
  userConfig:
    configMap:
      name: ingress-nginx-user-values
      namespace: NAMESPACE
```

Any defaults that we override are visible in the following `values.yaml` file, under the `controller.config` key. Check this [`values.yaml`](https://github.com/giantswarm/ingress-nginx-app/blob/main/helm/ingress-nginx/values.yaml) as an example.

Do not copy all the defaults if you do not need to change them, that way we can adjust them in case they need to change.

Do make sure you look at the right tag of that repository, when reading this file check that the tag corresponds to the version of the Ingress NGINX Controller running on your cluster.

### Configure Proxy Protocol

**Warning:**

We also allow setting `use-proxy-protocol: "true"/"false"`. This setting always applies globally for the Ingress NGINX Controller.

#### AWS / CAPA

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

When you want to have the default server on the Ingress NGINX Controller support TLS you need to provide a certificate. This is configured using the flag `--default-ssl-certificate`. Now you can provide this value in the user values ConfigMap to force the component to be restarted with the provided certificate. The value of the property should be the namespace and secret name which holds the certificate content.

```yaml
data:
  values: |
    controller:
       extraArgs:
         default-ssl-certificate: <namespace>/<secret_name>
```

### Custom annotation prefix

By default we use the standard annotation prefix `nginx.ingress.kubernetes.io` in the Ingress Controller. In case you want to have a specific one this can be achieved via the user values ConfigMap:

```yaml
data:
  values: |
    controller:
      extraArgs:
        annotations-prefix: custom.prefix.io
```

### Web Application Firewall

Ingress NGINX Controller ships with the [ModSecurity](https://www.modsecurity.org) module which can be used for enhancing your Ingress NGINX Controller deployment by Web Application Firewall capabilities to protect your workload against malicious requests.

While enabling those capabilities in the first step is quite easy, it might take some more effort to actually fine-tune it to your needs. Since especially in blocking mode even legal requests might get blocked, we recommend to first run ModSecurity in the detection mode and observe its logs while it already checks incoming traffic for malicious requests.

The included configuration is split into two parts: One is used for the basic setup of the ModSecurity module, the other is the [OWASP ModSecurity Core Rule Set](https://coreruleset.org) which provides a collection of rules against common and well-known attack vectors. While both can be enabled in parallel, the former will keep the whole ModSecurity in the before mentioned detection mode by default until explicitly configured otherwise:

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

Adding your own configuration, like for activating the blocking mode, requires a configuration snippet which - at the moment of writing this - [removes the inclusion](https://github.com/kubernetes/ingress-nginx/blob/main/rootfs/etc/nginx/template/nginx.tmpl#L156-L171) of the basic ModSecurity configuration from the resulting NGINX configuration (`nginx.conf`) inside your controller pods. Therefore we first need to re-include the default configuration before adding our own:

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

The above configuration snippet makes ModSecurity send its logs to `/dev/stdout`, so you can process them in the same way you're doing for access & error logs of Ingress NGINX Controller itself. Additionally it disables [rule 920350](https://github.com/coreruleset/coreruleset/blob/v3.3/master/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf#L708-L736), which blocks direct access by IP, which is required for the Kubernetes probes to work. Without disabling this rule, your Ingress NGINX Controller containers would start to repeatedly get killed the moment you activate the blocking mode. Apart from that, you would see a lot of spam regarding this false-positive in your logs even in detection mode.

If you do not want to maintain your ModSecurity configuration inside this snippet, you can also mount it as a volume into the Ingress NGINX Controller pods and include it the same way we are including the default configuration above. In the following example we first create a `ConfigMap` containing your custom configuration in the same namespace as the Ingress NGINX Controller. This `ConfigMap` is then getting mounted into each of the Ingress NGINX Controller pods by adding the `controller.extraVolumeMounts` user value:

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

Last but not least and when you've tested all your workloads and fine-tuned ModSecurity to your needs, you can enable the blocking mode by enabling `SecRuleEngine` either in the configuration snippet or the configuration file mounted into the Ingress NGINX Controller pods:

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

If you are currently writing Ingress NGINX Controller access logs as JSON, you might also be interested in setting the `SecAuditLogFormat` to `JSON`, too. This directive is already included in the before shown configuration examples.

This section of the documentation is based on an article by Daniel Jimenez Garcia on System Weakness: [Kubernetes NGINX Ingress WAF with ModSecurity. From zero to hero!](https://systemweakness.com/nginx-ingress-waf-with-modsecurity-from-zero-to-hero-fa284cb6f54a)

## Further reading

- [Official Kubernetes documentation for the Ingress Resource](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Configuration documentation for the Ingress NGINX Controller](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/)
- [Official Ingress NGINX Controller configuration snippets example](https://github.com/kubernetes/ingress-nginx/tree/main/docs/examples/customization/configuration-snippets)
