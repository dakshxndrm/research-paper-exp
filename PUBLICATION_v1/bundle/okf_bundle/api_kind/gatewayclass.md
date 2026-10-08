---
type: API Kind
title: GatewayClass
description: A GatewayClass defines a set of gateways with common configuration and
  managed by a controller.
resource: source://services-networking__gateway.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- gateway class
- infrastructure provider
---

A [Gateway](/api_kind/gateway.md) object is associated with exactly one GatewayClass; the GatewayClass describes the gateway [controller](/pattern/kubernetes_controller_pattern.md) responsible for managing Gateways of this [class](/entity/priorityclass.md).
