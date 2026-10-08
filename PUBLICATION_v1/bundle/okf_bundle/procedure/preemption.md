---
type: Procedure
title: Preemption
description: The process of preempting a PodGroup to make room for higher-priority
  PodGroups or Pods.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- preemptive scheduling
- scheduler preemption
---

When the scheduler preempts a [PodGroup](/definition/podgroup.md), it sets the `DisruptionTarget` [condition](/condition/quorum_condition.md) to `True` with reason `PreemptionByScheduler`.
