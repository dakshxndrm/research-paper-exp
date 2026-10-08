---
type: Communication Service
title: Konnectivity Service
description: Explains the Konnectivity service as a replacement for SSH tunnels, providing
  TCP level proxy for control plane to cluster communication.
resource: source://architecture__control-plane-node-communication.md
tags:
- communication
- security
- replacement
- proxy
- tcp
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Konnectivity server
- Konnectivity agents
- control plane to cluster communication
---

As a replacement to the [SSH tunnels](/communication_method/ssh_tunnels_for_control_plane.md), the Konnectivity [service](/entity/kubernetes_service.md) provides TCP level [proxy](/entity/kube_proxy.md) for the [control plane](/definition/kubernetes_cluster_architecture.md) to cluster communication. The Konnectivity service consists of two parts: the Konnectivity server in the control plane network and the Konnectivity agents in the nodes network. The Konnectivity agents initiate connections to the Konnectivity server and maintain the network connections. After enabling the Konnectivity service, all control plane to nodes traffic goes through these connections. Users can follow the Konnectivity service task to set up the Konnectivity service in their cluster.
