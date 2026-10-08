---
type: Procedure
title: Create Dual-Stack Services
description: Procedure to create dual-stack services for Kubernetes clusters.
resource: source://services-networking__dual-stack.md
tags:
- kubernetes
- networking
- service
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- create dual-stack service
- dual-stack service creation
---

You can create [Services](/procedure/configuring_load_balancing_and_services.md) which can use IPv4, IPv6, or both. Set the `.spec.ipFamilyPolicy` field to `PreferDualStack` or `RequireDualStack`.
