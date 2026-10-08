---
type: Procedure
title: Disrupting a Pod Group
description: How the scheduler treats Pods in a group when in PodGroup mode.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- pod group disruption
---

The `[PodGroup](/definition/podgroup.md)` [mode](/definition/disruption_mode.md) emphasizes "all-or-nothing" semantics for disruption. It instructs the scheduler that all [pods](/definition/kubernetes_cluster_architecture.md) from the PodGroup have to be disrupted together.
