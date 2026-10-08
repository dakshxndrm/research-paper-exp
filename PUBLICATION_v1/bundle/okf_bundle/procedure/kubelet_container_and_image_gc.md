---
type: Procedure
title: Kubelet Container and Image GC
description: Describes how the kubelet performs garbage collection for unused containers
  and images, including its frequency and configuration method.
resource: source://architecture__garbage-collection.md
tags:
- kubelet
- garbage collection
- containers
- images
- configuration
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kubelet performs garbage collection
- unused containers garbage collection
- unused images garbage collection
- KubeletConfiguration
---

The [kubelet](/definition/kubernetes_node_components_overview.md) performs [garbage collection](/concept/garbage_collection.md) on unused images every five minutes and on unused containers every minute. It is recommended to avoid using external [garbage collection](/policy/finalizer_purpose.md) tools, as these can disrupt kubelet behavior and remove containers that should exist.

To configure options for unused container and [image garbage collection](/rule/kubelet_image_gc_disk_usage_thresholds.md), the kubelet can be tuned using a configuration file, specifically by changing parameters related to garbage collection within the `KubeletConfiguration` [resource type](/definition/api_group_resource_type_namespace_and_name.md).
