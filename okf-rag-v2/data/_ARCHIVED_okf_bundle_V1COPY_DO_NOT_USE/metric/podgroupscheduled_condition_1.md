---
type: Metric
title: PodGroupScheduled Condition
description: Condition reflecting the outcome of initial scheduling attempt.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- scheduler
- metric
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- condition
- scheduling
---

The `PodGroupScheduled` [condition](/condition/quorum_condition.md) reflects the outcome of the initial [scheduling](/concept/scheduling.md) attempt only. Once the condition is set to `True`, the scheduler does not update it if [Pods](/definition/kubernetes_cluster_architecture.md) later fail, are evicted, or stop running.
