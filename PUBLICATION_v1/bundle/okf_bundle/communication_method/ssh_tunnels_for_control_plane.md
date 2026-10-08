---
type: Communication Method
title: SSH Tunnels for Control Plane
description: Describes the deprecated SSH tunneling method used to protect control
  plane to node communication paths.
resource: source://architecture__control-plane-node-communication.md
tags:
- communication
- security
- deprecated
- ssh
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- SSH tunnels
- SSH tunneling
- SSH server listening on port 22
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) supports SSH tunnels to protect the [control plane](/definition/kubernetes_cluster_architecture.md) to nodes communication paths. In this configuration, the [API server](/policy/api_server_behavior_in_kubernetes.md) initiates an SSH tunnel to each [node](/entity/node.md) in the cluster, connecting to the SSH server listening on port 22. All traffic destined for a [kubelet](/definition/kubernetes_node_components_overview.md), [node](/entity/worker_node.md), pod, or [service](/entity/kubernetes_service.md) is passed through the tunnel, which ensures that the traffic is not exposed outside of the network in which the nodes are running. SSH tunnels are currently deprecated and should not be used unless specifically required, as the [Konnectivity service](/communication_service/konnectivity_service.md) is a replacement for this communication channel.
