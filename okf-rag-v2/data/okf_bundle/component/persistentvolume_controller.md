---
type: Component
title: PersistentVolume Controller
description: The PersistentVolume controller manages volume attachment and detachment
  for stateful workloads, enabling recovery when nodes fail.
resource: source://architecture__self-healing.md
tags:
- kubernetes
- component
- persistentvolume
- storage
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- PersistentVolume
- volume management
- storage controller
---

- **Persistent [storage recovery](/definition/persistentvolume_recovery.md):** If a node is running a Pod with a PersistentVolume (PV) attached, and the node fails, Kubernetes can reattach the volume to a new Pod on a different node.
