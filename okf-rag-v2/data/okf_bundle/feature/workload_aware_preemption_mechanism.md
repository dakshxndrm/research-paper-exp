---
type: Feature
title: Workload-aware preemption mechanism
description: A preemption mechanism designed for PodGroups that treats the group as
  a single preemptor unit and evaluates the entire cluster as a single domain to make
  scheduling possible.
resource: source://scheduling-eviction__workload-aware-preemption.md
tags:
- preemption
- podgroup
- scheduling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- preemption mechanism
- workload-aware preemption
- PodGroup preemption
---

Workload-aware [preemption](/definition/podgroup_preemption_and_disruption.md) introduces a preemption mechanism specifically designed for PodGroups. When a [PodGroup](/entity/podgroup.md) cannot be scheduled, the [scheduler](/definition/kube_scheduler.md) utilizes a preemption logic that tries to make [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) of this PodGroup possible. This approach is used exclusively during [PodGroup scheduling](/concept/podgroup_lifecycle_and_controller_relationship.md) and replaces the [default preemption](/defaultbehavior/default_pod_preemption_for_single_pods.md) mechanism for pods from a given PodGroup. When this feature is enabled, the scheduler treats the PodGroup as a single preemptor unit, rather than evaluating individual pods from a PodGroup in isolation. To make room for the pending pods in the group, it searches for victims across the entire cluster, and knows how to treat and preempt other PodGroups as victims according to their disruption modes.
