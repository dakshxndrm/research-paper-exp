---
type: Procedure
title: Pod Sorting
description: The process of sorting Pods deterministically for scheduling.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- pod ordering
- scheduler pod sort
---

The scheduler sorts the [Pods](/definition/kubernetes_cluster_architecture.md) in a [PodGroup](/definition/podgroup.md) deterministically based on priority and the time they were initially observed by the scheduler.
