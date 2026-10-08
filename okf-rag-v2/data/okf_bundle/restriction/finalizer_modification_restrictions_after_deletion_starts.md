---
type: Restriction
title: Finalizer modification restrictions after deletion starts
description: Once deletion is requested, existing finalizers can be removed but new
  ones cannot be added, and deletionTimestamp cannot be modified.
resource: source://overview__working-with-objects__finalizers.md
tags:
- deletion-restrictions
- api-behavior
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cannot add finalizer after deletion
- cannot modify deletionTimestamp
- finalizer removal only after deletion starts
---

When you [DELETE](/operations/kubectl_resource_management_operations.md) an object, Kubernetes adds the deletion timestamp and immediately starts to restrict changes to the `.metadata.[finalizers](/definition/what_are_finalizers.md)` field for the object that is now pending deletion. You can remove existing finalizers (deleting an entry from the `finalizers` list) but you cannot add a new finalizer. You also cannot modify the `deletionTimestamp` for an object once it is set.
