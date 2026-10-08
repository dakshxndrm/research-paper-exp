---
type: Definition
title: PodGroupTemplates
description: The spec.podGroupTemplates list defines the distinct components of a
  workload, such as driver and worker templates for a machine learning job.
resource: source://workloads__workload-api.md
tags:
- api
- podgroup
- workload component
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- podGroup template list
- workload component list
- scheduling policy template
---

# PodGroupTemplates

The `spec.podGroupTemplates` list defines the distinct components of your workload. For example, a machine learning job might have a `driver` [template](/entity/podgrouptemplate.md) and a `worker` template.

Each entry in `podGroupTemplates` must have:
1. A unique `name` that will be used to reference the template in the `[PodGroup](/entity/podgroup.md)`'s `[spec.podGroupTemplateRef](/definition/podgroup_template_reference.md)`.
2. A [scheduling policy](/definition/podgroup_scheduling_policy.md) (`basic` or `gang`).

If the `WorkloadAwarePreemption` feature gate is enabled each entry in `podGroups` can also have priority and [disruption mode](/policy/podgroup_priority_and_disruption_mode_evaluation.md).

The maximum number of PodGroupTemplates in a single Workload is 8.

When a [workload controller](/definition/workload_controller.md) creates a `PodGroup` from one of these templates, it copies the `schedulingPolicy` into the `PodGroup`'s own spec. Changes to the `Workload` only affect newly created `PodGroups`, not existing ones.
