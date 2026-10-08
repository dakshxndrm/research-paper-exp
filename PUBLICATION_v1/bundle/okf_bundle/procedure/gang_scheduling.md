---
type: Procedure
title: Gang Scheduling
description: A scheduling policy that groups Pods together for scheduling.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- gang policy
- podgroup gang
---

For [gang policy](/policy_type/gang_policy.md) PodGroups, the scheduler attempts to find placements for all [Pods](/definition/kubernetes_cluster_architecture.md) in the group simultaneously.
