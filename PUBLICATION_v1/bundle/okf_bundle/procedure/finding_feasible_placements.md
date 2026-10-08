---
type: Procedure
title: Finding Feasible Placements
description: The process of finding valid Node placements for the Pods in a PodGroup.
resource: source://scheduling-eviction__podgroup-scheduling.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- placement search
- feasibility check
---

The scheduler runs the [PodGroup](/definition/podgroup.md) [scheduling algorithm](/procedure/understanding_the_gang_scheduling_algorithm.md) to find valid [Node](/entity/node.md) placements for the [Pods](/definition/kubernetes_cluster_architecture.md) in the group.
