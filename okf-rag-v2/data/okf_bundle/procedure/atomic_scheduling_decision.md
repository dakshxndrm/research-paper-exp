---
type: Procedure
title: Atomic Scheduling Decision
description: The scheduler makes a single atomic scheduling decision for all Pods
  in the group using the PodGroup scheduling cycle.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- procedure
- scheduling-cycle
timestamp: '2026-09-02T17:04:11+00:00'
---

Once the quorum is met, the [scheduler](/definition/kube_scheduler.md) attempts to find placements for all Pods in the group. It utilizes the [PodGroup scheduling cycle](/procedure/podgroup_scheduling_cycle.md) to make a single, atomic [scheduling decision](/definition/binding_process.md). The GangScheduling plugin implements a Permit [extension](/definition/third_party_workload_resources.md) point that is evaluated for each schedulable Pod during the cycle. This is used to determine whether the [minCount](/definition/gang_scheduling_constraints.md) constraint is satisfied, by comparing the number of successfully placed pods against the minCount value.
