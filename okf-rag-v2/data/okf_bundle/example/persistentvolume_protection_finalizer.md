---
type: Example
title: PersistentVolume protection finalizer
description: The pv-protection finalizer prevents accidental deletion of PersistentVolume
  objects currently in use.
resource: source://overview__working-with-objects__finalizers.md
tags:
- builtin-finalizer
- storage
- persistentvolume
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kubernetes.io/pv-protection
- pv-protection finalizer
- PersistentVolume deletion protection
- PV protection
---

A common example of a [finalizer](/definition/what_are_finalizers.md) is `kubernetes.io/pv-protection`, which prevents accidental deletion of `[PersistentVolume](/component/persistentvolume_controller.md)` objects. When a `PersistentVolume` object is in use by a Pod, Kubernetes adds the `pv-protection` finalizer. If you try to [delete](/operations/kubectl_resource_management_operations.md) the `PersistentVolume`, it enters a `Terminating` status, but the controller cannot delete it because the finalizer exists. When the Pod stops using the `PersistentVolume`, Kubernetes clears the `pv-protection` finalizer, and the controller deletes the volume.
