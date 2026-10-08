---
type: Definition
title: PodGroup Scheduling Limitations
description: Constraints regarding Pod sorting, group heterogeneity, and scheduler
  name consistency that affect placement feasibility.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- scheduling
- limitations
- constraints
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- limitations
- scheduling constraints
- algorithm limitations
---

The [PodGroup scheduling algorithm](/algorithm/podgroup_scheduling_algorithm.md) relies on specific Pod sorting and may fail to find a valid placement that could be discovered with different processing order. For homogeneous Pod groups with identical requirements and no inter-Pod dependencies, a placement is expected to be found if one exists. For heterogeneous Pod groups or groups with inter-Pod dependencies, finding a valid placement is not guaranteed. For Pod groups with intra-group dependencies, such as schedulability of one Pod depending on another via affinity, the algorithm may fail regardless of [cluster state](/concept/desired_versus_current_state.md) due to deterministic processing order. Additionally, for consistent behavior, all Pods belonging to a single [PodGroup](/entity/podgroup.md) must share the same `.spec.schedulerName`.
