---
type: Policy
title: PodGroup lifecycle and ownership
description: PodGroups are owned by workload controllers and garbage collected when
  the owner is deleted; names must be unique within a namespace and valid DNS subdomains.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- lifecycle
- ownership
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroup lifecycle
- PodGroup ownership
- PodGroup deletion
---

A [PodGroup](/entity/podgroup.md) is scheduled as a unit and protected from premature deletion while its Pods are still running. PodGroups are owned by the [workload controller](/definition/workload_controller.md) that created them via standard [ownerReferences](/mechanism/owner_references_in_object_specifications.md). When the owning object is deleted, PodGroups are automatically garbage collected. PodGroup names must be unique within a namespace and must be valid DNS subdomains.
