---
type: Communication Path
title: API Server Proxy Functionality
description: Explains the API server's proxy functionality for connecting to nodes,
  pods, or services and its security implications.
resource: source://architecture__control-plane-node-communication.md
tags:
- communication
- api server
- proxy
- node
- pod
- service
- security
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- API server's proxy functionality
- API server to nodes, pods, and services
- connections from the API server to a node, pod, or service
---

The [API server](/policy/api_server_behavior_in_kubernetes.md)'s [proxy](/entity/kube_proxy.md) functionality allows connections from the API server to any [node](/entity/node.md), pod, or [service](/entity/kubernetes_service.md). These connections default to plain HTTP and are therefore neither authenticated nor encrypted, making them unsafe to run over untrusted or public networks. While they can be run over a secure HTTPS connection by prefixing `https:` to the [node](/entity/worker_node.md), pod, or [service name](/procedure/relaxed_service_name_validation.md) in the API URL, this only encrypts the connection. It will not validate the certificate provided by the HTTPS endpoint nor provide client credentials, meaning it does not provide any guarantees of integrity. These connections are not currently safe to run over untrusted or public networks.
