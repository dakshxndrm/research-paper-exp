---
type: Procedure
title: Scheduling with Workload-Aware Preemption
description: Schedule a PodGroup using workload-aware preemption in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- podgroups
- preemption
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- scheduling podgroups
- workload-aware preemption scheduling
---

The scheduler treats the [PodGroup](/definition/podgroup.md) as a single preemptor unit, rather than evaluating individual [pods](/definition/kubernetes_cluster_architecture.md) from a PodGroup in isolation. It searches for victims across the entire cluster and knows how to treat and preempt other PodGroups as victims according to their disruption modes.
