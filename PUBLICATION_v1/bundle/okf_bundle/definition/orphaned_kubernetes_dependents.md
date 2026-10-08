---
type: Definition
title: Orphaned Kubernetes Dependents
description: Defines orphaned objects as dependents left behind when their owner object
  is deleted.
resource: source://architecture__garbage-collection.md
tags:
- deletion
- dependents
- orphaned
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- orphan objects
- orphaned dependents
---

When [Kubernetes](/policy/garbage_collection_in_kubernetes.md) deletes an owner object, any dependents left behind are called *[orphan](/definition/foreground_and_orphan_cascading_deletion.md)* objects. By default, Kubernetes deletes dependent objects. This behavior can be overridden to retain dependents.
