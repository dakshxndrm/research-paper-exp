---
type: Procedure
title: Customizing Plugin Weights
description: Users can adjust weights for plugins to balance bin-packing logic and
  scheduling.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- configuration
- plugins
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- plugin weight configuration
- bin-packing resource weights
---

By default, the `NodeResourcesFit` and `PodGroupPodsCount` plugins are configured with equal weights (both default to 1) to maintain a good balance between bin-packing logic and [scheduling](/concept/scheduling.md) as many [pods](/definition/kubernetes_cluster_architecture.md) as possible. Users can adjust these weights in their [KubeSchedulerConfiguration](/entity/kubeschedulerconfiguration.md).
