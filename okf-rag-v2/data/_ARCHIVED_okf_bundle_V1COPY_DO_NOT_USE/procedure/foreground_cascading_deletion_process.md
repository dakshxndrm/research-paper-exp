---
type: Procedure
title: Foreground Cascading Deletion Process
description: Details the steps and states involved when an owner object is deleted
  using foreground cascading deletion.
resource: source://architecture__garbage-collection.md
tags:
- deletion
- cascading deletion
- foreground
- finalizers
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- foreground cascading deletion
- foreground deletion
- deletion in progress state
---

In [foreground](/definition/foreground_and_orphan_cascading_deletion.md) [cascading deletion](/definition/kubernetes_cascading_deletion.md), the owner object being deleted first enters a *deletion in progress* state. During this state:

*   The [Kubernetes API](/entity/kubernetes_api.md) server sets the object's `metadata.deletionTimestamp` field to the time it was marked for deletion.
*   The [Kubernetes](/policy/garbage_collection_in_kubernetes.md) [API server](/policy/api_server_behavior_in_kubernetes.md) also sets the `[metadata.finalizers](/procedure/specifying_finalizers_in_a_manifest_file.md)` field to `foregroundDeletion`.
*   The object remains visible through the Kubernetes API until the [deletion process](/process/how_finalizers_work.md) is complete.

After the owner object enters this state, the [controller](/pattern/kubernetes_controller_pattern.md) deletes all known dependents. Once all dependent objects are deleted, the controller deletes the owner object, which then becomes no longer visible in the Kubernetes API.

During foreground cascading deletion, only dependents with the `[ownerReference](/metric/invalid_owner_references.md).blockOwnerDeletion=true` field that are present in the [garbage collection](/concept/garbage_collection.md) controller cache will block owner deletion. The cache may not contain objects whose [resource type](/definition/api_group_resource_type_namespace_and_name.md) cannot be listed/watched successfully, or objects created concurrently with the owner's deletion.
