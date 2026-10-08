---
type: Procedure
title: Deleting Resources in Kubernetes
description: How resources are deleted in Kubernetes.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- delete
- kubernetes
---

In [foreground deletion](/procedure/foreground_cascading_deletion_process.md), it adds the `[foreground](/definition/foreground_and_orphan_cascading_deletion.md)` [finalizer](/procedure/using_finalizers_in_kubernetes.md) so that the [controller](/pattern/kubernetes_controller_pattern.md) must delete dependent resources that also have `[ownerReferences](/procedure/configuring_owner_relationships_manually.md).blockOwnerDeletion=true` before it deletes the owner.
