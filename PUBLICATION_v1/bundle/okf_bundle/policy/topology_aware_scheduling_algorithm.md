---
type: Policy
title: Topology-Aware Scheduling Algorithm
description: A placement scheduling algorithm that finds optimal pod placement.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- scheduling
- placement
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Topology-Aware Placement
---

Topology-Aware [Workload](/entity/workload.md) [Scheduling](/concept/scheduling.md) uses a [placement scheduling algorithm](/procedure/placement_scheduling_algorithm.md) called [Topology-Aware Scheduling](/policy/topology_aware_scheduling.md) (TAS) to find the optimal placement for PodGroups, guaranteeing that all [pods](/definition/kubernetes_cluster_architecture.md) will be collocated within the same [topology domain](/entity/topology_domain.md).
