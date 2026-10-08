---
type: Capability
title: Persistent Storage Recovery
description: Explains how Kubernetes can reattach PersistentVolumes to new Pods on
  different nodes after a node failure.
resource: source://architecture__self-healing.md
tags:
- persistentvolume
- pv
- storage
- node
- self-healing
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- PV recovery
- volume reattachment
---

If a [node](/entity/node.md) is running a Pod with a [PersistentVolume](/metric/terminating_status_in_persistentvolumes.md) (PV) attached, and the [node](/entity/worker_node.md) fails, [Kubernetes](/policy/garbage_collection_in_kubernetes.md) can reattach the volume to a new Pod on a different node.
