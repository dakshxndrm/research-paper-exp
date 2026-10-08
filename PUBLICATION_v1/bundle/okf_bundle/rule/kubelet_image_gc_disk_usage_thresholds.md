---
type: Rule
title: Kubelet Image GC Disk Usage Thresholds
description: Explains how the kubelet's image manager uses disk usage thresholds to
  trigger and manage garbage collection of container images.
resource: source://architecture__garbage-collection.md
tags:
- kubelet
- images
- garbage collection
- disk usage
- thresholds
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- image manager
- image garbage collection
- HighThresholdPercent
- LowThresholdPercent
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) manages the [lifecycle](/policy/podgroup_ownership_and_lifecycle.md) of all images through its *image manager*, which is part of the [kubelet](/definition/kubernetes_node_components_overview.md), in cooperation with cadvisor. The kubelet considers the following disk usage limits when making [garbage collection](/concept/garbage_collection.md) decisions:

*   `HighThresholdPercent`
*   `LowThresholdPercent`

Disk usage exceeding the configured `HighThresholdPercent` value triggers [garbage collection](/policy/finalizer_purpose.md). This [process](/concept/pod_definition.md) deletes images in order based on their last usage time, starting with the oldest, until disk usage reaches the `LowThresholdPercent` value.
