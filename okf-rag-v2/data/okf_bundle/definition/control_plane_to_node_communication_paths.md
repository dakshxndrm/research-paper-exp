---
type: Definition
title: Control Plane to Node Communication Paths
description: 'The control plane communicates with nodes through two primary paths:
  API server to kubelet for pod management operations, and API server proxy functionality
  for node, pod, and service access.'
resource: source://architecture__control-plane-node-communication.md
tags:
- communication
- control plane
- kubelet
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- node communication paths
- API server paths
---

There are two primary communication paths from the [control plane](/definition/control_plane_components.md) (the [API server](/definition/kube_apiserver.md)) to the nodes. The first is from the API server to the [kubelet](/definition/kubelet.md) process which runs on each node in the cluster. The second is from the API server to any node, pod, or [service](/component/service_load_balancing.md) through the API server's _proxy_ functionality.
