---
type: Definition
title: PodGroup template reference
description: An optional field linking the PodGroup back to the PodGroupTemplate in
  the Workload it was created from, useful for observability and tooling.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- api structure
- observability
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- spec.podGroupTemplateRef
- template reference
---

The optional spec.podGroupTemplateRef links the [PodGroup](/entity/podgroup.md) back to the [PodGroupTemplate](/entity/podgrouptemplate.md) in the Workload it was created from. This is useful for observability and tooling.
