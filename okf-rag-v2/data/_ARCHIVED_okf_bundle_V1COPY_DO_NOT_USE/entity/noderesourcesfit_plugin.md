---
type: Entity
title: NodeResourcesFit Plugin
description: Scores placements based on resource utilization within a placement.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- plugins
- scoring
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- placement scoring
- resource fit
---

The `NodeResourcesFit` [plugin](/plugin/gangscheduling_plugin.md) implements the `PlacementScorePlugin` interface and scores placements based on the allocation ratio across all [nodes](/definition/kubernetes_cluster_architecture.md) within the placement. It uses the `MostAllocated` strategy to maximize [resource](/resource/cluster_resources.md) utilization within a placement.
