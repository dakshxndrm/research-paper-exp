---
type: Definition
title: PodGroup scheduling policy
description: The scheduling policy for a PodGroup, either 'basic' or 'gang', defined
  in spec.schedulingPolicy and copied from the Workload's PodGroupTemplate at creation
  time.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- scheduling policy
- basic
- gang
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduling policy
- basic policy
- gang policy
- spec.schedulingPolicy
---

Each [PodGroup](/entity/podgroup.md) carries a [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) policy (basic or gang) in spec.schedulingPolicy. When a [workload controller](/definition/workload_controller.md) creates the PodGroup, this policy is copied from the Workload's [PodGroupTemplate](/entity/podgrouptemplate.md) at creation time. For standalone PodGroups, you set the policy directly.
