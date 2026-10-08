---
type: Procedure
title: Endpoint Slice Creation for Selectorless Services
description: Users who manually specify endpoints for selectorless Services should
  do so by creating EndpointSlice resources directly.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- api
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- endpoint slice creation
- selectorless service
---

This is because the Endpoints API is deprecated and users should use the EndpointSlice API instead.
