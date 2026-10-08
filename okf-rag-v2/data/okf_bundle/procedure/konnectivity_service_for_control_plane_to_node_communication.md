---
type: Procedure
title: Konnectivity Service for Control Plane to Node Communication
description: The Konnectivity service provides a TCP level proxy for control plane
  to cluster communication, consisting of a server in the control plane and agents
  on nodes, replacing deprecated SSH tunnels.
resource: source://architecture__control-plane-node-communication.md
tags:
- konnectivity
- proxy
- communication
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Konnectivity
- TCP proxy
- control plane traffic
---

As a replacement to the SSH tunnels, the Konnectivity [service](/component/service_load_balancing.md) provides TCP level proxy for the [control plane](/definition/control_plane_components.md) to cluster communication. The Konnectivity service consists of two parts: the Konnectivity server in the control plane network and the Konnectivity agents in the nodes network. The Konnectivity agents initiate connections to the Konnectivity server and maintain the network connections. After enabling the Konnectivity service, all control plane to nodes traffic goes through these connections. Follow the Konnectivity service task to set up the Konnectivity service in your cluster.
