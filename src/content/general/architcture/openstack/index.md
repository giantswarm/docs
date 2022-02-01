---
linkTitle: Openstack
title: The Giant Swarm Openstack architecture
description: Architecture overview showing how Giant Swarm is set up within a customer data center on Open stack deployment, using cluster API.
weight: 30
menu:
  main:
    parent: general-architecture
last_review_date: 2022-02-02
user_questions:
  - Do you run Openstack?
aliases:
  - /basics/openstack-architecture/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
---


# MC bootstraping

We use a helm chart to store all the CAPI resources needed to bootstrap the MC.

1. Pull secrets from Lastpass 
  - Default values.yaml for the helm chart
  - Open rc file (needed by CAPI controllers to know where Openstack API endpoint it is and other metadata needed)
  - taylorbot token
  - secrets (OIDC settings and others)

2. Installation branch creation (we need to create a installation entry for every MC we create)

3. Setup kind

4. Install the capo controllers in the kind cluster

5. From the rc file pulled from Lastpass, create a secret with the cloudbase configuration needed in Openstack to connect with the API endpoint.

6. Create the cloudbase secret in the kind cluster, install the CAPO helm chart with the cluster manifests and wait till kubeconfig is ready.

7. Save MC kubeconfig in last pass for this installation

8. Deploy CNI to the MC cluster (calico from upstream)

9. Get network and subnet IDs, create values yaml for the [cloud provider openstack app](https://github.com/giantswarm/cloud-provider-openstack-app) and install in the cluster. By now the app install cloud controller manager for Openstack and CSI cinder.

10. Install cert manager app with default values

11. Install CAPO controllers in the MC

12. Move MC cluster resources from the kind cluster to the MC cluster (running in the same cluster)

13. Create `giantswarm` and `ardgocd` namespace in the MC

14. 

# The Giant Swarm Openstack Architecture

Giant Swarm's architecture is split into two logical parts. One describes the management cluster and the other describes one or more workload clusters. We prefer running on bare metal machines, but can also work with virtualized infrastructure (e.g. VMWare) in cases where nested virtualization is possible.


## Giant Swarm on-premises management cluster


## Giant Swarm on-premises workload cluster(s)

## Service architecture

## Further Reading

* [Giant Swarm VPN and secure cluster access]({{< relref "/security/cluster-access" >}})
