---
type: Metric
title: Terminating Status in PersistentVolumes
description: What happens when a PersistentVolume is deleted in Kubernetes.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- terminating
- PersistentVolume
---

The volume remains in the `Terminating` status until [Kubernetes](/policy/garbage_collection_in_kubernetes.md) clears the [finalizer](/procedure/using_finalizers_in_kubernetes.md), which only happens after the `PersistentVolume` is no longer bound to a Pod.
