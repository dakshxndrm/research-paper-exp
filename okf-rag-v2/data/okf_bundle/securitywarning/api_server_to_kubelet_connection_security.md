---
type: SecurityWarning
title: API Server to Kubelet Connection Security
description: Default connections from the API server to the kubelet are unsafe over
  untrusted networks because the API server does not verify the kubelet's serving
  certificate, making them subject to man-in-the-middle attacks.
resource: source://architecture__control-plane-node-communication.md
tags:
- security
- kubelet
- tls
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kubelet connection
- logs fetching
- port-forwarding
- kubectl attach
---

The connections from the [API server](/definition/kube_apiserver.md) to the [kubelet](/definition/kubelet.md) are used for fetching logs for pods, attaching (usually through `[kubectl](/definition/kubectl_command_line_tool.md)`) to running pods, and providing the kubelet's port-forwarding functionality. These connections terminate at the kubelet's HTTPS endpoint. By default, the API server does not verify the kubelet's serving certificate, which makes the connection subject to man-in-the-middle attacks and **unsafe** to run over untrusted and/or public networks. To verify this connection, use the `--kubelet-certificate-authority` flag to provide the API server with a root certificate bundle to use to verify the kubelet's serving certificate. If that is not possible, use [SSH tunneling](/procedure/ssh_tunnels_for_control_plane_to_node_communication.md) between the API server and kubelet if required to avoid connecting over an untrusted or public network. Finally, Kubelet [authentication](/authentication/kubectl_authentication_methods.md) and/or authorization should be enabled to secure the kubelet API.
