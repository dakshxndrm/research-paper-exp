---
type: Entity
title: PodGroupTemplate
description: A distinct component of a workload that defines scheduling policies for
  groups of Pods.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- entity
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- template
- scheduling policy
---

Each entry in `[podGroupTemplates](/template/podgrouptemplates.md)` must have a unique `[name](/definition/api_group_resource_type_namespace_and_name.md)` and a [scheduling policy](/concept/workload_placement.md) (`basic` or `gang`).
