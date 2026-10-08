---
type: Procedure
title: Setting Scheduling Policies via PodGroupTemplates
description: Explains how scheduling policies are defined and applied within PodGroupTemplates
  in the Workload API.
resource: source://workloads__workload-api__policies.md
tags:
- scheduling
- workload api
- podgrouptemplate
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroupTemplate policy
- Workload API policy
- template policy
---

When using the Workload API, [scheduling policies](/configuration/scheduling_policies_configuration.md) are defined inside `[PodGroupTemplates](/definition/podgrouptemplates.md)`. The [workload controller](/definition/workload_controller.md) copies the policy from the [template](/entity/podgrouptemplate.md) into each [PodGroup](/entity/podgroup.md) it creates, making the PodGroup self-contained. Changes to the Workload's templates only affect newly created PodGroups and do not affect existing ones. For standalone PodGroups created without a Workload, the [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) policy is set directly on `[spec.schedulingPolicy](/definition/podgroup_scheduling_policy.md)` on the PodGroup itself.
