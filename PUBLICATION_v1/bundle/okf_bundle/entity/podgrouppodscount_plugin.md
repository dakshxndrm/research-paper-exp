---
type: Entity
title: PodGroupPodsCount Plugin
description: Scores candidate placements based on total number of pods in PodGroup.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- plugins
- scoring
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- placement scoring
- pod count
---

The `PodGroupPodsCount` [plugin](/plugin/gangscheduling_plugin.md) implements the `PlacementScorePlugin` interface and scores candidate placements based on the total number of [pods](/definition/kubernetes_cluster_architecture.md) in the [PodGroup](/definition/podgroup.md) that you can successfully schedule.
