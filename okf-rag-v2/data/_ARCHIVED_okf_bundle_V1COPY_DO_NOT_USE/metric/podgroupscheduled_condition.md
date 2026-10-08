---
type: Metric
title: PodGroupScheduled Condition
description: A condition reflecting the initial scheduling decision.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- podgroup-scheduled
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduling status
- PodGroup condition
---

The `PodGroupScheduled` [condition](/condition/quorum_condition.md) reflects the initial [scheduling decision](/decision/scheduling_decision.md) only. The scheduler does not update it if [Pods](/definition/kubernetes_cluster_architecture.md) later fail or are evicted.
