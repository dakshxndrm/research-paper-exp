---
type: Implementation
title: Service Proxy Implementation
description: Routes service traffic to its backends.
resource: source://services-networking.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kube-proxy
---

A [service proxy](/api/service_api.md) implementation monitors the set of [Service](/entity/kubernetes_service.md) and EndpointSlice objects, and programs the data plane to route service traffic to its backends.
