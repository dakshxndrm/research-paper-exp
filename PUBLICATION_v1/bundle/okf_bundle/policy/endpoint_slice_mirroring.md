---
type: Policy
title: Endpoint Slice Mirroring
description: The control plane mirrors most user-created Endpoints resources to corresponding
  EndpointSlices.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- control-plane
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- endpoint mirroring
---

However, this feature is deprecated. Users who manually specify endpoints for selectorless [Services](/procedure/configuring_load_balancing_and_services.md) should do so by creating EndpointSlice resources directly, rather than by creating Endpoints resources and allowing them to be mirrored.
