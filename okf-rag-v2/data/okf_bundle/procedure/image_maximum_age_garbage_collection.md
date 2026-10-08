---
type: Procedure
title: Image Maximum Age Garbage Collection
description: Administrators can set a maximum unused age for local container images
  via the imageMaximumGCAge kubelet configuration field, specifying a Kubernetes duration
  after which unused images qualify for garbage collection regardless of disk usage.
resource: source://architecture__garbage-collection.md
tags:
- image-age-gc
- kubelet-configuration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- image age gc
- maximum image age configuration
---

# [Garbage collection](/definition/supporting_concepts_garbage_collection.md) for unused container images

You can specify the maximum time a local image can be unused for, regardless of disk usage. This is a [kubelet](/definition/kubelet.md) setting that you configure for each node.

To configure the setting, you need to set a value for the imageMaximumGCAge field in the [kubelet configuration](/configuration/configure_ipv4ipv6_dual_stack_cluster_network_assignments.md) file.

The value is specified as a Kubernetes duration. See duration in the glossary for more details.

For example, you can set the configuration field to 12h45m, which means 12 hours and 45 minutes.

This feature does not track image usage across kubelet restarts. If the kubelet is restarted, the tracked image age is reset, causing the kubelet to wait the full imageMaximumGCAge duration before qualifying images for garbage collection based on image age.
