---
type: Policy
title: PodGroup Ownership and Lifecycle
description: Ownership and lifecycle of PodGroups in a workload.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- workload
- controller
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- ownership
- lifecycle
---

A `[PodGroup](/definition/podgroup.md)` is owned by the [workload](/entity/workload.md) [controller](/pattern/kubernetes_controller_pattern.md) that created it via standard `[ownerReferences](/procedure/configuring_owner_relationships_manually.md)`. When the owning object is deleted, `PodGroups` are automatically garbage collected.
