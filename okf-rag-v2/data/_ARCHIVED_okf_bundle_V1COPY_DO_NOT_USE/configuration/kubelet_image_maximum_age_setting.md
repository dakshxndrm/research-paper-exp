---
type: Configuration
title: Kubelet Image Maximum Age Setting
description: Details the `imageMaximumGCAge` setting for configuring the maximum time
  an unused local image can persist, regardless of disk usage.
resource: source://architecture__garbage-collection.md
tags:
- kubelet
- images
- garbage collection
- configuration
- age
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- imageMaximumGCAge
- maximum time a local image can be unused for
- image age garbage collection
---

You can specify the maximum time a local image can remain unused, irrespective of disk usage. This is a [kubelet](/definition/kubernetes_node_components_overview.md) setting configured for each [node](/entity/node.md) by setting a value for the `imageMaximumGCAge` field in the kubelet configuration file.

The value is specified as a [Kubernetes](/policy/garbage_collection_in_kubernetes.md) duration, for example, `12h45m` for 12 hours and 45 minutes.

This feature does not track image usage across kubelet restarts. If the kubelet restarts, the tracked image age is reset, causing the kubelet to wait the full `imageMaximumGCAge` duration before qualifying images for [garbage collection](/concept/garbage_collection.md) based on their age.
