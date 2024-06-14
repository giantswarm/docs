---
title: Create a workload cluster and install applications
linkTitle: Provision your first workload cluster
description: Experience the steps to configure and provision your first workload cluster using the platform API.
weight: 40
last_review_date: 2024-06-13
menu:
  principal:
    parent: getting-started
    identifier: getting-started-provision-cluster
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I configure and provision my first workload cluster?
  - What do I need to do to configure and provision my first workload cluster?
---

Once you have access to the platform API, you can create a workload cluster easily.

gitops
kgs
happa

```
DOWN -> Move this to specific page
## Step 2: Choose a workload cluster name

First, please choose a name for the new workload cluster. We recommend you choose a naming scheme suiting your organization, and then stick to it.

- The maximum cluster name length is 20 characters.
- Letters, digits and dashes are allowed. Dashes are not possible at beginning or end.
- For example, `dev-eu-central-1-a`, `dev-a`, `prod-b`, `ecommerce-dev-eu`, `prod-us` or `staging01` are all valid names.
- The cluster name will be part of domain names such as `api.<cluster name>.<base domain>` (for instance: `api.mycluster.eu-west-1.aws.gigantic.io` or `ingress.mycluster.mycompany.com`). The _base domain_ is defined by the management cluster. Since DNS records can normally be resolved publically by anyone, you should avoid encoding sensitive information into the cluster name (`mycluster` in our examples).
- Clusters can't be renamed after creation.
- Keep cluster names unique across your whole company. This is why:

    - Within one management cluster, all workload cluster names must be unique, even across namespaces. This is so that tooling and operators can look up workload clusters by their unique name without the chance of confusion.
    - Multiple management clusters can share the same base domain (see examples above), so workload cluster names should be unique across your company since their domains would otherwise clash.
    - Using identical workload cluster names creates problems and risk. Imagine asking for support, or trying to resolve an incident, and Giant Swarm's or your team members confuse two clusters of the same name. Hence, cluster names should be unique, easily spellable and pronounceable by humans – for example during incident calls and in chat – and follow a somewhat consistent naming scheme.
- We strongly recommend specifying a cluster name explicitly using the `--name` parameter, as in the below instructions. If you really want a randomly-generated name, you can instead use `--generate-name`.

## Step 3: Template and create the workload cluster

You will now create resources with `kubectl gs`. In particular, this tutorial uses the `kubectl gs template` command to create valid YAML for each resource. The templating commands do not immediately create the cluster – the resulting YAML manifest must be applied to the management cluster API or committed to the GitOps repository in order to create the cluster. Alternatively, the Web UI provides a visual way to create clusters.

You can template a cluster ([command reference]({{< relref "/vintage/use-the-api/kubectl-gs/template-cluster" >}})) as follows:

{{< tabs >}}
{{< tab id="cluster-vintage-azure" for-impl="vintage_azure" >}}

[Choose a release version here](https://docs.giantswarm.io/changes/workload-cluster-releases-for-azure), or use `kubectl gs get releases`, and fill it into this example command:

```sh
kubectl gs template cluster \
  --provider azure \
  --name mycluster \
  --organization testing \
  --release 19.0.1 `# please fill in your desired release version` \
  > cluster.yaml
```

For backward compatibility, vintage cluster templating does not require the `--name` parameter. If no name is specified, a random one like `zekfaewnxh` will be generated. The `--name` parameter becomes required with CAPI clusters, but you can also use `--generate-name` if a random name is really desired.

{{< /tab >}}
{{< tab id="cluster-vintage-aws" for-impl="vintage_aws">}}

[Choose a release version here](https://docs.giantswarm.io/changes/workload-cluster-releases-for-aws), or use `kubectl gs get releases`, and fill it into this example command:

```sh
kubectl gs template cluster \
  --provider aws \
  --name mycluster \
  --organization testing \
  --release 19.0.0 `# please fill in your desired release version` \
  > cluster.yaml
```

For backward compatibility, vintage cluster templating does not require the `--name` parameter. If no name is specified, a random one like `zekfaewnxh` will be generated. The `--name` parameter becomes required with CAPI clusters, but you can also use `--generate-name` if a random name is really desired.

{{< /tab >}}
{{< tab id="cluster-capa-ec2" for-impl="capa_ec2">}}

This will automatically use the latest release of the relevant Helm chart [cluster-aws](https://github.com/giantswarm/cluster-aws/blob/master/CHANGELOG.md):

```sh
kubectl gs template cluster \
  --provider capa \
  --name mycluster \
  --organization testing \
  > cluster.yaml
```

You can select the AWS account by specifying the `aws-cluster-role-identity-name` argument when templating the cluster.
The name passed to `aws-cluster-role-identity-name` must match the name of [an existing `AWSClusterRoleIdentity`](https://docs.giantswarm.io/getting-started/cloud-provider-accounts/cluster-api/aws/#configure-the-awsclusterroleidentity).

```sh
kubectl gs template cluster \
  --provider capa \
  --name mycluster \
  --organization testing \
  --aws-cluster-role-identity-name=dev-account-role-identity
  > cluster.yaml
```

If no `aws-cluster-role-identity-name` is passed, then we assume a `AWSClusterRoleIdentity` called `default` exists and will be used.

{{< /tab >}}
{{< tab id="cluster-capa-eks" for-impl="capa_eks">}}

This will automatically use the latest release of the relevant Helm chart [cluster-eks](https://github.com/giantswarm/cluster-eks/blob/master/CHANGELOG.md):

```sh
kubectl gs template cluster \
  --provider eks \
  --name mycluster \
  --organization testing \
  > cluster.yaml
```

You can select the AWS account by specifying the `aws-cluster-role-identity-name` argument when templating the cluster.
The name passed to `aws-cluster-role-identity-name` must match the name of [an existing `AWSClusterRoleIdentity`](https://docs.giantswarm.io/getting-started/cloud-provider-accounts/cluster-api/aws/#configure-the-awsclusterroleidentity).

```sh
kubectl gs template cluster \
  --provider capa \
  --name mycluster \
  --organization testing \
  --aws-cluster-role-identity-name=dev-account-role-identity
  > cluster.yaml
```

If no `aws-cluster-role-identity-name` is passed, then we assume a `AWSClusterRoleIdentity` called `default` exists and will be used.

{{< /tab >}}
{{< tab id="cluster-capz-azure-vms" for-impl="capz_vms">}}

This will automatically use the latest release of the relevant Helm chart [cluster-azure](https://github.com/giantswarm/cluster-azure/blob/master/CHANGELOG.md):

```sh
kubectl gs template cluster \
  --provider capz \
  --name mycluster \
  --organization testing \
  --region westeurope \
  --azure-subscription-id 00000000-0000-0000-0000-000000000000 `# fill in your subscription ID` \
  > cluster.yaml
```

{{< /tab >}}
{{< tab id="cluster-capvcd" for-impl="capvcd">}}

The VMware Cloud Director provider is not yet supported by `kubectl gs template cluster` but you can use the [example manifest](https://github.com/giantswarm/cluster-cloud-director/tree/main/examples) provided in the cluster chart's repo.

Make sure to replace the relevant fields to fit your own VCD environment.

This will install the relevant Helm chart [cluster-cloud-director](https://github.com/giantswarm/cluster-cloud-director).

{{< /tab >}}
{{< tab id="cluster-capv" for-impl="capv">}}

This will automatically use the latest release of the relevant Helm chart [cluster-vsphere](https://github.com/giantswarm/cluster-vsphere/blob/master/CHANGELOG.md):

```sh
kubectl gs template cluster \
  --provider vsphere \
  --name mycluster \
  --organization testing \
  --vsphere-service-load-balancer-cidr <cidr_ip>/<netmask> \
  --kubernetes-version=1.24.11
  > cluster.yaml
```

{{< /tab >}}
{{< /tabs >}}

This will create a `cluster.yaml` file containing all the Custom Resources (CRs) necessary to create the cluster.

For the [Cluster API (CAPI)]({{< relref "/vintage/platform-overview/architecture" >}}) product family, you will notice that clusters are templated exactly like managed apps (i.e. as `App` resource), with `kubectl-gs` filling certain default values into the configuration. This is different from vintage products.

In the vintage product family, no worker node pool is created by default, so you should attach one:

{{< tabs >}}
{{< tab id="nodepool-vintage-azure" for-impl="vintage_azure">}}

```sh
kubectl gs template nodepool \
  --provider azure \
  --cluster-name "<please fill in the cluster name from cluster.yaml>" \
  --description "Worker node pool for workload cluster" \
  --organization testing \
  --release 19.0.1 `# please fill in your desired release version` \
  > nodepool.yaml
```

This will create a `nodepool.yaml` file with all the CRs needed for attaching a node pool to the cluster created in the previous step.

{{< /tab >}}
{{< tab id="nodepool-capi" for-impl="capi_any">}}

This is not needed for CAPI. The `nodePools` value in the cluster app has a default. For example, see [nodePools configuration for cluster-aws](https://github.com/giantswarm/cluster-aws/blob/master/helm/cluster-aws/README.md#node-pools) when using the CAPA-based product (AWS cloud).

{{< /tab >}}
{{< /tabs >}}

Templating these and other resources as YAML files is reasonable if you prefer deployments using GitOps (YAML manifests committed and deployed from a Git control repository) or want to develop/deploy using scripts or the command line, without manual steps in the web interface. We recommend running `kubectl gs template [...] --help` and the online [reference]({{< relref "/vintage/use-the-api/kubectl-gs" >}}) to see available parameters. For clusters and node pools, you probably want to choose a different instance size (varies in CPU, memory, pricing), maximum number of nodes, cloud provider region, or IP CIDRs. Instead of the kubectl-gs command line, you can also manually edit the YAML file with the help of our documentation for cluster configuration options (example: [configuration options for cluster-aws](https://github.com/giantswarm/cluster-aws/blob/master/helm/cluster-aws/README.md)).

To _actually_ create the resources – the workload cluster and (only for vintage product family) worker node pool – you need to apply the manifests. Ensure you are still pointing to the management cluster's kubectl context and run:

```sh
kubectl apply -f cluster.yaml

# Only for vintage product family:
kubectl apply -f nodepool.yaml
```

### Deleting the workload cluster {#deleting-workload-cluster}

Deletion works in the same way: run `kubectl delete -f FILENAME.yaml` and the operators in the management cluster will delete the resources in a few minutes. Please do not directly delete the CAPI custom resources (such as `Cluster`, `AWSCluster` or `MachineDeployment`) since this may leave resources behind or even lead to inadvertently recreating the cluster once the `App` is reconciled again. Deletion should be done exactly like the creation, using the original manifests. For the CAPI product family, our example output file `cluster.yaml` contains 2 `App` and 2 `ConfigMap` manifests. If you no longer have the manifests at hand, delete the following:

- `App/<cluster>`
- `ConfigMap/<cluster>-userconfig`

If you would like to protect your clusters from accidental deletion, take a look at our [deletion prevention mechanism]({{< relref "/vintage/advanced/app-platform/deletion-prevention" >}}).

### Private workload clusters

By default, the created Kubernetes cluster API endpoint is public. See [Private clusters]({{< relref "/vintage/advanced/cluster-management/private-clusters" >}}) if you want to limit networking to/from the cluster.

## Step 4: Watch the status of workload clusters

In the Web UI, click on the cluster's name to see its details. The workload cluster's name is shown on the top-left (in the screenshot: `o8r3r`).

![Adding a nodepool](nodepool.png)

For the vintage product family, if you did not yet attach a node pool to the WC as shown above, you can now add one by clicking the "Add node pool" button.

Using the command line, you can also watch the creation and status of the workload cluster:

{{< tabs >}}
{{< tab id="status-vintage" for-impl="vintage_any">}}

```sh
kubectl gs get clusters -A

kubectl gs get nodepools -A
```

{{< /tab >}}
{{< tab id="status-capi" for-impl="capi_any">}}

Either use kubectl-gs:

```sh
kubectl gs get clusters -A
```

Or use other kubectl tooling to display the relations and status of the CAPI manifests:

```sh
kubectl describe clusters.cluster.x-k8s.io -n org-testing name-of-workload-cluster

# Using CAPI's clusterctl tool (https://cluster-api.sigs.k8s.io/clusterctl/overview.html)
clusterctl describe cluster -n org-testing name-of-workload-cluster --show-conditions all

# Using kubectl-tree plugin (https://github.com/ahmetb/kubectl-tree)
kubectl krew install tree
kubectl tree clusters.cluster.x-k8s.io -n org-testing name-of-workload-cluster
```

Note how our example commands use the fully-qualified CRD name `clusters.cluster.x-k8s.io`. The shorthands `cluster` or `clusters` also work as long as there are no CRDs with a conflicting name installed.

{{< /tab >}}
{{< /tabs >}}

## Step 5: Log in to the workload cluster

Using the Web UI, click on the workload cluster and then the _Client certificates_ tab. Copy the command suggested at the _Create a client certificate_ step. As value for `--certificate-group`, you can use `system:masters`. More information about group certificates can be found in [Kubernetes RBAC: Default roles and role bindings](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings).

![Creating a client certificate](client-certificates.png)

In our example, therefore, we will run

```sh
kubectl gs login gs-wombat \
  --workload-cluster o8r3r \
  --organization giantswarm \
  --certificate-group system:masters \
  --certificate-ttl 3h
```

At this point, you are logged in to the workload cluster, with full access. Try `kubectl get pod -A`, for example, to take a look into the cluster.

Some of the custom resource definitions (CRDs) available in the management cluster are not available in the WC because those concepts do not exist in workload clusters. For instance, if we try to get the organizations, we get an error, because they are a concept that makes sense in the MC but not in the WC:

```text
$ kubectl get orgs
error: the server doesn't have a resource type "organizations"
```

The WCs are where the "actual" work happens, i.e. where Giant Swarm-supported managed apps and your business applications are deployed. The easiest way to check whether an application is running is `kubectl get pods -A | grep APPLICATION_NAME`, for instance: `kubectl get pods -A | grep kong`.

## Step 6: Template and deploy managed apps

In addition to workload clusters, you can also template applications. Apps belong to catalogs. While you can define your own catalogs, we already provide two: `giantswarm` (_Giant Swarm Catalog_) contains applications that we know how to manage; `giantswarm-playground` (_Playground_) contains applications that we have integrated but are not managed by us. Other catalogs such as the _Giant Swarm Cluster Catalog_ are used for templating of clusters (which you did above).

You can easily surf catalogs from the _Apps_ section in the Web UI:

![App Catalog](apps.png)

Let's assume you want to install the Kong app. By clicking on it, we can see its details:

![The Kong application](kong-app.png)

With the web interface, you can configure and deploy the app by clicking _Install in this cluster_. In this tutorial, we show how to template the app into a YAML manifest. The command can be seen at the bottom of the Web UI app overview, for instance:

```sh
kubectl gs template app \
  --catalog giantswarm \
  --name kong-app \
  --target-namespace test-namespace \
  --cluster-name o8r3r \
  --version 3.3.0 \
  > kong-app.yaml
```

This writes the `App` CR to the file `kong-app.yaml`.

To deploy the app, deploy it, again using the management cluster context:

```sh
kubectl apply -f kong-app.yaml
```

Notice that by running `kubectl gs template app --help` you can list all the options that can be useful when templating an app. For instance, the `--user-configmap` and `--user-secret` options allow for adding YAML files containing useful configurations or secrets.

Here is an example which disables the config flag `proxy.enabled` for Kong:

```sh
cat > kong-config.yaml <<EOF
proxy:
  enabled: false
EOF

kubectl gs template app \
  --catalog giantswarm \
  --name kong-app \
  --target-namespace test-namespace \
  --cluster-name o8r3r \
  --version 3.3.0 \
  --user-configmap kong-config.yaml \
  > kong-app.yaml
```

In general, whenever templating and/or installing an application, please read its documentation page on the Web UI to be sure you are configuring everything correctly.

## Step 7: Updates of workload clusters and managed apps

### Updating an application

Updating an application can either be done in the Web UI, or by using `kubectl gs`.

Beware: before performing any updates, verify that there are no breaking changes! If there are breaking changes, prepare for the upgrade accordingly. We document breaking and other changes in the repository's `CHANGELOG.md` (example: [changelog for Kong app](https://github.com/giantswarm/kong-app/blob/main/CHANGELOG.md)). Mind that the upstream project can also introduce major changes, so looking at their changelog is also reasonable.

You can update (or roll back) an application by running the following command in the management cluster:

```sh
kubectl gs update app \
  --name APP_NAME \
  --namespace NAMESPACE \
  --version NEW_VERSION
```

For instance:

```sh
kubectl gs update app \
  --name kong \
  --namespace test-namespace \
  --version 3.3.0
```

### Updating a cluster

Cluster updates can be easily performed straight away or scheduled for a specific moment in time. The latter is a feature in the vintage product family that many customers find very useful because it allows them to schedule updates without the need to physically be there to "press the button".

More information on updating a cluster can be found [in the kubectl-gs reference]({{< relref "/vintage/use-the-api/kubectl-gs/update-cluster" >}}).
