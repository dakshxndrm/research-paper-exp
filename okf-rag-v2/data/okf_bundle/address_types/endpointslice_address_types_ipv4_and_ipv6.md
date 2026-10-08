---
type: Address types
title: EndpointSlice address types IPv4 and IPv6
description: 'EndpointSlices support two address types: IPv4 and IPv6. Each EndpointSlice
  object represents a specific IP address type; a Service available via both IPv4
  and IPv6 will have at least two EndpointSlice objects.'
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- networking
- ip address
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- IPv4 address
- IPv6 address
- address type
---

EndpointSlices support two address types: IPv4 and IPv6. Each [EndpointSlice object](/definition/endpointslice_api_resource.md) represents a specific IP address type. If you have a [Service](/component/service_load_balancing.md) that is available via IPv4 and IPv6, there will be at least two [EndpointSlice](/definition/service_api_and_stable_endpoints.md) objects (one for IPv4, and one for IPv6).
