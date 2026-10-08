---
type: Configuration
title: Kubelet Container GC Parameters
description: Lists and explains the configurable variables that the kubelet uses for
  garbage collecting unused containers.
resource: source://architecture__garbage-collection.md
tags:
- kubelet
- containers
- garbage collection
- configuration
- parameters
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- container garbage collection
- MinAge
- MaxPerPodContainer
- MaxContainers
---

The [kubelet](/definition/kubernetes_node_components_overview.md) garbage collects unused containers based on the following configurable variables:

*   `MinAge`: The minimum age at which the kubelet can garbage collect a container. Setting this to `0` disables the age check.
*   `MaxPerPodContainer`: The maximum number of dead containers each Pod can have. Setting this to less than `0` disables this limit.
*   `MaxContainers`: The maximum number of dead containers the cluster can have. Setting this to less than `0` disables this limit.

In addition to these variables, the kubelet garbage collects unidentified and deleted containers, typically starting with the oldest first.

`MaxPerPodContainer` and `MaxContainers` may conflict if retaining the maximum number of containers per Pod (`MaxPerPodContainer`) would exceed the global limit of dead containers (`MaxContainers`). In such cases, the kubelet adjusts `MaxPerPodContainer` to resolve the conflict, potentially downgrading it to `1` and evicting the oldest containers. Containers owned by deleted [pods](/definition/kubernetes_cluster_architecture.md) are removed once they are older than `MinAge`.

The kubelet only garbage collects the containers it manages.
