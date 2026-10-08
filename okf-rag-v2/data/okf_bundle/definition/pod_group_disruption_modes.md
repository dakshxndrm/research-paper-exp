---
type: Definition
title: Pod Group Disruption Modes
description: PodGroup defines two disruption modes, Pod and PodGroup, that dictate
  how the scheduler can disrupt running pods during workload-aware preemption events.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- disruption
- scheduler
- preemption
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- disruption mode
- Pod disruption mode
- PodGroup disruption mode
---

## [Disruption mode](/policy/podgroup_priority_and_disruption_mode_evaluation.md) types

As of 1.36, the `priority` or `disruptionMode` fields of the [PodGroup](/entity/podgroup.md) are only respected by [workload-aware preemption](/feature/workload_aware_preemption_mechanism.md). During the [pod scheduling](/definition/kubernetes_scheduling_overview.md) phase, the [scheduler](/definition/kube_scheduler.md) does not take into account the `priority` or `disruptionMode` fields of the PodGroup.

The API supports two [disruption](/definition/podgroup_preemption_and_disruption.md) modes: `Pod` and `PodGroup`. The default one is `Pod`.

### Pod

The `Pod` mode instructs the scheduler to treat all Pods in the group as separate entities, allowing independent disruption of a single pod from a PodGroup.

### PodGroup

The `PodGroup` mode emphasizes "all-or-nothing" semantics for disruption. It instructs the scheduler that all pods from the PodGroup have to be disrupted together.
