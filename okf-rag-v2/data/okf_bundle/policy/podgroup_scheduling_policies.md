---
type: Policy
title: PodGroup scheduling policies
description: PodGroups support basic and gang scheduling policies; all Pods in a group
  share the same scheduler name and minimum pod count.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- scheduling policies
- basic gang
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling policies
- basic scheduling
- gang scheduling policies
---

PodGroups support basic and gang [scheduling policies](/configuration/scheduling_policies_configuration.md). All Pods in a [PodGroup](/entity/podgroup.md) must use the same [scheduler name](/limitation/podgroup_scheduling_constraints.md). The [spec.schedulingPolicy](/definition/podgroup_scheduling_policy.md).gang.[minCount](/definition/gang_scheduling_constraints.md) field determines the minimum number of Pods that must be schedulable for the group to be admitted.
