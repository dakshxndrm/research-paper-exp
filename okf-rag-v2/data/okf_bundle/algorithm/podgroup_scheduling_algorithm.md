---
type: Algorithm
title: PodGroup Scheduling Algorithm
description: The default algorithm iterates through Pods, finds feasible nodes, and
  checks group scheduling criteria via the Permit extension point.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- algorithm
- workflow
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling algorithm
- default algorithm
- PodGroup placement
---

The default [PodGroup scheduling](/concept/podgroup_lifecycle_and_controller_relationship.md) algorithm relies on the baseline Pod-based [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) algorithm. For each Pod in the group, the algorithm finds a feasible node using standard per-Pod filtering and scoring phases. If a Pod fits, it is temporarily reserved on the selected node until the algorithm completes. If a Pod cannot fit, the [scheduler](/definition/kube_scheduler.md) attempts [preemption](/definition/podgroup_preemption_and_disruption.md) via the `PostFilter` [extension](/definition/third_party_workload_resources.md) point. After processing each Pod, the algorithm checks whether schedulable Pods meet the group's scheduling criteria, such as the `[minCount](/definition/gang_scheduling_constraints.md)` constraint for [gang scheduling](/definition/workload_placement_and_podgrouptemplates.md), using the `Permit` extension point. If `Permit` returns `Success` for any Pod, the [PodGroup](/entity/podgroup.md) is deemed feasible. If all Pods are processed without achieving `Success`, the PodGroup is considered unschedulable.
