---
type: Procedure
title: Understanding Limitations of PodGroups
description: A step-by-step guide to understanding limitations of podgroups.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- podgroup-limitations
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- podgroup limitations
- scheduling unit limitations
---

The `PodGroupScheduled` [condition](/condition/quorum_condition.md) reflects the initial [scheduling decision](/decision/scheduling_decision.md) only. The scheduler does not update it if [Pods](/definition/kubernetes_cluster_architecture.md) later fail or are evicted.
