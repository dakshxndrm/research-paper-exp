---
type: Procedure
title: SSH Tunnels for Control Plane to Node Communication
description: Kubernetes supports SSH tunnels to secure control plane to node traffic
  by routing all traffic through an SSH server on port 22, preventing exposure outside
  the node network.
resource: source://architecture__control-plane-node-communication.md
tags:
- security
- ssh
- tunnel
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- SSH tunneling
- secure tunnel
- Konnectivity replacement
---

Kubernetes supports SSH tunnels to protect the [control plane](/definition/control_plane_components.md) to nodes communication paths. In this configuration, the [API server](/definition/kube_apiserver.md) initiates an SSH tunnel to each node in the cluster (connecting to the SSH server listening on port 22) and passes all traffic destined for a [kubelet](/definition/kubelet.md), node, pod, or [service](/component/service_load_balancing.md) through the tunnel. This tunnel ensures that the traffic is not exposed outside of the network in which the nodes are running. SSH tunnels are currently deprecated, so you shouldn't opt to use them unless you know what you are doing. The [Konnectivity](/procedure/konnectivity_service_for_control_plane_to_node_communication.md) service is a replacement for this communication channel.
