---
type: Definition
title: Atomic PodGroup Binding
description: The all-or-nothing binding decision where all Pods in a group are placed
  together or none are placed.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- binding
- workflow
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- binding
- atomic decision
- placement binding
---

The [PodGroup scheduling cycle](/procedure/podgroup_scheduling_cycle.md) applies atomic decisions for the entire group. If sufficient resources and valid placements are found, Pods proceed directly to the [binding](/definition/binding_process.md) cycle with their selected nodes. Any remaining [unschedulable Pods](/definition/unschedulable_pods.md) are returned to the [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) queue. If the [scheduler](/definition/kube_scheduler.md) cannot find enough resources, the entire [PodGroup](/entity/podgroup.md) is unschedulable and no Pods are bound; instead, all Pods return to the scheduling queue for later retry. This approach avoids inefficient bottlenecks where partially scheduled groups reserve cluster capacity while waiting indefinitely for the rest of their group to fit.
