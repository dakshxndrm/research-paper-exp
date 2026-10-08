---
type: Definition
title: PodGroup basic vs gang scheduling policy
description: 'The two types of scheduling policies available for PodGroups: basic
  policy and gang policy which requires all Pods to be schedulable simultaneously.'
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- scheduling policy
- basic
- gang
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling policy types
- basic scheduling
- gang scheduling
- policy types
---

Each [PodGroup](/entity/podgroup.md) carries a [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) policy (basic or gang) in [spec.schedulingPolicy](/definition/podgroup_scheduling_policy.md). When a [workload controller](/definition/workload_controller.md) creates the PodGroup, this policy is copied from the Workload's [PodGroupTemplate](/entity/podgrouptemplate.md) at creation time. For standalone PodGroups, you set the policy directly.
