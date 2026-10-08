---
type: Metric
title: Priority Value
description: The integer value representing the priority.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- integer priority
---

The priority of a [PodGroup](/definition/podgroup.md) is an authoritative priority for all [pods](/definition/kubernetes_cluster_architecture.md) in the group during [workload-aware preemption](/policy/workload_aware_preemption_policy.md) events, even when priorities of individual pods forming this PodGroup differ.
