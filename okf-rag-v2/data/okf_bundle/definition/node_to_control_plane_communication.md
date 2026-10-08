---
type: Definition
title: Node to Control Plane Communication
description: Kubernetes uses a hub-and-spoke API pattern where all API usage from
  nodes or their pods terminates at the API server, which listens on a secure HTTPS
  port with client authentication and authorization enabled.
resource: source://architecture__control-plane-node-communication.md
tags:
- communication
- security
- api-server
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- node communication
- hub-and-spoke model
- API server connection
---

Kubernetes has a "hub-and-spoke" API pattern. All API usage from nodes (or the pods they run) terminates at the [API server](/definition/kube_apiserver.md). None of the other [control plane components](/definition/control_plane_components.md) are designed to expose remote services. The API server is configured to listen for remote connections on a secure HTTPS port (typically 443) with one or more forms of client [authentication](/authentication/kubectl_authentication_methods.md) enabled. One or more forms of authorization should be enabled, especially if anonymous requests or [service](/component/service_load_balancing.md) account tokens are allowed. Nodes should be provisioned with the public root certificate for the cluster such that they can connect securely to the API server along with valid client credentials. A good approach is that the client credentials provided to the [kubelet](/definition/kubelet.md) are in the form of a client certificate. See kubelet TLS bootstrapping for automated provisioning of kubelet [client certificates](/definition/authentication_modules_overview.md). Pods that wish to connect to the API server can do so securely by leveraging a service account so that Kubernetes will automatically inject the public root certificate and a valid bearer token into the pod when it is instantiated. The `kubernetes` service (in `default` namespace) is configured with a virtual IP address that is redirected (via `[kube-proxy](/definition/kube_proxy_optional.md)`) to the HTTPS endpoint on the API server. The control plane components also communicate with the API server over the secure port. As a result, the default operating mode for connections from the nodes and pod running on the nodes to the control plane is secured by default and can run over untrusted and/or public networks.
