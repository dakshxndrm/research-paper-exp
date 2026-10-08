---
type: Recommendation
title: Secure Communication Configuration
description: To secure API server to kubelet connections, provide a root certificate
  bundle via the `--kubelet-certificate-authority` flag or use SSH tunneling; additionally
  enable kubelet authentication and authorization.
resource: source://architecture__control-plane-node-communication.md
tags:
- security
- configuration
- tls
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- secure configuration
- TLS verification
- kubelet security
---

To verify this connection, use the `--[kubelet](/definition/kubelet.md)-certificate-authority` flag to provide the [API server](/definition/kube_apiserver.md) with a root certificate bundle to use to verify the kubelet's serving certificate. If that is not possible, use [SSH tunneling](/procedure/ssh_tunnels_for_control_plane_to_node_communication.md) between the API server and kubelet if required to avoid connecting over an untrusted or public network. Finally, Kubelet [authentication](/authentication/kubectl_authentication_methods.md) and/or authorization should be enabled to secure the kubelet API.
