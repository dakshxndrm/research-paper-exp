---
type: Metric
title: Pod Count
description: Scores candidate placements based on total number of pods in PodGroup.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- metrics
- scoring
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- placement scoring
---

The [pod count](/entity/podgrouppodscount_plugin.md) is calculated by the `PodGroupPodsCount` [plugin](/plugin/gangscheduling_plugin.md) and scores candidate placements based on the total number of [pods](/definition/kubernetes_cluster_architecture.md) in the [PodGroup](/definition/podgroup.md) that you can successfully schedule.
