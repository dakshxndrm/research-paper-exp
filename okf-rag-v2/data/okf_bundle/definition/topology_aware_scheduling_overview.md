---
type: Definition
title: Topology-Aware Scheduling Overview
description: Topology-Aware Scheduling (TAS) is a placement scheduling algorithm that
  finds optimal placement for PodGroups, guaranteeing all pods are collocated within
  the same topology domain.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- scheduling
- topology
- placement
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Topology-Aware Scheduling
- topology scheduling
---

Topology-Aware [Scheduling](/scheduling/runtimeclass_scheduling_constraints.md) (TAS) is a [placement scheduling algorithm](/algorithm/placement_scheduling_algorithm.md) that allows finding the optimal placement for the considered [PodGroup](/entity/podgroup.md), guaranteeing that all pods will be collocated within the same [topology domain](/definition/topology_constraint_definition.md). Users can adapt TAS to their specific needs by changing TAS [plugins](/extensibility/kubectl_plugins.md) configuration.
