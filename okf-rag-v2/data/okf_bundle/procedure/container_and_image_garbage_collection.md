---
type: Procedure
title: Container and Image Garbage Collection
description: The kubelet performs garbage collection on unused container images every
  five minutes and on unused containers every minute, with configurable thresholds
  and age limits to manage disk usage and container retention.
resource: source://architecture__garbage-collection.md
tags:
- container-gc
- image-gc
- kubelet
- procedure
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- container garbage collection
- image garbage collection
- kubelet garbage collection
---

# [Garbage collection](/definition/supporting_concepts_garbage_collection.md) of unused containers and images

The [kubelet](/definition/kubelet.md) performs garbage collection on unused images every five minutes and on unused containers every minute. You should avoid using external garbage collection tools, as these can break the kubelet behavior and remove containers that should exist.

To configure options for unused container and image garbage collection, tune the kubelet using a configuration file and change the parameters related to garbage collection using the KubeletConfiguration resource type.
