---
type: Entity
title: PodGroupTemplate
description: Defines the PodGroupTemplate resource used to configure scheduling policies
  for workload-created PodGroups.
resource: source://workloads__workload-api__policies.md
tags:
- entity
- workload api
- podgrouptemplate
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup template
- workload template
- template
---

When using the Workload API, [scheduling policies](/configuration/scheduling_policies_configuration.md) are defined inside `[PodGroupTemplates](/definition/podgrouptemplates.md)`. The [workload controller](/definition/workload_controller.md) copies the policy from the template into each [PodGroup](/entity/podgroup.md) it creates, making the PodGroup self-contained.
