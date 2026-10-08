---
type: Definition
title: Controller-managed vs user-managed PodGroups
description: Workload controllers automatically create PodGroups with determined names;
  users can create PodGroups directly for full control over naming and lifecycle.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- controller
- user-managed
- naming
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- controller-managed PodGroups
- user-managed PodGroups
- PodGroup naming
---

In most cases, workload controllers (for example, Job) [create](/operations/kubectl_resource_management_operations.md) PodGroups automatically (controller-managed). The controller determines the [podGroupName](/concept/pod_reference_to_podgroup.md) for each Pod at creation time. If you need more control over naming and lifecycle, you can create [PodGroup](/entity/podgroup.md) objects directly and set [spec.schedulingGroup](/definition/workload_placement_and_podgrouptemplates.md).podGroupName in your Pod templates yourself (user-managed). This gives you full control over [PodGroup creation](/procedure/creating_a_podgroup.md) and naming.
