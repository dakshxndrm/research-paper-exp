---
type: Procedure
title: PodGroup Scheduling Cycle
description: The scheduler evaluates all pending Pods in a PodGroup collectively,
  using a single cycle that snapshots cluster state and applies atomic binding decisions.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- procedure
- workflow
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling cycle
- PodGroup cycle
- binding phase
---

When the [scheduler](/definition/kube_scheduler.md) pops a Pod belonging to a [PodGroup](/entity/podgroup.md), it retrieves all other queued Pods in that group and sorts them deterministically by priority and observation time. The [PodGroup scheduling cycle](/definition/podgroup_scheduling_overview.md) proceeds in three steps: First, the scheduler takes a single snapshot of the [cluster state](/concept/desired_versus_current_state.md) that lasts for the entire duration of the cycle to ensure consistency and prevent race conditions. Second, the scheduler runs the [PodGroup scheduling algorithm](/algorithm/podgroup_scheduling_algorithm.md) to find valid Node placements for all Pods in the group. Third, the [scheduling decision](/definition/binding_process.md) is applied atomically; if successful, Pods proceed to binding, and any remaining [unschedulable Pods](/definition/unschedulable_pods.md) return to the queue. If the scheduler cannot find enough resources, the entire PodGroup is considered unschedulable, no Pods are bound, and all are returned to the [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) queue with standard backoff logic. If new Pods are added after some have been scheduled, the cycle evaluates the new Pods while accounting for existing ones.
