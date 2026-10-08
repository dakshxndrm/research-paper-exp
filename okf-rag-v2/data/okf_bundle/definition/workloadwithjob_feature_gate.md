---
type: Definition
title: WorkloadWithJob feature gate
description: When enabled, the Job controller automatically creates Workload and PodGroup
  objects for parallel indexed Jobs where parallelism equals completions, implementing
  gang scheduling with minCount set to parallelism.
resource: source://workloads__workload-api.md
tags:
- feature gate
- scheduling
- job controller
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- feature gate enabled
- WorkloadWithJob enabled
- gang scheduling feature
---

# WorkloadWithJob feature gate

When the `WorkloadWithJob` feature gate is enabled, the [Job controller](/procedure/job_controller_workflow.md) automatically creates Workload and [PodGroup](/entity/podgroup.md) objects for parallel indexed Jobs where `.spec.parallelism` equals `.spec.completions`. The [gang policy](/definition/gang_scheduling_constraints.md)'s `minCount` is set to the Job's parallelism, so all Pods must be schedulable together before any of them are bound to nodes.
