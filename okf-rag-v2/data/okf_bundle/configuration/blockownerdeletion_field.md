---
type: Configuration
title: blockOwnerDeletion Field
description: Dependent objects have an ownerReferences.blockOwnerDeletion field that
  takes a boolean value and controls whether specific dependents can block garbage
  collection from deleting their owner object; Kubernetes automatically sets this
  field to true if a controller sets the ownerReferences field, but it can also be
  set manually.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- blockownerdeletion
- garbage collection
- finalizer
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- blockOwnerDeletion
- block deletion
- garbage collection blocking
- finalizer control
---

[Dependent objects](/definition/owner_and_dependent_objects.md) also have an [ownerReferences](/mechanism/owner_references_in_object_specifications.md).blockOwnerDeletion field that takes a boolean value and controls whether specific dependents can block [garbage collection](/definition/supporting_concepts_garbage_collection.md) from deleting their owner object. Kubernetes automatically sets this field to true if a controller (for example, the [Deployment controller](/component/replicaset_and_deployment_controllers.md)) sets the value of the metadata.ownerReferences field. You can also set the value of the blockOwnerDeletion field manually to control which dependents block garbage collection.
