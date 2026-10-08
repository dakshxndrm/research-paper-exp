---
type: Definition
title: Workload controller
description: The controller that creates PodGroup objects from Workload PodGroupTemplates
  at runtime.
resource: source://workloads__workload-api.md
tags:
- controller
- runtime
- scheduling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Job controller
- workload management controller
- PodGroup creator
---

# [Workload controller](/concept/podgroup_lifecycle_and_controller_relationship.md)

While workload controllers such as Job manage the application's [runtime](/definition/container_runtime.md) state, the `Workload` specifies how groups of `Pods` should be scheduled. The [Job controller](/procedure/job_controller_workflow.md) is the only built-in controller that creates [PodGroup](/entity/podgroup.md) objects from the `Workload`'s `[PodGroupTemplates](/definition/podgrouptemplates.md)` at runtime.

When a workload controller creates a `PodGroup` from one of these templates, it copies the `schedulingPolicy` into the `PodGroup`'s own spec. Changes to the `Workload` only affect newly created `PodGroups`, not existing ones.

Other workload controllers (such as JobSet) may manage their own Workload and PodGroup objects independently.
