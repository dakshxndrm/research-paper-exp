---
type: Procedure
title: Placement Scheduling Algorithm
description: An alternative PodGroup scheduling algorithm that uses scheduling plugins
  to find optimal placements.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- placement algorithm
- plugin-based placement
---

The Placement [scheduling algorithm](/procedure/understanding_the_gang_scheduling_algorithm.md) proceeds in three main phases for a given [PodGroup](/definition/podgroup.md): candidate [placement generation](/entity/topologyplacement_plugin.md), pod-level filtering and [feasibility check](/procedure/finding_feasible_placements.md), and [placement scoring](/entity/noderesourcesfit_plugin.md) and selection.
