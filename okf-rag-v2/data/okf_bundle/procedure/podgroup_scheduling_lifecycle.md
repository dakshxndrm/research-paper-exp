---
type: Procedure
title: PodGroup Scheduling Lifecycle
description: Pods are held in PreEnqueue phase until the PodGroup object exists and
  the number of created Pods meets or exceeds minCount.
resource: source://scheduling-eviction__gang-scheduling.md
tags:
- procedure
- lifecycle
timestamp: '2026-09-02T17:04:11+00:00'
---

When the GangScheduling plugin is enabled, the [scheduler](/definition/kube_scheduler.md) alters the lifecycle for Pods belonging to a [PodGroup](/entity/podgroup.md) that has a [gang scheduling policy](/definition/gang_scheduling_policy.md). The process follows these steps for each PodGroup: The scheduler holds Pods in the PreEnqueue phase until the referenced PodGroup object exists and the number of Pods created for the PodGroup is at least equal to [minCount](/definition/gang_scheduling_constraints.md). Pods do not enter the active [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) queue until both conditions are met.
