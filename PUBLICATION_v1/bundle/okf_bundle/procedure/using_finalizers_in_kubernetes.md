---
type: Procedure
title: Using Finalizers in Kubernetes
description: How finalizers are used in Kubernetes.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- finalizer
- kubernetes.io/pv-protection
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) also adds finalizers to an owner [resource](/resource/cluster_resources.md) when you use either [foreground](/definition/foreground_and_orphan_cascading_deletion.md) or orphan [cascading deletion](/definition/kubernetes_cascading_deletion.md).
