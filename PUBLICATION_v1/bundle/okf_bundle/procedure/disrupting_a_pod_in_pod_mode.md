---
type: Procedure
title: Disrupting a Pod in Pod Mode
description: How the scheduler treats Pods in a group when in Pod mode.
resource: source://workloads__workload-api__disruption-and-priority.md
tags:
- kubernetes
- workload-api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- disrupting a pod
- pod disruption
---

The `Pod` [mode](/definition/disruption_mode.md) instructs the scheduler to treat all [Pods](/definition/kubernetes_cluster_architecture.md) in the group as separate entities, allowing independent disruption of a single pod from a [PodGroup](/definition/podgroup.md).
