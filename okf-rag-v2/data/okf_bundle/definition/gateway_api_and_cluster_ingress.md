---
type: Definition
title: Gateway API and Cluster Ingress
description: Describes the Gateway API and Ingress as mechanisms for making Services
  accessible to external clients.
resource: source://services-networking.md
tags:
- networking
- ingress
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Gateway API
- Ingress
- cluster ingress
- external access
---

# [Gateway API](/entity/gateway_api.md) and Cluster Ingress

The [Gateway](/api_kind/gateway_resource.md) API (or its predecessor, Ingress) allows you to make Services accessible to clients that are outside the cluster.

* A simpler, but less-configurable, mechanism for cluster ingress is available via the [Service API](/definition/service_api_and_stable_endpoints.md)'s `type: [LoadBalancer](/definition/external_access_mechanisms.md)`, when using a supported cloud-provider.
