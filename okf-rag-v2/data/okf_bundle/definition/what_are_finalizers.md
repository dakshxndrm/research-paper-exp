---
type: Definition
title: What are finalizers
description: Finalizers are metadata fields that control garbage collection of objects
  by alerting controllers to perform cleanup tasks before resource deletion.
resource: source://overview__working-with-objects__finalizers.md
tags:
- garbage-collection
- object-deletion
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- finalizer
- finalizers
---

Finalizers are used to control [garbage collection](/definition/supporting_concepts_garbage_collection.md) of objects by alerting controllers to perform specific cleanup tasks before deleting the target resource. They do not usually specify the code to execute but are typically lists of keys on a specific resource similar to annotations. Kubernetes specifies some finalizers automatically, but users can also specify their own.
