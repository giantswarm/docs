---
linkTitle: Kernel settings
title: Kernel settings
description: Here's a complete list of the kernel settings we apply to all cluster nodes, be it control plane or worker.
weight: 200
layout: single
menu:
  principal:
    parent: overview-security
    identifier: overview-security-kernel-settings
user_questions:
  - How is the Linux kernel of cluster nodes configured?
last_review_date: 2025-07-14
aliases:
  - /advanced/security/kernel-settings
  - /guides/kernel-settings/
  - /advanced/kernel-settings/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
  - https://github.com/orgs/giantswarm/teams/team-rocket
---

We adjust some kernel settings of Flatcar Container Linux machines used as Kubernetes nodes to non-standard values. Here's a complete reference. For information on other Linux kernel settings, please refer to the [official documentation](https://www.kernel.org/doc/html/latest/).

## General performance and security settings

| Setting                                    | Value | Description                                                                  |
| :----------------------------------------- | :---- | :--------------------------------------------------------------------------- |
| `kernel.kptr_restrict`                     | 2     | Hide kernel pointers to mitigate the kernel's attack surface.                |
| `kernel.panic`                             | 10    | Reboot the system 10 seconds after a kernel panic.                           |
| `kernel.panic_on_oops`                     | 1     | Panic the kernel on oops to prevent an unstable state.                       |
| `kernel.sysrq`                             | 0     | Reduce the kernel's attack surface.                                          |
| `net.ipv4.conf.all.arp_ignore`             | 1     | Harden SSH security.                                                         |
| `net.ipv4.conf.all.arp_announce`           | 2     | Harden SSH security.                                                         |
| `net.ipv4.conf.all.log_martians`           | 1     | Log all martian packets coming to existing network interfaces.               |
| `net.ipv4.conf.all.send_redirects`         | 0     | Don't send redirects for IPv4.                                               |
| `net.ipv4.conf.default.accept_redirects`   | 0     | Don't accept redirects for IPv4.                                             |
| `net.ipv4.conf.default.log_martians`       | 1     | Log all martian packets coming to freshly added network interfaces.          |
| `net.ipv4.tcp_congestion_control`          | bbr   | Set TCP congestion control to BBR for better performance.                    |
| `net.ipv4.tcp_timestamps`                  | 0     | Don't add timestamps to use less CPU cycles.                                 |
| `net.ipv6.conf.all.accept_redirects`       | 0     | Don't send redirects for IPv6.                                               |
| `net.ipv6.conf.all.disable_ipv6`           | 0     | Enable IPv6.                                                                 |
| `net.ipv6.conf.default.accept_redirects`   | 0     | Don't accept redirects for IPv6.                                             |

## Kubernetes-specific tuning

| Setting                                    | Value         | Description                                                                  |
| :----------------------------------------- | :------------ | :--------------------------------------------------------------------------- |
| `net.bridge.bridge-nf-call-ip6tables`      | 1             | Required for Kubernetes networking, enables ip6tables rules for bridged traffic. |
| `net.bridge.bridge-nf-call-iptables`       | 1             | Required for Kubernetes networking, enables iptables rules for bridged traffic.  |
| `net.ipv4.ip_forward`                      | 1             | Enable IP forwarding for IPv4.                                               |
| `net.ipv4.ip_local_reserved_ports`         | 30000-32767   | Reserved to avoid conflicts with kube-apiserver, which allocates within this range. |
| `net.ipv6.conf.all.forwarding`             | 1             | Enable IP forwarding for IPv6.                                               |

## CRI-specific tuning

| Setting                                    | Value | Description                                                              |
| :----------------------------------------- | :---- | :----------------------------------------------------------------------- |
| `fs.inotify.max_user_instances`            | 8192  | Increase the max number of file descriptors to avoid a docker lock.      |
| `fs.inotify.max_user_watches`              | 16384 | Increase the max number of opened file watches to avoid a docker lock.   |
| `net.ipv4.conf.all.rp_filter`              | 0     | Disable rp_filter to avoid dropping mangled packets with Cilium.         |
| `net.ipv4.conf.cilium_*.rp_filter`         | 0     | Disable rp_filter on Cilium interfaces to avoid dropping mangled packets.  |
| `net.ipv4.conf.lxc*.rp_filter`             | 0     | Disable rp_filter on LXC interfaces to avoid dropping mangled packets.     |

## Workload-specific tuning

| Setting            | Value  | Description                                                                                                |
| :----------------- | :----- | :--------------------------------------------------------------------------------------------------------- |
| `vm.max_map_count` | 262144 | Increased mmapfs because some applications, like ES, need higher limit to store data properly.             |
| `vm.overcommit_memory`                     | 1     | Allow memory overcommit to avoid issues with certain applications.           |
