---
type: Migration Guide
title: Migrating from Ingress to Gateway API
description: Gateway API is the successor to the Ingress API, requiring a one-time
  conversion of existing Ingress resources.
resource: source://services-networking__gateway.md
tags:
- migration
- ingress
- gateway api
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- ingress migration
- migrating from ingress
- ingress to gateway api
---

[Gateway API](/entity/gateway_api.md) is the successor to the [Ingress](/definition/gateway_api_and_cluster_ingress.md) API; however, it does not include the Ingress kind. As a result, a one-time conversion from existing Ingress resources to [Gateway](/api_kind/gateway_resource.md) API resources is necessary. Refer to the ingress migration guide for details on migrating Ingress resources to Gateway API resources.
