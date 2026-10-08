---
type: Procedure
title: Background Cascading Deletion Process
description: Explains how background cascading deletion works, where the owner is
  deleted immediately and dependents are cleaned up later.
resource: source://architecture__garbage-collection.md
tags:
- deletion
- cascading deletion
- background
- finalizers
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- background cascading deletion
- background deletion
---

In background [cascading deletion](/definition/kubernetes_cascading_deletion.md), the [Kubernetes API](/entity/kubernetes_api.md) server immediately deletes the owner object. Subsequently, the garbage collector [controller](/pattern/kubernetes_controller_pattern.md) (custom or default) cleans up the dependent objects in the background. If a [finalizer](/procedure/using_finalizers_in_kubernetes.md) exists, it ensures that objects are not deleted until all necessary clean-up tasks are completed. By default, [Kubernetes](/policy/garbage_collection_in_kubernetes.md) uses background cascading deletion unless [foreground deletion](/procedure/foreground_cascading_deletion_process.md) is manually specified or dependent objects are chosen to be orphaned.
