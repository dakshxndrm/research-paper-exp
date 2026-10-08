---
type: Procedure
title: Default Pod Preemption
description: Default preemption mechanism for single Pods in Kubernetes.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- kubernetes
- podgroups
- preemption
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- single pod preemption
---

When [scheduling](/concept/scheduling.md) a single Pod, the default pod [preemption](/procedure/preemption.md) applies. The scheduler performs a default [preemption](/procedure/selecting_victims_for_preemption.md) for a single Pod and attempts to preempt a Pod belonging to a [PodGroup](/definition/podgroup.md).
