---
type: Definition
title: External Access Mechanisms
description: Compares the Gateway API, Ingress, and LoadBalancer Service types for
  external cluster access.
resource: source://services-networking.md
tags:
- networking
- access
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- external access
- cluster ingress
- LoadBalancer
- routing
---

# External Access Mechanisms

The [Gateway API](/entity/gateway_api.md) (or its predecessor, Ingress) allows you to make Services accessible to clients that are outside the cluster.

* A simpler, but less-configurable, mechanism for [cluster ingress](/definition/gateway_api_and_cluster_ingress.md) is available via the [Service API](/definition/service_api_and_stable_endpoints.md)'s `type: LoadBalancer`, when using a supported cloud-provider.
