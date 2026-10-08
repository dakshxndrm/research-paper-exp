---
type: Plugin
title: TopologyPlacement Plugin
description: Generates candidate placements by grouping nodes based on distinct topology
  key values from the PodGroup.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- plugin
- placement
- topology
- generation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- TopologyPlacement
- placement generation
---

The [scheduler](/definition/kube_scheduler.md) includes new and extended in-tree [plugins](/extensibility/kubectl_plugins.md) that implement the TAS [extension](/definition/third_party_workload_resources.md) points: TopologyPlacement: Implements the PlacementGeneratePlugin interface. It generates candidate placements by grouping nodes based on the distinct values of the requested topology key (defined in the [PodGroup](/entity/podgroup.md)).
