---
type: Definition
title: PodGroupTemplate unique name
description: Each PodGroupTemplate entry must have a unique name used to reference
  the template in the PodGroup's spec.podGroupTemplateRef.
resource: source://workloads__workload-api.md
tags:
- api
- naming
- podgrouptemplate
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- template name
- unique name
- PodGroup template reference
---

# [PodGroupTemplate](/entity/podgrouptemplate.md) unique name

Each entry in `[podGroupTemplates](/definition/podgrouptemplates.md)` must have a unique `name` that will be used to reference the template in the `[PodGroup](/entity/podgroup.md)`'s `[spec.podGroupTemplateRef](/definition/podgroup_template_reference.md)`.
