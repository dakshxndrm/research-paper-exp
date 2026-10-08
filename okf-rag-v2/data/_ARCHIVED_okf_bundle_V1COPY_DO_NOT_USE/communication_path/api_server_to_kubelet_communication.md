---
type: Communication Path
title: API Server to Kubelet Communication
description: Details the communication path from the API server to the kubelet process
  on each node, its uses, and security considerations.
resource: source://architecture__control-plane-node-communication.md
tags:
- communication
- api server
- kubelet
- security
- logs
- attach
- port-forwarding
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- API server to kubelet
- connections from the API server to the kubelet
---

The connections from the [API server](/policy/api_server_behavior_in_kubernetes.md) to the [kubelet](/definition/kubernetes_node_components_overview.md) [process](/concept/pod_definition.md), which runs on each [node](/entity/node.md) in the cluster, are used for fetching logs for [pods](/definition/kubernetes_cluster_architecture.md), attaching (usually through `[kubectl](/tool/kubectl_command_line_tool.md)`) to running pods, and providing the kubelet's port-forwarding functionality. These connections terminate at the kubelet's HTTPS endpoint. By default, the API server does not verify the kubelet's serving certificate, which makes the connection subject to man-in-the-middle attacks and unsafe to run over untrusted and/or public networks. To verify this connection, the `--kubelet-certificate-authority` flag can be used to provide the API server with a root certificate bundle. If that is not possible, [SSH tunneling](/communication_method/ssh_tunnels_for_control_plane.md) between the API server and kubelet can be used to avoid connecting over an untrusted or public network. Kubelet [authentication](/authentication/authentication_with_kubeconfig_file.md) and/or [authorization](/definition/kubernetes_authentication_and_authorization.md) should also be enabled to secure the kubelet API.
