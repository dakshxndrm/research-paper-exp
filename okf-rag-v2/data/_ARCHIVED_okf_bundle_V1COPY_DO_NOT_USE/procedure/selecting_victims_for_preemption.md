---
type: Procedure
title: Selecting Victims for Preemption
description: Selection of victims for preemption in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- podgroups
- preemption
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- victim selection
- preemption
---

The scheduler selects a set of victims across multiple [nodes](/definition/kubernetes_cluster_architecture.md) that can be removed to make enough room for the preemptor [PodGroup](/definition/podgroup.md) to be scheduled.
