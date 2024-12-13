---
linkTitle: Container image cache in the cluster
title: Setting up a caching container registry within a cluster using Zot
description: A registry cache within the cluster can provide benefits for availability, performance, and cost. Here we explain how to set up a registry, using the Zot app provided by Giant Swarm.
weight: 110
menu:
  principal:
    parent: tutorials-registry
    identifier: tutorials-registry-in-cluster-cache-using-zot
user_questions:
  - How can I cache container images within the cluster?
  - How can I have a backup registry for container images?
last_review_date: 2024-10-31
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

A registry cache within the cluster can provide several benefits.

- Availability, in case the upstream registry is experiencing an outage
- Pull limits are enforced by certain upstream registries
- Faster boot times simply because of being closer to the cluster

Here we explain how to set up a registry, using the [Zot](https://zotregistry.dev/) app provided by Giant Swarm. Zot is an OCI-native container image registry. The [Giant Swarm packaged version](https://github.com/giantswarm/zot) extends it with opinionated components like
autoscaling, monitoring, Cilium network policies, etc.

We explain how to deploy apps in our [app platform docs]({{< relref "/tutorials/fleet-management/app-platform/deploy-app/#creating-an-app-resource" >}}).

## Zot configuration

The Zot binary itself can be configured via `.configFiles.config.json` Helm value as JSON. The `.mountConfig` values must be set to `true` to enable mounting the configuration file.

```yaml
configFiles:
  config.json: |-
    {
      # ...
    }
```

The Zot project provides a [full configuration reference](https://zotregistry.dev/latest/admin-guide/admin-configuration/) with more details.

## Caching strategies

You can configure either active or on-demand replication via the Zot configuration file.

- __Active__ (`onDemand: false`) means that Zot will actively sync images from the upstream registry, to have it available when needed.
- __On-demand__ (`onDemand: true`) means that Zot will only pull the image when it's requested, and then cache it.

The below example configures `docker.io` as on-demand mirror, while the `my-registry.example.org` registry it's set to actively sync all `6.*` tagged images for `my-organization/my-image`.

```json
{
  "extensions": {
    "sync": {
      "enable": true,
      "registries": [
        {
          "urls": [
            "https://docker.io/library"
          ],
          "onDemand": true,
          "tlsVerify": true,
          "maxRetries": 3,
          "retryDelay": "5m"
        },
        {
          "urls": [
            "https://my-registry.example.org"
          ],
          "onDemand": false,
          "pollInterval": "5m",
          "tlsVerify": true,
          "maxRetries": 3,
          "retryDelay": "5m",
          "onlySigned": false,
          "content": [
            {
              "prefix": "my-organization/my-image",
              "tags": {
                "regex": "^6.*",
                "semver": true
              }
            }
          ]
        }
      ]
    }
  }
}
```

<!-- Please update the section below once containerd mirroring configuration is settled -->

__Note:__ For Zot to be used on the cluster, you need to for example configure containerd on the nodes to use Zot as a mirror for given upstream registries. The containerd configuration in Giant Swarm clusters is currently subject to change. Please reach out to Giant Swarm support for the latest information.

For the full mirroring documentation, check the [upstream documentation](https://zotregistry.dev/latest/articles/mirroring/).

## Restricting access to container images

If not configured specifically, access to the registry is public for anonymous users. This means that all workloads within the cluster can pull images from it.

To restrict access, you have to add configuration. Since Zot supports a variety of authentication mechanisms, we only provide an example here, using Basic authentication. For all the possible authentication methods, please refer to the [Zot authentication docs](https://zotregistry.dev/latest/admin-guide/admin-configuration/#authentication).

To configure Basic authentication, set the `.secretFiles` Helm value and make sure `.mountSecret` is set to `true`, as shown in the example below. The `.secretFiles` content represents an  `htpasswd` file with one user and password per line.

To generate the user entries, use the `htpasswd` tool like here, where we create two different users named `admin` and `reader`:

```shell
htpasswd -bBn admin password
htpasswd -bBn reader password
```

Store the output like shown in the example:

```yaml
mountSecret: true
secretFiles:
  htpasswd: |-
    admin:$2y$05$.fR2nhyzstpecApibWVQDOg12aeXG8I4Zq8fW/ez8VJJ9zSc8zBQi
    reader:$2y$05$20dysb7065watYOcYZLo/unDEWgB0Lr6SAB7/hcyZVhtvZNkbN8rW
```

Finally, enable it via the `"http"` key in the configuration file:

```json
{
  ...
  "http": {
    "auth": {
      "htpasswd": {
        "path": "/secret/htpasswd"
      }
    },
    "accessControl": {
      "repositories": {
        "**": {
          "policies": [
            {
              "users": [
                "admin"
              ],
              "actions": [
                "read",
                "create",
                "update",
                "delete"
              ]
            },
            {
              "users": [
                "reader"
              ],
              "actions": [
                "read",
              ]
            }
          ]
        }
      }
    },
    "address": "0.0.0.0",
    "port": "5000"
  }
  ...
}
```

Note how the `"policies"` key is used to define the access control for the repositories. The `"**"` key is a wildcard for all repositories. The `"actions"` key defines the allowed actions for the users.

### Exposing the registry

In some use-cases you possibly want to expose Zot to be used by let's say workload clusters, so you manage only a single instance by sharing it across multiple workloads.

To enable the ingress in the Giant Swarm managed chart, use these settings matching your cluster:

```yaml
ingress:
  enabled: true
  hosts:
    - host: my-registry.example.org
      paths:
        - path: /
  tls:
    - secretName: my-registry-tls
      hosts:
        - my-registry.example.org
```

For private clusters, the ingress needs to be annotated differently from the default for Cert Manager to generate a proper certificate.

```yaml
ingress:
  annotations:
    cert-manager.io/cluster-issuer: private-giantswarm
```

### Authenticating with the upstream registry

In case you want to cache container images from private registries, Zot needs credentials for accessing them. In order to provide these credentials, add an entry to the `.secretFiles` key in chart values. Here is an example snippet:

```yaml
secretFiles:
  credentials: |-
    {
      "my-registry.example.org": {
        "username": "my-user",
        "password": "my-token"
      }
    }
```

Then configure the `sync` extension to use that file as a source to authenticate towards registries via the Zot configuration file.

```json
{
  ...
  "extensions": {
    "sync": {
      "credentialsFile": "/secret/credentials"
    }
  }
  ...
}
```

## Configuration recommendations

Depending on your use of Zot, please consider these additional recommendations for your deployment.

### Memory constraints

Zot can take up a lot of memory over time. In the Giant Swarm packaged app you can deploy it with a vertical pod autoscaler (VPA). You can set the resource constraints like shown here:

```yaml
giantswarm:
  verticalPodAutoscaler:
    enabled: true
    maxAllowed:
      # Set this higher than .resources.limits.cpu
      # to stretch limits in case of higher load
      cpu: 750m
      # Set this higher than .resources.limits.memory
      # to stretch limits in case of higher load
      memory: 2048Mi

resources:
  requests:
    # The minimum amount of CPU required for your scenario
    cpu: 300m
    # The minimum amount of memory required for your scenario
    memory: 1024Mi
  limits:
    # The generally maximum amount of CPU required for your scenario
    cpu: 500m
    # The generally maximum amount of CPU required for your scenario
    memory: 1536Mi
```

In case of an out-of-memory kill, VPA controller will dynamically stretch the limits on the deployment based on Prometheus metrics
up to what's set under `.giantswarm.verticalPodAutoscaler.maxAllowed`.

In certain scenarios - in our experience - it's better, more stable to run with a fixed amount of memory. You can
enforce the constraint by setting the memory request and limit to the same value and configuring the
Go garbage collector. Don't forget to disable the VPA in this case!

```yaml
giantswarm:
  verticalPodAutoscaler:
    enabled: false

resources:
  requests:
    cpu: 350m
    memory: 1024Mi
  limits:
    cpu: 500m
    memory: 1024Mi

env:
  - name: GOGC
    value: "50"
  - name: GOMEMLIMIT
    # Set this to about 80% of the memory limit.
    value: 800MiB
```

For more details on this approach, we recommend to read the [Guide to the Go Garbage Collector](https://tip.golang.org/doc/gc-guide).

### Deployment strategies

Some extension, like `search` can create file locks on the data volume mount. With the `RollingUpdate` strategy,
this will cause the new pods failing to stand up. In such scenarios it's recommended to set it to `Recreate`.

```yaml
strategy:
  type: Recreate
```
