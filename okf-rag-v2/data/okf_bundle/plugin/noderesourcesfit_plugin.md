---
type: Plugin
title: NodeResourcesFit Plugin
description: Scores placements based on allocation ratio across all nodes within the
  placement using MostAllocated strategy.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- plugin
- scoring
- resources
- bin-packing
- allocation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- NodeResourcesFit
- resources fit
- bin-packing
- allocation ratio
---

NodeResourcesFit: Extended to implement the PlacementScorePlugin interface. Following similar logic to standard pod bin-packing, it scores placements based on the allocation ratio across all nodes within the placement. It uses the MostAllocated strategy to maximize resource utilization within a placement, and it inherits [resource weights](/configuration/customizing_plugin_weights.md) from the standard pod-by-pod plugin settings.
