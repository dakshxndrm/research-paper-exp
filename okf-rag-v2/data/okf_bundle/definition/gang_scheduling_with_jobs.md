---
type: Definition
title: Gang scheduling with Jobs
description: When the WorkloadWithJob feature gate is enabled, the Job controller
  automatically creates Workload and PodGroup objects for parallel indexed Jobs where
  parallelism equals completions, setting the gang policy's minCount to the Job's
  parallelism.
resource: source://workloads__workload-api.md
tags:
- scheduling
- job
- gang policy
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- gang policy
- minCount scheduling
- parallel Job scheduling
---

# [Gang scheduling](/definition/workload_placement_and_podgrouptemplates.md) with Jobs

When the `WorkloadWithJob` feature gate is enabled, the [Job controller](/procedure/job_controller_workflow.md) automatically creates Workload and [PodGroup](/entity/podgroup.md) objects for parallel indexed Jobs where `.spec.parallelism` equals `.spec.completions`. The [gang policy](/definition/gang_scheduling_constraints.md)'s `minCount` is set to the Job's parallelism, so all Pods must be schedulable together before any of them are bound to nodes.

This is the built-in path for using gang [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) with Jobs. You do not need to [create](/operations/kubectl_resource_management_operations.md) Workload or PodGroup objects yourself as the Job controller handles it automatically. Other workload controllers (such as JobSet) may manage their own Workload and PodGroup objects independently.
