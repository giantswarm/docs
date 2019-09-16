+++
title = "Cluster Health"
description = "What defines a healthy or unhealthy tenant cluster according to Giant Swarm"
date = "2019-09-16"
layout = "subsection"
weight = 30
+++

# Cluster health

Giant Swarm gives you a high-level assessment of the health of your tenant clusters. You can use this assessment to decide whether you should investigate a problem with the cluster, take any action (e. g. adding resources) or check back with the Giant Swarm support staff to collaborate on any issue mitigation.

**Important note:** Cluster health is a recent addition and only takes into consideration a limited set of information. Some possible failure sources, like for example on the overlay networking layer, will not be taken into account. We are working on increasing the coverage and value your input regarding requirements and priorities.

## Health categories

We categorize cluster health in a system that comprises three levels:

- <strong style="color: green">GOOD</strong>: The cluster should work as expected, is scalable and resilient.

- <strong style="color: orange">PASSABLE</strong>: Some part of the cluster is in a state that is not considered ideal. Scalability or resilience may be impaired. However should not affect scheduled workloads and the cluster is considered functional in general.

- <strong style="color: red">BAD</strong>: Something is wrong with the cluster that likely needs fixing. Please contact the Giant Swarm support team to get more information regarding the investigation and mitigation.

## Aggregation throughout levels

While there are pure cluster-level state details that influence the health assessment, a cluster's health assessment also reflects the state of the worker and master nodes the cluster comprises.

In clusters without node pools, aggregation of node health directly influences the cluster health assessment.

For clusters with node pools, the node's health is aggregated on the node pools level. Then the cluster health is derived considering the health of all node pools in the cluster.

```nohighlight
TODO: image

  master node(s) --> cluster
  worker nodes  /

  master node(s) --> node pool --> cluster
  worker nodes  /

```

### Rules

This sections explains in full detail the logic that defines health assessment on each level.

The rules contain both ones evaluated on an individual level as well as aggregation rules, taking into consideration health assessments from lower levels.

When combining the outcome of different rules on a level, there is a simple priority system defining the result:

- <strong style="color: orange">PASSABLE</strong> will override <strong style="color: green">GOOD</strong>.
- <strong style="color: red">BAD</strong> will override <strong style="color: orange">PASSABLE</strong>.

#### Master nodes

- If the node's state anything different than `Ready`, the node's health is reported as <strong style="color: red">BAD</strong>.

#### Worker nodes

- If the node's state is not `Ready`, the node's health is reported as <strong style="color: orange">PASSABLE</strong>.

- If the sum of CPU limits of workloads scheduled to the node exceed `TODO` % of the node's CPU resources, the node's health is reported as <strong style="color: orange">PASSABLE</strong>.

#### Clusters and node pools

- If the cluster/node pool is in state `Creating` or `Deleting`, it will be reported as <strong style="color: orange">PASSABLE</strong>.

- If the cluster's/node pool's AWS CloudFormation stack is in state `FAILED`, it will be reported as <strong style="color: red">BAD</strong>.

- If a master node of the cluster/node pool is not GOOD:
  - If the cluster is in `Upgrading` state, then the cluster (or node pool) health is <strong style="color: orange">PASSABLE</strong>.
  - If the cluster is not in `Upgrading` state, then the cluster (or node pool) health is <strong style="color: red">BAD</strong>.

- If the cluster (or node pool) state is neither `Creating` nor `Deleting`, then
  - If less than 75% of worker nodes are in state `Ready`, then cluster (or node pool) health is <strong style="color: orange">PASSABLE</strong>.
  - If the cluster or node pool is supposed to have 20 or more workers and less than 50% of the worker nodes are in state `Ready`, then cluster (or node pool) health is <strong style="color: orange">RED</strong>.
  - If less than three worker nodes are in a state other than `Ready`, the cluster (or node pool) health will be reported as <strong style="color: red">BAD</strong>.

#### Clusters with node pools

- If any of the node pools is <strong style="color: orange">PASSABLE</strong>, the cluster health will be reported as <strong style="color: orange">PASSABLE</strong>.

- If any of the node pools is <strong style="color: red">BAD</strong>, the cluster health will be reported as <strong style="color: red">BAD</strong>.


## Further reading

```
TODO: Links to
- web interface reference regarding health display
- API docs
```