---
linkTitle: Key pairs for workload clusters
title: Creating workload cluster key pairs via the Management API
description: We recommend OIDC for authentication to the workload cluster Kubernetes API. However, in some scenarios, X.509 key pairs are a viable alternative. Here we explain a Giant Swarm specific way to create such key pairs via the Management API.
weight: 40
menu:
  main:
    identifier: uiapi-managementapi-keypairs
    parent: uiapi-managementapi
user_questions:
  - How to create workload cluster key pairs via the Management API?
last_review_date: 2021-07-26
owner:
  - https://github.com/orgs/giantswarm/teams/team-biscuit
---

# Creating workload cluster key pairs via the Management API

We recommend OIDC for authentication to the workload cluster Kubernetes API. However, in some scenarios, X.509 key pairs are a viable alternative. Here we explain a method specific to Giant Swarm to create such key pairs via the Management API.

**Note:** The method described here makes use of the [`CertConfig`]({{< relref "/ui-api/management-api/crd/certconfigs.core.giantswarm.io.md" >}}) <abbr title="custom resource definition">CRD</abbr></a> and [cert-operator](https://github.com/giantswarm/cert-operator), which is currently part of every Giant Swarm management cluster. As Giant Swarm is shifting towards using Cluster API controllers, this method will not work once this transition is done. Please consider it a temporary solution.

**Note:** If you want to use the deprecated Giant Swarm Rest API for creating key pairs, please check [`gsctl create kubeconfig`]({{< relref "/ui-api/gsctl/create-kubeconfig.md" >}}) and [`gsctl create keypair`]({{< relref "/ui-api/gsctl/create-keypair.md" >}}).

## Prerequisites

You need:

- Your installation's Management API endpoint (similar to `https://g8s.codename.eu-west-1.aws.gigantic.io`) or base domain (similar to `codename.eu-west-1.aws.gigantic.io`).
- Management API access as an admin.
- Unique ID of the workload cluster to grant access to.
- Name of the organization "owning" that workload cluster.

These tools are also required:

- `kubectl`
- [kubectl gs]({{< relref "/ui-api/kubectl-gs/" >}}), the `kubectl` plug-in for the Giant Swarm Management API.

If you want to use our [example script](#script), you also need:

- [jq](https://stedolan.github.io/jq/)
- The shell commands/utilities `base64`, `cut`, `date`, and `shasum`

## Ensure Management API access

Using our `kubectl` plug-in, you can make sure to be authenticated against the Management API:

```nohighlight
kubectl gs login <URL>
```

Here, `<URL>` can be either

- the Management API endpoint URL or host name
- your installation's web interface URL or host name

See the [`kubectl gs login` reference]({{< relref " /ui-api/kubectl-gs/login.md" >}}) for details.

## Create a CertConfig resource

The [`CertConfig`]({{< relref "/ui-api/management-api/crd/certconfigs.core.giantswarm.io.md" >}}) resource, which is reconciled by cert-operator, allows to request the creation of a key pair. While it is designed for a number of different purposes, e. g. management cluster components, when configured the right way, the key pair is valid for authentication with a particular workload cluster's Kubernetes API.

Here is an example of a `CertConfig` resource manifest. Follow the detailed explanations below.

```yaml
apiVersion: core.giantswarm.io/v1alpha1
kind: CertConfig
metadata:
  name: mycert-20210726
  namespace: default
  labels:
    cert-operator.giantswarm.io/version: 0.1.0
    giantswarm.io/certificate: mycert
    giantswarm.io/cluster: a1b2c
    giantswarm.io/organization: myorg
spec:
  cert:
    allowBareDomains: true
    clusterComponent: mycert
    clusterID: a1b2c
    commonName: mycert.a1b2c.k8s.codename.eu-west-1.aws.gigantic.io
    disableRegeneration: true
    organizations:
      - developers
      - monitoring
    ttl: 1h
  versionBundle:
    version: 0.1.0
```

Here is how you should adapt the example to match your case:

- `.metadata`:
    - `.name`: name for this `CertConfig` resource, unique within the management cluster.
    - `.labels`:
        - `.giantswarm.io/certificate`: an identifier for this key pair that must be unique within the management cluster.
        - `.giantswarm.io/cluster`: ID of the workload cluster to grant access to.
        - `.giantswarm.io/organization`: Name of the organization owning the above workload cluster.
- `.spec`:
    - `.cert`:
        - `.clusterComponent`: set this to the same value as the `giantswarm.io/certificate` label.
        - `.clusterID`: set this to the same value as the `giantswarm.io/cluster` label.
        - `.commonName`: the `CN` that the created certificate will have. Set this to a unique string ending with your workload cluster's Kubernetes API endpoint domain.
        - `.organizations`: defines the RBAC groups set in the created certificate via the `O` attribute. You can include `system:masters` here to create an admin key pair. Check the security notice below.
        - `.ttl`: The duration until the created certificate will expire. `1h` stands for one hour. Check the security notice below.

All other values should be set as given in the example.

**Security notice:** Once issued, Kubernetes provides no way to revoke key pairs. A powerful key pair getting into the wrong hands is a severe risk. Hence we recommend to set expiry durations as short as possible via `.spec.cert.ttl`. Also, please use specific group names via `.spec.cert.organizations` instead of `system:masters`, in order to assign the required permissions via RBAC roles and role bindings, which can be unassigned in case a key pair has been handed to an untrusted party.

Once the `CertConfig` manifest is adapted as required, you can create the according resource by submitting the manifest to the Management API via the `kubectl apply` command.

## Retrieving the key pair

Once the `CertConfig` resource has been created, it should only be a matter of a few seconds until a new secret has been created in the default namespace, with the same name as the `CertConfig` resource. This secret contains three separate attributes we are interested in:

- `.data.crt`: the X.509 certificate
- `.data.key`: the private key
- `.data.ca`: the X.509 certificate of the certificate authority that signed the new certificate and also signed the workload cluster's Kubernetes API server certificate.

All three items are Base64-encoded PEM blocks.

In order to use these items in a `kubectl` config file, all items should be decoded and saved as PEM files first and then applied in `kubectl config set-cluster` (for the CA certificate) and `kubectl config set-credentials` (for the key and certificate).

The example script in the [putting it all together](#script) section shows a way of doing that, as well as the initial `CertConfig` creation in a single step.

## Remove the CertConfig resource

Once the key pair details have been retrieved, there should be no reason to keep the `CertConfig` resource on the management cluster. For best security the resource should be deleted.

Please use `kubectl delete certconfig <name>` to delete the resource.

## Putting it all together {#script}

The following bash script allows to

- Create a `CertConfig` resource with a unique name.
- Retrieve the created key pair and CA certificate.
- Create a new, stand-alone `kubectl` configuration file.

Store the following bash code as `create-keypair.sh` and adapt it to your needs:

```bash
#!/bin/bash

# Installation base domain
BASE_DOMAIN=codename.eu-west-1.aws.gigantic.io

# ID of the workload cluster to grant access to
WORKLOAD_CLUSTER=a1b2c

# Organization owning the cluster above
ORGANIZATION=myorg

# Group name (O) to set in the X.509 certificate
GROUP=developers

# Expiry duration. 1h stands for one hour.
TTL=1h

### Config end

# Management API endpoint
URL=https://g8s.$BASE_DOMAIN


set -e
set -u
set -o pipefail


# Check prerequisites
which jq >> /dev/null || (echo "ERROR: Please install jq" && exit 1)
which kubectl >> /dev/null || (echo "ERROR: Please install kubectl" && exit 1)
which kubectl-gs >> /dev/null || (echo "ERROR: Please install kubectl-gs via 'kubectl krew install gs'" && exit 1)

if [ "$ORGANIZATION" = "" ]; then
    echo "ERROR: Please set the \$ORGANIZATION variable." && exit 1
fi

if [ "$WORKLOAD_CLUSTER" = "" ]; then
    echo "ERROR: Please set the \$WORKLOAD_CLUSTER variable." && exit 1
fi

if [ "$GROUP" = "" ]; then
    echo "ERROR: Please set the \$GROUP variable." && exit 1
fi

if [ "$TTL" = "" ]; then
    echo "ERROR: Please set the \$TTL variable." && exit 1
fi
# Check prerequisites end

# Authenticate against the management API, set current kubectl context
kubectl gs login $URL

# Create name for the CertConfig and kubeconfig
DATE=$(date)
UNIQUE_ID=$(echo "$ORGANIZATION $WORKLOAD_CLUSTER $DATE" | shasum | cut -c 1-12)
NAME="$WORKLOAD_CLUSTER-$UNIQUE_ID"

# Create CN
CN="$UNIQUE_ID.$WORKLOAD_CLUSTER.k8s.$BASE_DOMAIN"

kubectl apply -f - <<EOF
apiVersion: core.giantswarm.io/v1alpha1
kind: CertConfig
metadata:
  labels:
    cert-operator.giantswarm.io/version: 0.1.0
    giantswarm.io/certificate: $UNIQUE_ID
    giantswarm.io/cluster: $WORKLOAD_CLUSTER
    giantswarm.io/organization: $ORGANIZATION
  name: $NAME
  namespace: default
spec:
  cert:
    allowBareDomains: true
    clusterComponent: $UNIQUE_ID
    clusterID: $WORKLOAD_CLUSTER
    commonName: $CN
    disableRegeneration: true
    organizations:
    - $GROUP
    ttl: $TTL
  versionBundle:
    version: 0.1.0
EOF

# Wait a bit
sleep 3

echo ""

JSON=$(kubectl get secret $NAME -o json)
echo $JSON | jq -r .data.crt | base64 -D > $NAME-crt.pem
echo $JSON | jq -r .data.key | base64 -D > $NAME-key.pem
echo $JSON | jq -r .data.ca | base64 -D > $NAME-ca.pem

echo "Creating new kubeconfig file $NAME.yaml"

touch ./$NAME.yaml

kubectl --kubeconfig=./$NAME.yaml config set-cluster giantswarm-$WORKLOAD_CLUSTER \
    --server https://api.$WORKLOAD_CLUSTER.k8s.$BASE_DOMAIN \
    --certificate-authority $NAME-ca.pem \
    --embed-certs=true

kubectl --kubeconfig=./$NAME.yaml config set-credentials $UNIQUE_ID \
    --certificate-authority $NAME-ca.pem \
    --client-key $NAME-key.pem \
    --client-certificate $NAME-crt.pem \
    --embed-certs=true

kubectl --kubeconfig=./$NAME.yaml config set-context $NAME \
    --cluster=giantswarm-$WORKLOAD_CLUSTER \
    --user=$UNIQUE_ID

kubectl --kubeconfig=./$NAME.yaml config use-context $NAME

# Clean up
kubectl delete certconfig $NAME
rm $NAME-crt.pem $NAME-key.pem $NAME-ca.pem
```
