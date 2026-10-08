---
type: Procedure
title: How finalizers work during deletion
description: The API server adds a deletion timestamp and prevents removal until all
  finalizers are cleared, returning a 202 status code.
resource: source://overview__working-with-objects__finalizers.md
tags:
- deletion-procedure
- api-behavior
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- deletion process
- delete with finalizer
- 202 accepted status
---

When a resource is deleted, the [API server](/definition/kube_apiserver.md) adds a `metadata.deletionTimestamp` field and prevents the object from being removed until all items are removed from its `metadata.[finalizers](/definition/what_are_finalizers.md)` field. The API server returns a `202` status code (HTTP "Accepted"). Each time a finalizer condition is satisfied, the controller removes that key from the resource's `finalizers` field. When the `finalizers` field is emptied, the object with a `deletionTimestamp` set is automatically deleted.
