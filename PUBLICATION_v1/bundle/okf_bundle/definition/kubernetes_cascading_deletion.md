---
type: Definition
title: Kubernetes Cascading Deletion
description: Defines cascading deletion as the process where Kubernetes automatically
  deletes an object's dependents when the owner is deleted.
resource: source://architecture__garbage-collection.md
tags:
- deletion
- cascading
- owner references
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- cascading deletion
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) checks for and deletes objects that no longer have [owner references](/definition/kubernetes_owner_references.md), such as [pods](/definition/kubernetes_cluster_architecture.md) left behind when a ReplicaSet is deleted. When an object is deleted, you can control whether Kubernetes automatically deletes its dependents through a [process](/concept/pod_definition.md) called *cascading deletion*. There are two types of cascading deletion:

*   [Foreground cascading deletion](/procedure/foreground_cascading_deletion_process.md)
*   [Background cascading deletion](/procedure/background_cascading_deletion_process.md)

Kubernetes finalizers can also be used to control how and when [garbage collection](/concept/garbage_collection.md) deletes resources with owner references.
