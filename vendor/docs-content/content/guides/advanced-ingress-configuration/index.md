+++
title = "Advanced Ingress Configuration"
description = "Here we describe how you can customize and enable specific features for the NGINX-based Ingress"
date = "2017-03-01"
type = "page"
weight = 50
tags = ["tutorial"]
+++

# Advanced Ingress Configuration

The [NGINX-based Ingress Controller](https://github.com/kubernetes/ingress/tree/master/controllers/nginx) running inside your cluster has additional configuration options and features that can be customized. The functionality is split into three categories:

- [Per-Service options](#yaml) in each Ingress' YAML definition either directly or via [Annotations](https://kubernetes.io/docs/user-guide/annotations/).
- [Global options](#configmap) that influence all Ingresses via a Config Map.
- A fully customized [NGINX template](#template)

## Per-Service Options {#yaml}

### Aggregating Ingresses

You can aggregate several Ingress rules into a single Ingress definition like following:

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: <ingress-name>
spec:
  rules:
  - host: <yourchoice1>.<cluster-id>.k8s.gigantic.io
    http:
      paths:
      - path: /
        backend:
          serviceName: <service1-name>
          servicePort: <service1-port>
  - host: <yourchoice2>.<cluster-id>.k8s.gigantic.io
    http:
      paths:
      - path: /
        backend:
          serviceName: <service2-name>
          servicePort: <service2-port>
```

__Note:__ If you are using TLS you also need each of the hosts in the `tls` section (see below) of the yaml.

### Path Based Fanout

You can route an Ingress to different Services based on the path:

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: <ingress-name>
spec:
  rules:
  - host: <yourchoice>.<cluster-id>.k8s.gigantic.io
    http:
      paths:
      - path: /foo
        backend:
          serviceName: <service1-name>
          servicePort: <service1-port>
      - path: /bar
        backend:
          serviceName: <service2-name>
          servicePort: <service2-port>
```

__Note:__ Your applications need to be capable of running on a non-root path either by default or by setting the base path in their configuration.

### TLS

If your cluster has TLS enabled, you can terminate TLS either in your application itself by enabling SSL passthrough or let the Ingress Controller terminate for you.

#### SSL Passthrough

For SSL passthrough you need to set an annotation and enable TLS for the host:

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: <ingress-name>
  annotations:
    ingress.kubernetes.io/ssl-passthrough: "true"
spec:
   tls:
   - hosts:
     - <yourchoice>.<cluster-id>.k8s.gigantic.io
  rules:
  - host: <yourchoice>.<cluster-id>.k8s.gigantic.io
    http:
      paths:
      - path: /
        backend:
          serviceName: <service-name>
          servicePort: <service-port>
```

__Note:__ SSL passthrough cannot work with path based routing based on the nature of SSL.

#### Terminating TLS in Ingress Controller

For terminating TLS in the Ingress Controller you need to first create a TLS secret containing your certificate and private key in the same namespace as the Ingress object:

```yaml
apiVersion: v1
kind: Secret
type: kubernetes.io/tls
metadata:
  name: mytlssecret
data:
  tls.crt: <base64 encoded cert>
  tls.key: <base64 encoded key>
```

__Note:__ the data keys must be named `tls.crt` and `tls.key`!

Referencing this secret in an Ingress will tell the Ingress Controller to secure the channel from the client to the loadbalancer using TLS:

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: <ingress-name>
spec:
   tls:
   - hosts:
     - <yourchoice>.<cluster-id>.k8s.gigantic.io
     secretName: mytlssecret
  rules:
  - host: <yourchoice>.<cluster-id>.k8s.gigantic.io
    http:
      paths:
      - path: /
        backend:
          serviceName: <service-name>
          servicePort: <service-port>
```

### Authentication

The Ingress Controller includes support for adding authentication to an Ingress rule. You have the choice between [basic or digest http authentication types](https://tools.ietf.org/html/rfc2617).

First, you need to create a file called `auth` containing your usernames and passwords (one per line). You can do this either by using the [`htpasswd`](https://httpd.apache.org/docs/current/programs/htpasswd.html) command line tool (like in the following example) or an online htpasswd generator.

```nohighlight
$ htpasswd -c auth foo1
New password: <bar>
New password:
Re-type new password:
Adding password for user foo1
```

You can add users to the same file with:

```nohighlight
$ htpasswd auth foo2
New password: <bar>
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
  name: myauthsecret
data:
  auth: <base64 encoded auth>
```

Last, we create the Ingress with the according annotations:

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: <ingress-name>
  annotations:
    # type of authentication [basic|digest]
    ingress.kubernetes.io/auth-type: basic
    # name of the secret that contains the user/password definitions
    ingress.kubernetes.io/auth-secret: myauthsecret
    # message to display with an appropiate context why the authentication is required
    ingress.kubernetes.io/auth-realm: "Authentication Required - foo"
spec:
  rules:
  - host: <yourchoice>.<cluster-id>.k8s.gigantic.io
    http:
      paths:
      - path: /
        backend:
          serviceName: <service-name>
          servicePort: <service-port>
```

### External Authentication

To use an existing service that provides authentication the Ingress rule can be annotated with `ingress.kubernetes.io/auth-url` to indicate the URL where the HTTP request should be sent. Additionally it is possible to set `ingress.kubernetes.io/auth-method` to either `GET` (default) or `POST` and `ingress.kubernetes.io/auth-send-body` to `true` or `false` (default).

This functionality is based on the [auth_request](http://nginx.org/en/docs/http/ngx_http_auth_request_module.html) module, which expects a `2xx` response code from the external service if the access is allowed and `401` or `403` if denied.

### CORS

To enable Cross-Origin Resource Sharing (CORS) in an Ingress rule add the annotation `ingress.kubernetes.io/enable-cors: "true"`.

### Rewrite

In some scenarios the exposed URL in the backend service differs from the specified path in the Ingress rule. Without a rewrite any request will return 404. To circumvent this you can set the annotation `ingress.kubernetes.io/rewrite-target` to the path expected by the service.

This can for example be used together with path based routing, when the application expects to be on `/`:

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: <ingress-name>
  annotations:
    ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: <yourchoice>.<cluster-id>.k8s.gigantic.io
    http:
      paths:
      - path: /foo
        backend:
          serviceName: <service-name>
          servicePort: <service1port>
```

If the application contains relative links it is possible to add an additional annotation `ingress.kubernetes.io/add-base-url` that will prepend a [`base` tag](https://developer.mozilla.org/en/docs/Web/HTML/Element/base) in the header of the returned HTML from the backend.

### Rate limiting

The annotations `ingress.kubernetes.io/limit-connections` and `ingress.kubernetes.io/limit-rps` define a limit on the connections that can be opened by a single client IP address. This can be used to mitigate [DDoS Attacks](https://www.nginx.com/blog/mitigating-ddos-attacks-with-nginx-and-nginx-plus).

`ingress.kubernetes.io/limit-connections`: number of concurrent connections allowed from a single IP address.

`ingress.kubernetes.io/limit-rps`: number of connections that may be accepted from a given IP each second.

If you specify both annotations in a single Ingress rule, `limit-rps` takes precedence.

### Secure backends

By default NGINX uses `http` to reach the services. Adding the annotation `ingress.kubernetes.io/secure-backends: "true"` in the Ingress rule changes the protocol to `https`.

### Server-side HTTPS enforcement through redirect

By default the controller redirects (301) to `HTTPS` if TLS is enabled for that Ingress. If you want to disable that behaviour, you can use the `ingress.kubernetes.io/ssl-redirect: "false"` annotation.

### Whitelist source range

You can specify the allowed client IP source ranges through the `ingress.kubernetes.io/whitelist-source-range` annotation. The value is a comma separated list of [CIDRs](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing), e.g.  `10.0.0.0/24,172.10.0.1`.

__Note:__ Adding an annotation to an Ingress rule overrides any global restrictions set in the NGINX Ingress Controller.

### Custom max body size

A 413 error will be returned to the client when the size in a request exceeds the maximum allowed size of the client request body. This size can be configured by the parameter [`client_max_body_size`](http://nginx.org/en/docs/http/ngx_http_core_module.html#client_max_body_size) and is set to `1m` (1 Megabyte) by default.

To configure this setting globally for all Ingress rules, the `proxy-body-size` value may be set in the [NGINX ConfigMap](#configmap).

To use custom values in a specific Ingress add following annotation:

```
ingress.kubernetes.io/proxy-body-size: 8m
```

### Session Affinity

The annotation `ingress.kubernetes.io/affinity` enables and sets the affinity type in all Upstreams of an Ingress. This way, a request will always be directed to the same upstream server. 

#### Cookie affinity

If you use the `cookie` type you can also specify the name of the cookie that will be used to route the requests with the annotation `ingress.kubernetes.io/session-cookie-name`. The default is to create a cookie named `route`.

The annotation `ingress.kubernetes.io/session-cookie-hash` defines which algorithm will be used to hash the used upstream. Default value is `md5` and possible values are `md5`, `sha1` and `index`.

The `index` option is not hashed, an in-memory index is used instead, it's quicker and the overhead is shorter. Warning: The matching against the upstream servers list is inconsistent. So, at reload, if upstreams servers have changed, index values are not guaranted to correspond to the same server as before! Use with caution and only if you need to!

This feature is implemented by the third party module [nginx-sticky-module-ng](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng). The workflow used to define which upstream server will be used is explained in the [module documentation (PDF)](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng/raw/08a395c66e425540982c00482f55034e1fee67b6/docs/sticky.pdf).

## Global Options {#configmap}

Your Ingress Controller can be further customized using a ConfigMap named `ingress-controller-config-custom` located in your `kube-system` namespace.

The official documentation of the NGINX Ingress Controller contains a [list of allowed parameters](https://github.com/kubernetes/ingress/blob/master/controllers/nginx/configuration.md#allowed-parameters-in-configuration-configmap) as well as the [default configuration options](https://github.com/kubernetes/ingress/blob/master/controllers/nginx/configuration.md#default-configuration-options).

## Custom NGINX Template {#template}

There's a default `nginx.tmpl` mounted to the right path in your Ingress Controller. You can find it in your `kube-system` namespace as a ConfigMap called `ingress-controller-config-template`. You can edit the template to configure advanced options that are available in NGINX, but cannot be set via [Ingress YAML](#yaml) or [Custom ConfigMap](#configmap) like described above.

__Note:__ Editing the template can result in a broken Ingress Controller, so handle with care. Furthermore, the template is tied to the Go code of the Ingress Controller. Do not change names in the variable `$cfg`. 

For more information about the template syntax please refer to the [upstream NGINX Controller Documentation](https://github.com/kubernetes/ingress/blob/master/controllers/nginx/configuration.md#custom-nginx-template)

## Further reading
- [Official Kubernetes documentation for the Ingress Resource](http://kubernetes.io/docs/user-guide/ingress/)
- [Configuration documentation for the NGINX Ingress Controller](https://github.com/kubernetes/ingress/blob/master/controllers/nginx/configuration.md)
