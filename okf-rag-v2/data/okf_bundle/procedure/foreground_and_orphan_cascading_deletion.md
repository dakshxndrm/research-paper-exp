---
type: Procedure
title: Foreground and Orphan Cascading Deletion
description: Kubernetes adds the foreground finalizer so controllers must delete dependents
  with blockOwnerDeletion=true before deleting the owner; an orphan deletion policy
  adds the orphan finalizer so controllers ignore dependents after the owner object
  is deleted.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- deletion
- cascading
- finalizer
- orphan
- foreground
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cascading deletion
- foreground deletion
- orphan deletion
- finalizer policy
- deletion policy
---

Kubernetes also adds [finalizers](/definition/what_are_finalizers.md) to an owner resource when you use either foreground or orphan cascading deletion. In [foreground deletion](/procedure/cascading_deletion_types.md), it adds the [foreground finalizer](/finalizer/ownership_and_finalizers.md) so that the controller must [delete](/operations/kubectl_resource_management_operations.md) dependent resources that also have [ownerReferences](/mechanism/owner_references_in_object_specifications.md).[blockOwnerDeletion](/configuration/blockownerdeletion_field.md)=true before it deletes the owner. If you specify an orphan deletion policy, Kubernetes adds the orphan finalizer so that the controller ignores dependent resources after it deletes the owner object.
