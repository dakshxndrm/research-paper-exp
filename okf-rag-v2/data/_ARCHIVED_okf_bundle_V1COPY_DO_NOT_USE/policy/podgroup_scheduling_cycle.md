---
type: Policy
title: PodGroup Scheduling Cycle
description: The process of evaluating a group of Pods as a single unit for scheduling.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- podgroup cycle
- scheduling cycle
---

To support [scheduling](/concept/scheduling.md) a [group of Pods](/definition/podgroup.md) together, the [kube-scheduler](/policy/kubernetes_scheduling_overview.md) uses the **[PodGroup scheduling](/process/podgroup_scheduling_process.md) cycle**. Instead of processing [Pods](/definition/kubernetes_cluster_architecture.md) individually and holding them at a `WaitOnPermit` gate, the scheduler evaluates the entire group of pending Pods belonging to a specific PodGroup collectively.
