---
type: Entity
title: PodGroup Priority and Disruption
description: Priority and disruption mode of a PodGroup in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- podgroups
- priority
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- podgroup priority
- disruption mode
---

The scheduler considers the specific priority and [disruption mode](/definition/disruption_mode.md) of a [PodGroup](/definition/podgroup.md) to evaluate if and how its [pods](/definition/kubernetes_cluster_architecture.md) can be preempted during [preemption](/procedure/preemption.md) events.
