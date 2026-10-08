---
type: Definition
title: Background Cascading Deletion
description: In background cascading deletion, the Kubernetes API server deletes the
  owner object immediately, and the garbage collector controller cleans up dependent
  objects in the background, with finalizers potentially delaying deletion until cleanup
  tasks are complete.
resource: source://architecture__garbage-collection.md
tags:
- background-deletion
- definition
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- background deletion
---

# Background cascading deletion

In background cascading deletion, the [Kubernetes API server](/definition/kube_apiserver.md) deletes the owner object immediately and the garbage collector controller (custom or default) cleans up the [dependent objects](/definition/owner_and_dependent_objects.md) in the background. If a [finalizer](/definition/what_are_finalizers.md) exists, it ensures that objects are not deleted until all necessary clean-up tasks are completed. By default, Kubernetes uses background cascading deletion unless you manually use [foreground deletion](/procedure/cascading_deletion_types.md) or choose to orphan the dependent objects.
