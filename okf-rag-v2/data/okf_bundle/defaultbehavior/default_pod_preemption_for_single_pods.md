---
type: DefaultBehavior
title: Default pod preemption for single Pods
description: When scheduling a single Pod, the default pod preemption applies. As
  of version 1.36, default preemption for a single Pod does not respect the priority
  or disruptionMode fields of a PodGroup when attempting to preempt a Pod belonging
  to that group.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- preemption
- single pod
- version 1.36
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- default preemption
- single Pod preemption
- preemption behavior
---

When [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) a single Pod, the default pod [preemption](/definition/podgroup_preemption_and_disruption.md) applies. As of 1.36, when the [scheduler](/definition/kube_scheduler.md) performs a default preemption for a single Pod and it attempts to preempt a Pod belonging to a [PodGroup](/entity/podgroup.md), it does not respect the priority or disruptionMode fields of that PodGroup.
