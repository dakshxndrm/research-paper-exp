---
type: Resource
title: kubernetes.io/pv-protection finalizer function
description: Prevents deletion of PersistentVolume objects that are currently in use
  by Pods.
resource: source://overview__working-with-objects__finalizers.md
tags:
- builtin-finalizer
- persistentvolume
- storage
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- pv protection
- volume protection finalizer
- storage resource protection
---

A common example of a [finalizer](/definition/what_are_finalizers.md) is `[kubernetes.io/pv-protection](/example/persistentvolume_protection_finalizer.md)`, which prevents accidental deletion of `[PersistentVolume](/component/persistentvolume_controller.md)` objects. When a `PersistentVolume` object is in use by a Pod, Kubernetes adds the `pv-protection` finalizer. If you try to [delete](/operations/kubectl_resource_management_operations.md) the `PersistentVolume`, it enters a `Terminating` status, but the controller can't delete it because the finalizer exists. When the Pod stops using the `PersistentVolume`, Kubernetes clears the `pv-protection` finalizer, and the controller deletes the volume.
