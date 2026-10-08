---
type: Metric
title: minCount Metric
description: The minimum number of Pods required for gang scheduling.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- min count
- metric
---

If the scheduler finds valid placements for at least the `[minCount](/metric/mincount.md)` number of Pods, it allows those successfully placed Pods to be bound to their assigned [nodes](/definition/kubernetes_cluster_architecture.md).
