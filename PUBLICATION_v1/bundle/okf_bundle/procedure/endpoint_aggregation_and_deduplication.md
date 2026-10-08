---
type: Procedure
title: Endpoint Aggregation and Deduplication
description: Clients of the EndpointSlice API must iterate through all the existing
  EndpointSlices associated to a Service and build a complete list of unique network
  endpoints.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- endpoint aggregation
- endpoint deduplication
---

You can find a reference implementation for how to perform this endpoint aggregation and deduplication as part of the `EndpointSliceCache` code within `[kube-proxy](/component/kube_proxy.md)`.
