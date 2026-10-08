---
type: Procedure
title: Understanding the Gang Scheduling Algorithm
description: A step-by-step guide to understanding the gang scheduling algorithm.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- gang-scheduling-algorithm
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- gang scheduling
- scheduling algorithm
---

The [gang scheduling](/procedure/gang_scheduling.md) algorithm is used by PodGroups with a [gang scheduling policy](/definition/gang_scheduling_policy.md). It requires at least 4 [Pods](/definition/kubernetes_cluster_architecture.md) to be schedulable simultaneously.
