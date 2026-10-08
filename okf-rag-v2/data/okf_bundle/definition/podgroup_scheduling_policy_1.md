---
type: Definition
title: PodGroup scheduling policy
description: Each PodGroupTemplate entry requires a scheduling policy of basic or
  gang, with optional priority and disruption mode when WorkloadAwarePreemption is
  enabled.
resource: source://workloads__workload-api.md
tags:
- scheduling
- policy
- podgrouptemplate
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- workload scheduling policy
- basic vs gang policy
- PodGroup scheduling mode
---

# [PodGroup scheduling policy](/definition/podgroup_scheduling_policy.md)

Each entry in `[podGroupTemplates](/definition/podgrouptemplates.md)` must have a [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) policy (`basic` or `gang`). If the `WorkloadAwarePreemption` feature gate is enabled each entry in `podGroups` can also have priority and [disruption mode](/policy/podgroup_priority_and_disruption_mode_evaluation.md).
