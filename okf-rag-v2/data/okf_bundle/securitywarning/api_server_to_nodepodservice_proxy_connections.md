---
type: SecurityWarning
title: API Server to Node/Pod/Service Proxy Connections
description: Default connections from the API server to nodes, pods, or services through
  the proxy functionality use plain HTTP and are neither authenticated nor encrypted,
  making them unsafe over untrusted networks.
resource: source://architecture__control-plane-node-communication.md
tags:
- security
- proxy
- http
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- API proxy
- node proxy
- service proxy
---

The connections from the [API server](/definition/kube_apiserver.md) to a node, pod, or [service](/component/service_load_balancing.md) default to plain HTTP connections and are therefore neither authenticated nor encrypted. They can be run over a secure HTTPS connection by prefixing `https:` to the node, pod, or service name in the API URL, but they will not validate the certificate provided by the HTTPS endpoint nor provide client credentials. So while the connection will be encrypted, it will not provide any guarantees of integrity. These connections **are not currently safe** to run over untrusted or public networks.
