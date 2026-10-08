---
type: Procedure
title: Scheduling Gates
description: Holds off PodGroup scheduling until all pods are in the scheduling queue.
resource: source://workloads__workload-api__topology-aware-scheduling.md
tags:
- workload-api
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduling gate
- pod group scheduling
---

To partially mitigate the limitation of inconsistent behavior, you can use [scheduling](/concept/scheduling.md) gates to hold off [PodGroup scheduling](/process/podgroup_scheduling_process.md) until all [pods](/definition/kubernetes_cluster_architecture.md) within the [PodGroup](/definition/podgroup.md) are in the [scheduling](/policy/kubernetes_scheduling_overview.md) [queue](/queue/unschedulable_queue.md).
