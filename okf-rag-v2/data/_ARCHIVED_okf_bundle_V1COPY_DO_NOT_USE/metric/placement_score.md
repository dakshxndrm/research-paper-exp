---
type: Metric
title: Placement Score
description: Scores placements based on resource utilization within a placement.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- metrics
- scoring
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- placement scoring
- resource fit
---

The placement score is calculated by the `NodeResourcesFit` [plugin](/plugin/gangscheduling_plugin.md) and scores placements based on the allocation ratio across all [nodes](/definition/kubernetes_cluster_architecture.md) within the placement.
