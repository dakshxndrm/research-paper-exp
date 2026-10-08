---
type: Resource
title: Cluster Resources
description: The cluster resources required for gang scheduling.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- resource
---

If it cannot find enough placements to satisfy the `[minCount](/metric/mincount.md)` requirement, none of the [Pods](/definition/kubernetes_cluster_architecture.md) are scheduled. Instead, they are moved to the [unschedulable queue](/queue/unschedulable_queue.md) to wait for [cluster resources](/metric/resource_allocation_metrics_in_kubernetes.md) to free up.
