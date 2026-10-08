---
type: Procedure
title: Creation Ordering of Objects
description: Order in which controllers must create objects.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- controller
- workload
- podgroup
- pod
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- creation order
- object creation
---

[Controllers](/pattern/kubernetes_controller_pattern.md) must create objects in this order: 1. `[Workload](/entity/workload.md)` — the [scheduling policy](/concept/workload_placement.md) [template](/entity/podgrouptemplate.md). 2. `[PodGroup](/definition/podgroup.md)` — the [runtime](/entity/container_runtime_1.md) instance. 3. `[Pods](/definition/kubernetes_cluster_architecture.md)` — with `spec.schedulingGroup.podGroupName` pointing to the `PodGroup`.
