---
type: Limitation
title: Same Scheduler Name for All Pods in a Group
description: Requirement that all Pods in a group use the same scheduler name.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- pod
- scheduler
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduler name
- same scheduler
---

All [Pods](/definition/kubernetes_cluster_architecture.md) in a `[PodGroup](/definition/podgroup.md)` must use the same `.spec.schedulerName`. If a mismatch is detected, the scheduler rejects all Pods in the group as unschedulable.
