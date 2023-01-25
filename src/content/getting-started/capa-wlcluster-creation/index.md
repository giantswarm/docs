---
linkTitle: Create a workload cluster in CAPA
title: Create a cluster using cluster API in AWS (CAPA)
description: This guide will walk you through all necessary steps to create a workload cluster with cluster API in AWS environments.
weight: 100
menu:
  main:
    parent: getting-started
user_questions:
  - How can I create a workload cluster in a CAPA environment?
  - How can I get the capa cluster template using kubectl gs template cluster?
aliases:
  - /guides/create-wlcluster-capa-template/
owner:
  - https://github.com/orgs/giantswarm/teams/team-hydra
last_review_date: 2022-10-07
---

In order to create a cluster in an installation using the new cluster API in AWS environment you can follow these simple steps:

### Create yaml files

  - Create a template for a yaml file using `kubectl gs template cluster` command. An example of the command would be:
  ```nohighlight
  $ kubectl gs template cluster --provider capa --organization YOUR_ORG > cluster.yaml
  ```
  You can check all the available parameters in the [command reference]({{< relref "/use-the-api/kubectl-gs/template-cluster" >}})

  - This command will return several objects that you need to create in your management cluster to create your cluster. You can now edit the file to include your preferred options. Some interesting things you can customize here are:
    - instance type: default value m5.xlarge
    - size of the node and master node pool
    - availability zone usage

  ``` yaml 
  ---
apiVersion: v1
data:
  values: |
    aws: {}
    bastion: {}
    clusterName: brhf3
    controlPlane:
      replicas: 3
    machinePools:
      machine-pool0:
        availabilityZones:
        - eu-central-1a
        instanceType: m5.xlarge
        maxSize: 10
        minSize: 3
        rootVolumeSizeGB: 300
    network:
      availabilityZoneUsageLimit: 3
    organization: YOUR_ORG
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: brhf3
  name: brhf3-userconfig
  namespace: org-YOUR_ORG
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: brhf3
  namespace: org-YOUR_ORG
spec:
  catalog: cluster
  config:
    configMap:
      name: ""
      namespace: ""
    secret:
      name: ""
      namespace: ""
  kubeConfig:
    context:
      name: ""
    inCluster: true
    secret:
      name: ""
      namespace: ""
  name: cluster-aws
  namespace: org-YOUR_ORG
  userConfig:
    configMap:
      name: brhf3-userconfig
      namespace: org-YOUR_ORG
  version: 0.9.2
---
apiVersion: v1
data:
  values: |
    clusterName: brhf3
    organization: YOUR_ORG
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: brhf3
  name: brhf3-default-apps-userconfig
  namespace: org-YOUR_ORG
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: brhf3-default-apps
  namespace: org-YOUR_ORG
spec:
  catalog: cluster
  config:
    configMap:
      name: ""
      namespace: ""
    secret:
      name: ""
      namespace: ""
  kubeConfig:
    context:
      name: ""
    inCluster: true
    secret:
      name: ""
      namespace: ""
  name: default-apps-aws
  namespace: org-YOUR_ORG
  userConfig:
    configMap:
      name: brhf3-default-apps-userconfig
      namespace: org-YOUR_ORG
  version: 0.5.4

  ``` 

## Creating the cluster

Applying this files to the management cluster is enough to create the cluster. When this happens cluster operator takes control and creates the necessary resources for the new workload cluster.
```  
  kubectl apply -f cluster.yaml
```
You can check that the cluster has been properly created using `kubectl get clusters` in the management cluster.
```
kubectl get clusters -n org-YOUR_ORG 
NAME    PHASE         AGE     VERSION
brhf3   Provisioned   10m
``` 
