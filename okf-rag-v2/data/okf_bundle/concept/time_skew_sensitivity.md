---
type: Concept
title: Time skew sensitivity
description: How clock accuracy affects the TTL-after-finished controller behavior.
resource: source://workloads__controllers__ttlafterfinished.md
tags:
- time skew
- controller reliability
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- time skew
- clock accuracy
- timestamp sensitivity
---

The [TTL-after-finished controller](/definition/ttl_after_finished_controller.md) uses timestamps stored in Kubernetes Jobs to determine whether the TTL has expired. This feature is sensitive to time skew in the cluster, which may cause the [control plane](/definition/control_plane_components.md) to clean up Job objects at the wrong time. While clocks are not always perfectly correct, the difference should be very small. Users should be aware of this risk when setting a non-zero TTL.
