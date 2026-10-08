---
type: Entity
title: TopologyPlacement Plugin
description: Generates candidate placements by grouping nodes based on topology key.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- plugins
- placement
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- placement generation
- topology placement
---

The `TopologyPlacement` [plugin](/plugin/gangscheduling_plugin.md) implements the `PlacementGeneratePlugin` interface and generates candidate placements by grouping [nodes](/definition/kubernetes_cluster_architecture.md) based on the distinct values of the requested topology `key` (defined in the [PodGroup](/definition/podgroup.md)).
