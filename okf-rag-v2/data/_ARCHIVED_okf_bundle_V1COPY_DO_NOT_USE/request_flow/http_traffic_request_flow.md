---
type: Request Flow
title: HTTP Traffic Request Flow
description: The request flow for HTTP traffic being routed to a Service by using
  a Gateway and an HTTPRoute.
resource: source://services-networking__gateway.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- http request flow
- traffic routing
---

1. The client starts to prepare an HTTP request for the URL http://www.example.com 2. The client's DNS resolver queries for the destination [name](/definition/api_group_resource_type_namespace_and_name.md) and learns a mapping to one or more IP addresses associated with the [Gateway](/api_kind/gateway.md).
