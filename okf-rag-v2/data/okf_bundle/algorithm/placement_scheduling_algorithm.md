---
type: Algorithm
title: Placement Scheduling Algorithm
description: An alternative PodGroup scheduling algorithm that uses plugins to generate,
  filter, and score candidate node placements.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- algorithm
- plugin
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- placement algorithm
- placement scheduling
- plugin-based scheduling
---

The Placement [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) algorithm is an alternative to the default algorithm that uses [scheduling plugins](/configuration/scheduling_profiles.md) to find optimal placements for a [PodGroup](/entity/podgroup.md). It proceeds in three phases: Phase 1, Candidate [placement generation](/plugin/topologyplacement_plugin.md), generates theoretical feasible node subsets for the PodGroup based on [scheduling constraints](/definition/gang_scheduling_constraints.md), executing as the `PlacementGeneratePlugin` [extension](/definition/third_party_workload_resources.md) point. Phase 2, Pod-level filtering and feasibility check, validates each proposed placement using the default [PodGroup scheduling algorithm](/algorithm/podgroup_scheduling_algorithm.md) to determine if the required number of Pods can fit, marking feasible placements accordingly. Phase 3, Placement scoring and selection, scores all feasible placements to select the optimal domain for the PodGroup, executing as the `PlacementScorePlugin` extension point. This algorithm is limited by Pod sorting order and may fail to find valid placements for heterogeneous Pod groups or groups with inter-Pod dependencies, including intra-group dependencies like [affinity rules](/definition/node_selection_mechanisms.md). All Pods in a single PodGroup must share the same `.spec.schedulerName` for consistent behavior.
