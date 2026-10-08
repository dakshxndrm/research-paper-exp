---
type: Definition
title: kubelet
description: The primary agent that runs on each node and ensures that containers
  are running in a pod.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- node
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- node agent
- Kubernetes agent
---

kubelet is the primary agent that runs on each node. It ensures that containers are running in a pod and communicates with the [control plane](/definition/control_plane_components.md) to receive instructions about what containers should be running.
