---
type: Policy
title: Workload-Aware Preemption Policy
description: Preemption mechanism for PodGroups in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- podgroups
- preemption
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- workload-aware preemption
- preemption policy
---

[Workload](/entity/workload.md)-aware [preemption](/procedure/preemption.md) introduces a [preemption](/procedure/selecting_victims_for_preemption.md) mechanism specifically designed for PodGroups. When a [PodGroup](/definition/podgroup.md) cannot be scheduled, the scheduler utilizes a preemption logic that tries to make [scheduling](/concept/scheduling.md) of this PodGroup possible.
