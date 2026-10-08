---
type: Definition
title: Container Image Lifecycle GC Parameters
description: The kubelet uses HighThresholdPercent and LowThresholdPercent to trigger
  garbage collection of images, deleting oldest unused images first until disk usage
  drops to the low threshold.
resource: source://architecture__garbage-collection.md
tags:
- image-lifecycle
- gc-parameters
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- image maximum age gc
- disk threshold garbage collection
---

# Container image lifecycle

Kubernetes manages the lifecycle of all images through its image manager, which is part of the [kubelet](/definition/kubelet.md), with the cooperation of cadvisor. The kubelet considers the following disk usage limits when making [garbage collection](/definition/supporting_concepts_garbage_collection.md) decisions:

* HighThresholdPercent
* LowThresholdPercent

Disk usage above the configured HighThresholdPercent value triggers garbage collection, which deletes images in order based on the last time they were used, starting with the oldest first. The kubelet deletes images until disk usage reaches the LowThresholdPercent value.
