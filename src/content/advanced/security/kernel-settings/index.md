---
linkTitle: Kernel settings
title: Kernel settings
description: Complete list of the kernel settings we apply to all cluster nodes, be it control plane or worker.
weight: 200
menu:
  main:
    parent: advanced-security
user_questions:
  - How is the Linux kernel of cluster nodes configured?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
  - https://github.com/orgs/giantswarm/teams/team-rocket
last_review_date: 2022-07-12
aliases:
  - /reference/kernel-settings/
---

We adjust some kernel settings of Flatcar Container Linux machines used as Kubernetes nodes to non-standard values. Here is a complete reference. For information on other Linux kernel settings, please refer to the [official documentation](https://www.kernel.org/doc/html/latest/).

## General Performance and Security settings

| Setting                                  | Value | Description                                                         |
| ---                                      | ---   | ---                                                                 |
| `kernel.kptr_restrict`                   | 2     | Hide kernel pointers to mitigate the kernels attack surface         |
| `kernel.sysrq`                           | 0     | Reduce the kernel's attack surface                                  |
| `net.ipv4.conf.all.arp_ignore`           | 1     | Harden SSH security                                                 |
| `net.ipv4.conf.all.arp_announce`         | 2     | Harden SSH security                                                 |
| `net.ipv4.conf.all.log_martians`         | 1     | Log all martians packets coming to existing network interfaces      |
| `net.ipv4.conf.all.rp_filter`            | 1     | Harden SSH security                                                 |
| `net.ipv4.conf.all.send_redirects`       | 0     | Do not send redirects for IPv4                                      |
| `net.ipv4.conf.default.accept_redirects` | 0     | Do not accept redirects for IPv4                                    |
| `net.ipv4.conf.default.log_martians`     | 1     | Log all martians packets coming to freshly added network interfaces |
| `net.ipv4.tcp_timestamps`                | 0     | Do not add timestamps to use less CPU cycles                        |
| `net.ipv6.conf.all.accept_redirects`     | 0     | Do not send redirects for IPv6                                      |
| `net.ipv6.conf.default.accept_redirects` | 0     | Do not accept redirects for IPv6                                    |

## Kubernetes specific tuning

| Setting                            | Value         | Description                                                                 |
| ---                                | ---           | ---                                                                         |
| `net.ipv4.ip_local_reserved_ports` | 30000 - 32767 | Reserving for Node Ports allocations to avoid conflicts with kube-apiserver |

## Docker specific tuning

| Setting                         | Value | Description                                                         |
| ---                             | ---   | ---                                                                 |
| `fs.inotify.max_user_watches`   | 16384 | Increase the max number of opened file watches to avoid docker lock |
| `fs.inotify.max_user_instances` | 8192  | Increase the max number of file descriptors to avoid docker lock    |

## Workload specific tuning

| Setting            | Value  | Description                                                                                                |
| ---                | ---    | ---                                                                                                        |
| `vm.max_map_count` | 262144 | Increased max_map_count because some applications, like Elasticsearch, need higher limit to start properly |

## Unified cgroup hierarchy - cgroups v1 enforcement

| Setting                                    | Value | Description                                                                                                          |
| ---                                        | ---   | ---                                                                                                                  |
| `systemd.unified_cgroup_hierarchy`         | 0     | [Switching to unified cgroups](https://www.flatcar.org/docs/latest/container-runtimes/switching-to-unified-cgroups/) |
| `systemd.legacy_systemd_cgroup_controller` | null  | [Switching to unified cgroups](https://www.flatcar.org/docs/latest/container-runtimes/switching-to-unified-cgroups/) |
