---
title: Create a workload cluster and install applications
linkTitle: Provision your first workload cluster
description: Experience the steps to configure and provision your first workload cluster using the platform API.
weight: 40
last_review_date: 2024-08-21
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

Once you have access to the platform API, the most natural next step is to create a workload cluster to understand how the platform works. This guide will describe step-by-step how to do it.

Although our recommendable approach to manage your platform is to use [GitOps](https://www.giantswarm.io/blog/what-is-gitops) here we describe the process using the CLI to make it easier to understand the concepts. Translating these steps to GitOps is straightforward and you can follow our dedicated tutorial on [how to manage your workload clusters using GitOps]({{< relref "/vintage/advanced/gitops" >}}).

## Requirements

In case you haven't installed the `kubectl-gs` CLI plugin yet, please follow the [installation instructions]({{< relref "/getting-started/access-to-platform-api#Requirements" >}}).

## Step 1: Template the workload cluster

You will now create resources with `kubectl gs`. In particular, this tutorial uses the `kubectl gs template` command to create valid YAML for each resource. The template commands don't immediately create the cluster–the resulting YAML manifest must be applied to the management cluster API or committed to the GitOps repository in order to create the cluster.

You can template a cluster ([command reference]({{< relref "/vintage/use-the-api/kubectl-gs/template-cluster" >}})) as follows:

{{< tabs >}}
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

The name passed to `aws-cluster-role-identity-name` must match the name of [an existing `AWSClusterRoleIdentity`]({{< relref "getting-started/prepare-your-provider-account/aws/#configure-cluster-role-identity" >}}).

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

The name passed to `aws-cluster-role-identity-name` must match the name of [an existing `AWSClusterRoleIdentity`]({{< relref "getting-started/prepare-your-provider-account/aws/#configure-cluster-role-identity" >}}).

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

The VMware Cloud Director provider isn't yet supported by `kubectl gs template cluster` but you can use the [example manifest](https://github.com/giantswarm/cluster-cloud-director/tree/main/examples) provided in the cluster chart's repository.

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

You will notice that clusters are templated exactly like [managed apps]({{< relref "vintage/use-the-api/management-api/crd/apps.application.giantswarm.io/" >}}) (as `App` resource), with `kubectl-gs` filling certain default values into the configuration. Using an `App` custom resource for cluster templating allow us to keep consistency and simplicity using the platform API.

In Cluster API the node pools are defined inside the `App` chart. For example, see [nodePools configuration for cluster-aws](https://github.com/giantswarm/cluster-aws/blob/master/helm/cluster-aws/README.md#node-pools) when using the CAPA-based product.

__Note__: Templating these and other resources as YAML files is reasonable when you prefer deployments using GitOps (YAML manifests committed and deployed from a Git control repository). We recommend running `kubectl gs template --help` and the online [reference]({{< relref "/vintage/use-the-api/kubectl-gs" >}}) to see available parameters. For clusters and node pools, you probably want to choose a different instance size (varies in CPU, memory, pricing), maximum number of nodes, cloud provider region, or IP CIDRs. Instead of the kubectl-gs command line, you can also manually edit the YAML file with the help of our documentation for cluster configuration options (example: [configuration options for cluster-aws](https://github.com/giantswarm/cluster-aws/blob/master/helm/cluster-aws/README.md)).

To _actually_ create the resources you need to apply the manifests. Ensure you are still pointing to the management cluster's kubectl context and run:

```sh
kubectl apply -f cluster.yaml
```

## Step 2: Watch the status of the workload cluster

You can watch the creation and status of the workload cluster running:

```sh
kubectl gs get clusters -A
```

Additionally, you may want to display the relations and status of the Cluster API manifests using upstream tooling:

```sh
kubectl describe clusters.cluster.x-k8s.io -n org-testing name-of-workload-cluster

# Using Cluster API's clusterctl tool (https://cluster-api.sigs.k8s.io/clusterctl/overview.html)
clusterctl describe cluster -n org-testing name-of-workload-cluster --show-conditions all

# Using kubectl-tree plugin (https://github.com/ahmetb/kubectl-tree)
kubectl krew install tree
kubectl tree clusters.cluster.x-k8s.io -n org-testing name-of-workload-cluster
```

__Warning__: Note how our example commands use the fully qualified Custom Resource Definition (CRD) name `clusters.cluster.x-k8s.io`. The shorthands `cluster` or `clusters` also work, but within the management cluster there are other cluster custom resources like `clusters.rds.aws.upbound.io` that could cause confusion. This is the fact that Kubernetes does not restrict CRDs to share the same shortname.

## Step 3: Log in to the workload cluster

Use the login command to generate a certificate valid for the workload cluster. As value for `--certificate-group`, you can use `system:masters`. More information about group certificates can be found in [Kubernetes RBAC: Default roles and role bindings](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings).


```sh
kubectl gs login gs-wombat \
  --workload-cluster o8r3r \
  --organization giantswarm \
  --certificate-group system:masters \
  --certificate-ttl 3h
```

At this point, you are logged in to the workload cluster, with full access. Try `kubectl get pod -A`, for example, to take a look into the cluster.

Some of the [custom resource definitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) available in the management cluster aren't available in the workload cluster because those concepts don't exist in workload clusters. For instance, if we try to get the organizations, we get an error, because they're a concept that makes sense in the MC but not in the WC:

```text
$ kubectl get orgs
error: the server doesn't have a resource type "organizations"
```

The workload clusters are where the "actual" work happens, where Giant Swarm-supported managed apps and your business applications are deployed. The easiest way to check whether an application is running is `kubectl get pods -A | grep APPLICATION_NAME`, for instance: `kubectl get pods -A | grep kong`.

## Step 4: Deleting the workload cluster {#deleting-workload-cluster}

Deletion works similarly: run `kubectl delete -f cluster.yaml`, `cluster.yaml` being the name selected for the output file when creating the cluster, and the operators in the management cluster will delete the resources in a few minutes. Please don't directly delete the Cluster API custom resources (such as `Cluster`, `AWSCluster` or `MachineDeployment`) since this may leave resources behind or even lead to inadvertently recreating the cluster once the `App` is reconciled again. Deletion should be done exactly like the creation, using the original manifests. For the Cluster API product family, our example output file `cluster.yaml` contains 2 `App` and 2 `ConfigMap` manifests. If you no longer have the manifests at hand, delete the following:

- `App/<cluster>`
- `ConfigMap/<cluster>-userconfig`

If you would like to protect your clusters from accidental deletion, take a look at our [deletion prevention mechanism]({{< relref "/vintage/advanced/app-platform/deletion-prevention" >}}).

## Next step

Since you know how to provision a workload cluster, now you can deploy [your first app following these steps]({{< relref "/getting-started/install-an-application" >}}).
