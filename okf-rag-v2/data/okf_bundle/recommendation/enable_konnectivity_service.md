---
type: Recommendation
title: Enable Konnectivity Service
description: Replace deprecated SSH tunnels with the Konnectivity service for secure
  control plane to node communication by deploying Konnectivity server in the control
  plane and agents on nodes.
resource: source://architecture__control-plane-node-communication.md
tags:
- konnectivity
- replacement
- setup
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Konnectivity enable
- service setup
---

As a replacement to the SSH tunnels, the [Konnectivity](/procedure/konnectivity_service_for_control_plane_to_node_communication.md) [service](/component/service_load_balancing.md) provides TCP level proxy for the [control plane](/definition/control_plane_components.md) to cluster communication. The Konnectivity service consists of two parts: the Konnectivity server in the control plane network and the Konnectivity agents in the nodes network. The Konnectivity agents initiate connections to the Konnectivity server and maintain the network connections. After enabling the Konnectivity service, all control plane to nodes traffic goes through these connections. Follow the Konnectivity service task to set up the Konnectivity service in your cluster.
