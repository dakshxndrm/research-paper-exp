---
type: Definition
title: API Server Proxy Functionality
description: The API server proxies connections to nodes, pods, or services, defaulting
  to unencrypted HTTP but supporting HTTPS with limited certificate validation.
resource: source://architecture__control-plane-node-communication.md
tags:
- proxy
- api server
- networking
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- API proxy
- node service proxy
---

The connections from the [API server](/definition/kube_apiserver.md) to a node, pod, or [service](/component/service_load_balancing.md) default to plain HTTP connections and are therefore neither authenticated nor encrypted. They can be run over a secure HTTPS connection by prefixing `https:` to the node, pod, or service name in the API URL, but they will not validate the certificate provided by the HTTPS endpoint nor provide client credentials.
