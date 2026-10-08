---
type: Procedure
title: Creating a PodGroup from a Workload
description: Describes how a workload controller creates a PodGroup from a template.
resource: source://workloads__workload-api.md
tags:
- kubernetes
- procedure
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- podgroup creation
- template copying
---

When a [workload](/entity/workload.md) [controller](/pattern/kubernetes_controller_pattern.md) creates a `[PodGroup](/definition/podgroup.md)` from one of these templates, it copies the [scheduling policy](/concept/workload_placement.md) into the `PodGroup`'s own spec.
