---
type: Hierarchy
title: Victim importance hierarchy
description: 'The scheduler uses a strict hierarchy to decide which preemption units
  are more critical and should be spared: priority, workload type, group size, and
  start time.'
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- preemption
- hierarchy
- victim selection
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- importance hierarchy
- preemption hierarchy
- victim selection hierarchy
---

The [scheduler](/definition/kube_scheduler.md) decides which [preemption](/definition/podgroup_preemption_and_disruption.md) units (individual pods or PodGroups) are more critical and should be spared from preemption using a strict hierarchy: * Priority: Higher priority units are always more important. * Workload type: PodGroups are considered more important than individual Pods of the same priority. * Group size (PodGroups): If both units are PodGroups, the one with more members (larger size) is considered more important. * Start time: Units that started earlier are more important.
