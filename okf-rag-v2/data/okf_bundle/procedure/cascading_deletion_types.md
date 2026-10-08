---
type: Procedure
title: Cascading Deletion Types
description: 'Kubernetes supports two cascading deletion modes: foreground, where
  the owner enters deletion progress state before dependents are removed, and background,
  where the owner is deleted immediately and dependents are cleaned up by the garbage
  collector.'
resource: source://architecture__garbage-collection.md
tags:
- cascading-deletion
- procedure
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cascading deletion
- foreground deletion
- background deletion
---

# Cascading deletion

Kubernetes checks for and deletes objects that no longer have [owner references](/definition/owner_references_and_dependents.md), like the pods left behind when you [delete](/operations/kubectl_resource_management_operations.md) a [ReplicaSet](/component/replicaset_and_deployment_controllers.md). When you delete an object, you can control whether Kubernetes deletes the object's dependents automatically, in a process called cascading deletion. There are two types of cascading deletion:

* [Foreground cascading deletion](/definition/foreground_cascading_deletion.md)
* [Background cascading deletion](/definition/background_cascading_deletion.md)

You can also control how and when [garbage collection](/definition/supporting_concepts_garbage_collection.md) deletes resources that have owner references using Kubernetes [finalizers](/definition/what_are_finalizers.md).
