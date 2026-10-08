---
type: Communication Pattern
title: Node to Control Plane Communication
description: Explains how nodes and pods securely communicate with the Kubernetes
  API server using a hub-and-spoke pattern.
resource: source://architecture__control-plane-node-communication.md
tags:
- communication
- node
- control plane
- api server
- security
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Node to Control Plane
- API usage from nodes
- pods connecting to API server
- connections from the nodes and pod running on the nodes to the control plane
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) has a "hub-and-spoke" API pattern where all API usage from nodes (or the pods they run) terminates at the [API server](/policy/api_server_behavior_in_kubernetes.md). The API server is configured to listen for remote connections on a secure HTTPS port (typically 443) with one or more forms of client [authentication](/authentication/authentication_with_kubeconfig_file.md) and [authorization](/definition/kubernetes_authentication_and_authorization.md) enabled. Nodes should be provisioned with the public root certificate for the cluster and valid client credentials, such as a client certificate for the [kubelet](/definition/kubernetes_node_components_overview.md). Pods that wish to connect to the API server can do so securely by leveraging a [service](/entity/kubernetes_service.md) account, which automatically injects the public root certificate and a valid bearer token into the pod. The `kubernetes` service (in `default` [namespace](/definition/api_group_resource_type_namespace_and_name.md)) is configured with a virtual IP address that is redirected (via `[kube-proxy](/component/kube_proxy.md)`) to the HTTPS endpoint on the API server. [Control plane components](/definition/kubernetes_control_plane_role.md) also communicate with the API server over the secure port. As a result, the default operating [mode](/definition/disruption_mode.md) for connections from the nodes and pods running on the nodes to the [control plane](/definition/kubernetes_cluster_architecture.md) is secured by default and can run over untrusted and/or public networks.
