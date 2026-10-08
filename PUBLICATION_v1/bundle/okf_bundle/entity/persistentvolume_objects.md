---
type: Entity
title: PersistentVolume Objects
description: How PersistentVolume objects are handled by finalizers.
resource: source://overview__working-with-objects__finalizers.md
tags:
- kubernetes
- finalizers
- persistent volumes
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- pv-protection
- persistent volumes
---

A common example of a finalizer is `[kubernetes.io/pv-protection](/procedure/using_finalizers_in_kubernetes.md)`, which prevents accidental deletion of `[PersistentVolume](/metric/terminating_status_in_persistentvolumes.md)` objects.
