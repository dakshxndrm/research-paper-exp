---
type: Definition
title: Foreground and Orphan Cascading Deletion
description: What foreground and orphan cascading deletion are in Kubernetes.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- foreground
- orphan
---

In [foreground deletion](/procedure/foreground_cascading_deletion_process.md), the [controller](/pattern/kubernetes_controller_pattern.md) must [delete](/procedure/deleting_resources_in_kubernetes.md) dependent resources that also have `[ownerReferences](/procedure/configuring_owner_relationships_manually.md).blockOwnerDeletion=true` before it deletes the owner. If you specify an orphan deletion policy, [Kubernetes](/policy/garbage_collection_in_kubernetes.md) adds the `orphan` [finalizer](/procedure/using_finalizers_in_kubernetes.md) so that the controller ignores dependent resources after it deletes the owner object.
