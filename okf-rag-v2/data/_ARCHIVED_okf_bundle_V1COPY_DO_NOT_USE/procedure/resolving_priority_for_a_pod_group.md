---
type: Procedure
title: Resolving Priority for a Pod Group
description: How the priority admission controller resolves the priority.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- resolving pod group priority
- pod group priority resolution
---

The [priority admission controller](/policy/priority_admission_controller.md) checks the specification and resolves the priority of the [PodGroup](/definition/podgroup.md) to 1000000.
