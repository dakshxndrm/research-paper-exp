---
type: Design Principle
title: Role-Oriented Design
description: The role-oriented design principle of the Gateway API.
resource: source://services-networking__gateway.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- role-based design
- infrastructure provider
---

[Gateway API](/api/gateway_api.md) kinds are modeled after organizational roles that are responsible for managing [Kubernetes service](/entity/kubernetes_service.md) networking: Infrastructure Provider, Cluster Operator, and Application Developer.
