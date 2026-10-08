---
type: Definition
title: Gang Scheduling Constraints
description: The `minCount` requirement that determines the minimum number of Pods
  that must be placed together for gang scheduling to succeed.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- constraints
- gang
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- minCount
- gang policy
- scheduling constraints
---

For `gang` policy PodGroups, the `[PodGroupScheduled](/definition/podgroup_scheduling_status_conditions.md)` condition being `True` means that at least `minCount` Pods were successfully placed. The [scheduling algorithm](/algorithm/podgroup_scheduling_algorithm.md) checks whether schedulable Pods meet the group's criteria, including the `minCount` constraint, using the `Permit` [extension](/definition/third_party_workload_resources.md) point. If the algorithm cannot find sufficient resources to satisfy the `minCount` requirement, the [PodGroup](/entity/podgroup.md) is deemed unschedulable and no Pods are bound.
