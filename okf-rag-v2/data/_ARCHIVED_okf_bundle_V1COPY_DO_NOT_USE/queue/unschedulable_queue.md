---
type: Queue
title: Unschedulable Queue
description: The queue where unschedulable Pods are moved.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- queue
---

If it cannot find enough placements to satisfy the `[minCount](/metric/mincount.md)` requirement, none of the [Pods](/definition/kubernetes_cluster_architecture.md) are scheduled. Instead, they are moved to the unschedulable queue to wait for [cluster resources](/resource/cluster_resources.md) to free up.
