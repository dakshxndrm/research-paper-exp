---
type: Definition
title: Foreground Cascading Deletion
description: In foreground cascading deletion, the owner object enters a deletion
  in progress state, has its deletionTimestamp and finalizers set, and remains visible
  in the API until all dependents and the owner itself are deleted.
resource: source://architecture__garbage-collection.md
tags:
- foreground-deletion
- definition
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- foreground deletion
- deletion in progress
---

# Foreground [cascading deletion](/procedure/cascading_deletion_types.md)

In foreground cascading deletion, the owner object you're deleting first enters a deletion in progress state. In this state, the following happens to the owner object:

* The [Kubernetes API server](/definition/kube_apiserver.md) sets the object's metadata.deletionTimestamp field to the time the object was marked for deletion.
* The Kubernetes API server also sets the metadata.[finalizers](/definition/what_are_finalizers.md) field to foregroundDeletion.
* The object remains visible through the Kubernetes API until the [deletion process](/procedure/how_finalizers_work_during_deletion.md) is complete.

After the owner object enters the deletion in progress state, the controller deletes dependents it knows about. After deleting all the [dependent objects](/definition/owner_and_dependent_objects.md) it knows about, the controller deletes the owner object. At this point, the object is no longer visible in the Kubernetes API.

During foreground cascading deletion, the only dependents that block owner deletion are those that have the ownerReference.[blockOwnerDeletion](/configuration/blockownerdeletion_field.md)=true field and are in the [garbage collection](/definition/supporting_concepts_garbage_collection.md) controller cache. The garbage collection controller cache may not contain objects whose resource type cannot be listed / watched successfully, or objects that are created concurrent with deletion of an owner object.
