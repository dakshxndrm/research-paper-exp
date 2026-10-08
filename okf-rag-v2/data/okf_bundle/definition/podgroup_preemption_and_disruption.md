---
type: Definition
title: PodGroup Preemption and Disruption
description: Mechanism by which the scheduler preempts PodGroups to free resources
  for higher-priority workloads.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- preemption
- disruption
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- preemption
- disruption
- PodGroup termination
---

When the [scheduler](/definition/kube_scheduler.md) preempts a [PodGroup](/entity/podgroup.md) to make room for higher-priority PodGroups or Pods, it sets the `[DisruptionTarget](/definition/podgroup_conditions.md)` condition to `True` with reason `PreemptionByScheduler`. This condition indicates the PodGroup is about to be terminated due to a disruption such as preemption.
