---
type: Configuration
title: Customizing Plugin Weights
description: Administrators can adjust NodeResourcesFit and PodGroupPodsCount weights,
  or override NodeResourcesFit resource weights in KubeSchedulerConfiguration.
resource: source://scheduling-eviction__topology-aware-scheduling.md
tags:
- configuration
- weights
- customization
- kubeschedulerconfiguration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- custom weights
- weight adjustment
- KubeSchedulerConfiguration
- resource weights
- plugin configuration
---

You can adjust these weights, or the resource weights in the bin-packing strategy in your KubeSchedulerConfiguration. Here is an example snippet showing how to change the weights for both [plugins](/extensibility/kubectl_plugins.md), and how to override the [NodeResourcesFit](/plugin/noderesourcesfit_plugin.md) resource weights. The latter change will apply both to pod-by-pod and placement scoring algorithms.
