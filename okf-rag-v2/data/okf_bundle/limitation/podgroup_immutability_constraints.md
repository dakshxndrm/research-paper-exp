---
type: Limitation
title: PodGroup immutability constraints
description: The spec.schedulingGroup field on a Pod is immutable; a Pod cannot move
  to a different PodGroup once set. A single Workload can contain a maximum of 8 PodGroupTemplates.
resource: source://workloads__podgroup-api__lifecycle.md
tags:
- podgroup
- limitation
- immutability
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- schedulingGroup immutable
- PodGroup move
- PodGroupTemplates limit
---

The [spec.schedulingGroup](/definition/workload_placement_and_podgrouptemplates.md) field on a Pod is immutable. Once set, a Pod cannot move to a different [PodGroup](/entity/podgroup.md). The maximum number of [PodGroupTemplates](/definition/podgrouptemplates.md) in a single Workload is 8.
