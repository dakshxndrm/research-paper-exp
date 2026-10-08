---
type: Definition
title: Address Types
description: 'EndpointSlices support two address types: IPv4 and IPv6.'
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- address type
- ip family
---

Each EndpointSlice object represents a specific IP address type. If you have a [Service](/entity/kubernetes_service.md) that is available via IPv4 and IPv6, there will be at least two EndpointSlice objects (one for IPv4, and one for IPv6).
