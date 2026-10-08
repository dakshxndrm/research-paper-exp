---
type: Configuration
title: Default Plugin Weights
description: NodeResourcesFit and PodGroupPodsCount plugins default to equal weights
  of 1 for balanced bin-packing and pod scheduling.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- configuration
- weights
- plugin
- default
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- default weights
- plugin weights
- weight configuration
- equal weights
---

By default, the [NodeResourcesFit](/plugin/noderesourcesfit_plugin.md) and [PodGroupPodsCount](/plugin/podgrouppodscount_plugin.md) [plugins](/extensibility/kubectl_plugins.md) are configured with equal weights (both default to 1) to maintain a good balance between bin-packing logic and [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) as many pods as possible.
