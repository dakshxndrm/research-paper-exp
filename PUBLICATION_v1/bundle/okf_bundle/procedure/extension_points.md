---
type: Procedure
title: Extension Points
description: Points in the scheduling process where plugins can be used to extend
  functionality.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- plugin points
- scheduler extension
---

The scheduler uses extension points such as `PlacementGeneratePlugin` and `PlacementScorePlugin` to find optimal placements for a [PodGroup](/definition/podgroup.md).
