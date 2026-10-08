---
type: Definition
title: Disruption Mode
description: Disruption mode of a PodGroup in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- podgroups
- priority
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- mode
---

The scheduler considers the specific [disruption mode](/entity/podgroup_priority_and_disruption.md) of a [PodGroup](/definition/podgroup.md) to evaluate if and how its [pods](/definition/kubernetes_cluster_architecture.md) can be preempted during [preemption](/procedure/preemption.md) events.
