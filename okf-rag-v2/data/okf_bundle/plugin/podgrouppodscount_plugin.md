---
type: Plugin
title: PodGroupPodsCount Plugin
description: Scores candidate placements based on the total number of pods in the
  PodGroup that can be successfully scheduled.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- plugin
- scoring
- pods
- podgroup
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PodGroupPodsCount
- pods count
- scheduling pods
---

PodGroupPodsCount: Implements the PlacementScorePlugin interface. It scores candidate placements based on the total number of pods in the [PodGroup](/entity/podgroup.md) that you can successfully schedule.
