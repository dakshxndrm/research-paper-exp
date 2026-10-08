---
type: Definition
title: PersistentVolume Recovery
description: When a node fails, Kubernetes can reattach PersistentVolumes to new Pods
  on different nodes to recover stateful workloads.
resource: source://architecture__self-healing.md
tags:
- kubernetes
- definition
- persistentvolume
- recovery
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- volume recovery
- storage recovery
---

- **Persistent storage recovery:** If a node is running a Pod with a [PersistentVolume](/component/persistentvolume_controller.md) (PV) attached, and the node fails, Kubernetes can reattach the volume to a new Pod on a different node.
