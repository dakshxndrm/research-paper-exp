---
type: Policy
title: Disruption Mode Types
description: The two disruption modes supported by the PodGroup.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- PodGroup disruption modes
---

As of 1.36, the `priority` or `disruptionMode` fields of the [PodGroup](/definition/podgroup.md) are only respected by [workload-aware preemption](/policy/workload_aware_preemption_policy.md).

The API supports two disruption modes: `Pod` and `PodGroup`. The default one is `Pod`.
