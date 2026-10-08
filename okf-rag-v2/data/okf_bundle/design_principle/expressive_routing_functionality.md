---
type: Design Principle
title: Expressive Routing Functionality
description: Gateway API kinds support common traffic routing use cases such as header-based
  matching and traffic weighting.
resource: source://services-networking__gateway.md
tags:
- design
- principle
- expressive
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- expressive routing
- header-based matching
- traffic weighting
---

[Gateway API](/entity/gateway_api.md) kinds support functionality for common [traffic routing](/definition/service_endpoint_management.md) use cases such as header-based matching, traffic weighting, and others that were only possible in [Ingress](/definition/gateway_api_and_cluster_ingress.md) by using custom annotations. This expressiveness allows for more granular [traffic control](/definition/networkpolicy_for_traffic_control.md).
