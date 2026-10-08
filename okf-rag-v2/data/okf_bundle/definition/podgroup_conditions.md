---
type: Definition
title: PodGroup Conditions
description: Status conditions updated by the scheduler after a PodGroup scheduling
  cycle completes, including scheduling status and disruption indicators.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- conditions
- status
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- status conditions
- PodGroup status
- DisruptionTarget
---

After a [PodGroup scheduling cycle](/procedure/podgroup_scheduling_cycle.md) completes, the [scheduler](/definition/kube_scheduler.md) updates conditions on the [PodGroup](/entity/podgroup.md)'s `[status.conditions](/definition/podgroup_scheduling_status_conditions.md)`. The `PodGroupScheduled` condition reports whether the PodGroup has been successfully scheduled; for `gang` policy PodGroups, this means at least `[minCount](/definition/gang_scheduling_constraints.md)` Pods were placed. When [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) fails, `PodGroupScheduled` is set to `False` with reason `Unschedulable` if resource constraints or [affinity rules](/definition/node_selection_mechanisms.md) prevent placement, or `SchedulerError` if an internal error occurs during constraint parsing. The `DisruptionCondition` indicates the PodGroup is about to be terminated due to [disruption](/definition/podgroup_preemption_and_disruption.md), set to `True` with reason `PreemptionByScheduler` when the scheduler preempts a PodGroup to make room for higher-priority groups or Pods.
