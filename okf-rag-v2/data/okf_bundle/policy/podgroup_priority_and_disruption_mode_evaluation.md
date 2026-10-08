---
type: Policy
title: PodGroup priority and disruption mode evaluation
description: The scheduler considers the specific priority and disruption mode of
  a PodGroup to evaluate if and how its pods can be preempted during preemption events.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- preemption
- podgroup
- policy
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup priority
- disruption mode
- preemption policy
---

The [scheduler](/definition/kube_scheduler.md) considers the specific priority and disruption mode of a [PodGroup](/entity/podgroup.md) to evaluate if and how its pods can be preempted during [preemption](/definition/podgroup_preemption_and_disruption.md) events.
