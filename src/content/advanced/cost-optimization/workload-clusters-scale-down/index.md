---
linkTitle: Workload-clusters-scale-down
title: Workload Clusters Scale Down
description: In order to save costs over the weekends or stale periods some entities would like to scale down the clusters to 0 nodes, this guide describes such process for Giant Swarm clusters.
weight: 100
menu:
  main:
    parent: cost-optimization
last_review_date: 2021-11-15
user_questions:
- How can i scale down cluster nodes to 0?
- How can I silence alerts from the clusters?
aliases:
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

# Periodically scaling down workload clusters to 0 worker nodes

For limiting costs of workload clusters that are used periodically or have stale periods of time, there are use cases to scale down the worker nodes to zero. Such scenarios apply often th development clusters that are not being used over the weekends and there is limited possibility to scale down workloads completely.
Moreover in order to maximize fully the cost optimization, there should be no workers running at all.  

However as Giant Swarm is also running several components on the workload clusters that are being monitored, this can result in our Giant Swarm Oncall to be paged due to unavailability of such services.
The following tutorial describes a way to silence periodically alerts from specified clusters and scale down the worker nodes accordingly.

## Silences

Internally Giant Swarm introduced a concept of Silence Custom Resources. They are utilized to silence either particular alerts or whole clusters in case of known persistent issues or alerts that can be omitted for a while.
The resource consists of constraints and filters which define the silencing rules on defined alerts and clusters. Those are placed in a private github repository and are synced with every Management Cluster via [silence-operator](https://github.com/giantswarm/silence-operator).

You can see the example of such Custom Resource below:

```yaml
apiVersion: monitoring.giantswarm.io/v1alpha1
kind: Silence
metadata:
  name: INSTALLATION-CLUSTER-ID-silence-cluster
spec:
  targetTags:
  - name: installation
    value: YOUR_INSTALLATION_NAME
  matchers:
  - name: cluster_id
    value: CLUSTER_ID
    isRegex: false
```

Such Custom Resource if created manually, would be overwritten by the operator at the syncing time, meaning that there would be no option too set such silence manually.
In order to enable the manual configurability, we have introduced an annotation in order to instruct silence-operator to omit such resources.

The manually created Silence directly on Management Cluster looks then as following:

```yaml
apiVersion: monitoring.giantswarm.io/v1alpha1
kind: Silence
metadata:
  name: INSTALLATION-CLUSTER-ID-silence-cluster
  annotations:
    'giantswarm.io/keep': 'true'
spec:
  targetTags:
  - name: installation
    value: YOUR_INSTALLATION_NAME
  matchers:
  - name: cluster_id
    value: CLUSTER_ID
    isRegex: false
```

Adding the annotation `'giantswarm.io/keep': 'true'` makes it possible for customers to also set particular silences.

## Scaling and Silencing Cron Jobs

Taking into the consideration the use case of scaling down and silencing clusters for the weekends we have tested a following setup with Cron Jobs that can be scheduled to perform the actions.

### Permissions setup for the Cron Job

The first step to apply any Cron Jobs that can create silences and scale down the clusters is to define a set of permissions that are assigned to the given tasks.
Following [Cron Job RBAC example](cronjob-silence-rbac.yaml) provides required setup for the actual tasks to run in the future. Please adjust the Organization parameter accoringly to your Workload Cluster resources location.

### Scale down and silence clusters

After RBAC is applied successfully it is possible to create the Cron Jobs that will scale down and silence the clusters.  
Please consider using the syntax for naming and namespaces as listed in the following [example](cronjob-scale-down-silence.yaml):

```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: silences-customer-create-{CLUSTER-ID}
  namespace: {YOUR_ORGANIZATION}
  labels:
    app: silence-customer
spec:
  schedule: "47 16 * * 5" #Timezone - UTC by default - Fridays, 16;47 UTC
  successfulJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        metadata:
          labels:
            app: silences-customer
        spec:
          serviceAccountName: silences-customer-rbac
          containers:
          - name: silences-customer-create-{CLUSTER-ID}
            image: quay.io/giantswarm/k8s-initiator
            imagePullPolicy: IfNotPresent
            command:
            - /bin/sh
            - -c
            - |
              cat <<EOF | kubectl apply -f -
              apiVersion: monitoring.giantswarm.io/v1alpha1
              kind: Silence
              metadata:
                name: {INSTALLATION}-{CLUSTER-ID}-silence-cluster
                annotations:
                  'giantswarm.io/keep': 'true'
              spec:
                targetTags:
                - name: installation
                  value: {YOUR_INSTALLATION_NAME}
                matchers:
                - name: cluster_id
                  value: {CLUSTER_ID}
                  isRegex: false
              EOF

              # patch annotations of min and max values for autoscaling to 0
              kubectl patch MachinePool -n {YOUR_ORGANIZATION} {CLUSTER_ID} --type merge -p '{"metadata" : {"annotations": {"cluster.k8s.io/cluster-api-autoscaler-node-group-min-size": "0"}}}'
              kubectl patch MachinePool -n {YOUR_ORGANIZATION} {CLUSTER_ID} --type merge -p '{"metadata" : {"annotations": {"cluster.k8s.io/cluster-api-autoscaler-node-group-max-size": "0"}}}'

          restartPolicy: Never
```

This Cron Job will run accordingly to the specified schedule e.g. every Friday att 16:47 UTC. It will first create a silence for the whole cluster, such that the GS oncall is not paged by any incidents happening on the clusters.
After the Silence creation, the annotations for mininum and maximum scaling limits for autoscaler will be adjusted to 0 what will result in 0 worker nodes in the Node Pool. The patch command in the Cron Job can be repeated for multiple Node Pools to obtain 0 workers Wokload Clusters.

### Scale up and delete silence for the cluster

When the time is right to scale up the cluster again, following [template](cronjob-scale-up.yaml) can be applied:

```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: silences-customer-delete-{CLUSTER-ID}
  namespace: {YOUR_ORGANIZATION}
  labels:
    app: silence-customer
spec:
  schedule: "00 8 * * 1" #Timezone - UTC by default - Mondays, 8 AM UTC
  successfulJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        metadata:
          labels:
            app: silences-customer
        spec:
          serviceAccountName: silences-customer-rbac
          containers:
          - name: silences-customer-delete-{CLUSTER-ID}
            image: quay.io/giantswarm/k8s-initiator
            imagePullPolicy: IfNotPresent
            command:
            - /bin/sh
            - -c
            - |

              kubectl patch MachinePool -n {YOUR_ORGANIZATION} {CLUSTER-ID} --type merge -p '{"metadata" : {"annotations": {"cluster.k8s.io/cluster-api-autoscaler-node-group-min-size": "1"}}}'
              kubectl patch MachinePool -n {YOUR_ORGANIZATION} {CLUSTER-ID} --type merge -p '{"metadata" : {"annotations": {"cluster.k8s.io/cluster-api-autoscaler-node-group-max-size": "3"}}}'

              # Please let the 10minutes in for the workers to appear and initial workloads to be deployed on the cluster.
              sleep 10m

              kubectl delete silence {INSTALLATION}-{CLUSTER-ID}-silence-cluster

          restartPolicy: Never
```

This Cron Job will first patch the minimum and maximum values for scaling. After 10 minutes which are given for workers to come up it will then delete the silence and make the cluster fully supported with oncall by the Giant Swarm.

### Important notes

- Please remember to use the same name of the silence for deletion in order to have your cluster fully monitored.
- Please remember to adjust the Min and Max for scaling up back the cluster, if the requirements in terms of values on your side have changed in between as well.
- Created silences will not be adjusted or maintained by GiantSwarm, meaning that the sole maintenance is at hands of customers.
- It is advised to use the silencing Cron Jobs only for non-production Workload Clusters.

## Summary

Provided solution introduces a way to scale down and silence clusters for specifiied period of time, such as weekends to offload the costs of running resources.
The silences themselves can be also created by hand in case of testing Workload Clusters in order to exclude them from the monitoring loop at Giant Swarm and unnecessary pages towards Oncall.

## Further reading

- [CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
