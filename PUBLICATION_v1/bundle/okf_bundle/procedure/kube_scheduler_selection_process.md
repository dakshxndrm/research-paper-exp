---
type: Procedure
title: kube-scheduler Selection Process
description: The steps involved in selecting a node for a pod using kube-scheduler.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- node selection
- pod placement
---

[kube-scheduler](/policy/kubernetes_scheduling_overview.md) selects an optimal [node](/entity/node.md) to run newly created or not yet scheduled (unscheduled) [pods](/definition/kubernetes_cluster_architecture.md). The [process](/concept/pod_definition.md) involves filtering and scoring steps.
