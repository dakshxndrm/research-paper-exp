---
type: Definition
title: Victim Importance Hierarchy
description: Hierarchy of importance for preemption units in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- preemption
- priority
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- victim importance
- preemption hierarchy
---

The scheduler decides which [preemption](/procedure/preemption.md) units (individual [pods](/definition/kubernetes_cluster_architecture.md) or PodGroups) are more critical and should be spared from [preemption](/procedure/selecting_victims_for_preemption.md) using a strict hierarchy: * Priority: Higher priority units are always more important. * [Workload](/entity/workload.md) type: PodGroups are considered more important than individual Pods of the same priority.
