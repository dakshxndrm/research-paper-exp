---
type: Process
title: PodGroup Scheduling Process
description: The process followed by the scheduler for each PodGroup.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- podgroup scheduling
- scheduling process
---

The [process](/concept/pod_definition.md) follows these steps for each [PodGroup](/definition/podgroup.md):

1. The scheduler holds [Pods](/definition/kubernetes_cluster_architecture.md) in the `PreEnqueue` phase until:
   * The referenced [PodGroup object](/entity/podgroup_api_resource.md) exists.
   * The number of `Pods` created for the `PodGroup` is at least equal to `[minCount](/metric/mincount.md)`.
