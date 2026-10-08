---
type: Definition
title: Kubelet API Operations
description: The API server connects to the kubelet to fetch pod logs, support port-forwarding,
  and enable kubectl attachment to running pods.
resource: source://architecture__control-plane-node-communication.md
tags:
- kubelet
- api operations
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kubelet operations
- pod logs
- port-forwarding
- kubectl attach
---

The connections from the [API server](/definition/kube_apiserver.md) to the [kubelet](/definition/kubelet.md) are used for: Fetching logs for pods. Attaching (usually through `[kubectl](/definition/kubectl_command_line_tool.md)`) to running pods. Providing the kubelet's [port-forwarding](/securitywarning/api_server_to_kubelet_connection_security.md) functionality.
