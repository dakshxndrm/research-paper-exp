---
type: API Kind
title: GatewayClass Definition
description: Defines a set of gateways with common configuration and managed by a
  controller that implements the class.
resource: source://services-networking__gateway.md
tags:
- api
- kind
- gateway
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- gateway class
- gatewayclass
---

[Gateway API](/entity/gateway_api.md) has four stable API kinds. GatewayClass defines a set of gateways with common configuration and is managed by a controller that implements the class. A [Gateway](/api_kind/gateway_resource.md) must reference a GatewayClass that contains the name of the controller that implements the class. In a minimal example, a controller configured to manage GatewayClasses with the controller name `example.com/gateway-controller` will manage Gateways of this class. The GatewayClass reference provides a full definition of this API kind.
