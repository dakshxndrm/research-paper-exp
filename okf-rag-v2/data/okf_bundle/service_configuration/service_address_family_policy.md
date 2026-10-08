---
type: Service Configuration
title: Service address family policy
description: Configuration options for controlling IP address assignment behavior
  in Services.
resource: source://services-networking__dual-stack.md
tags:
- networking
- services
- ip address assignment
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- ipFamilyPolicy
- Service dual-stack configuration
- Service single-stack
- Service IP families
---

Services can use IPv4, IPv6, or both. The address family defaults to the first [service](/component/service_load_balancing.md) cluster IP range. The .spec.ipFamilyPolicy field can be set to SingleStack, PreferDualStack, or RequireDualStack. The .spec.ipFamilies field is conditionally mutable and can be set to ["IPv4"], ["IPv6"], ["IPv4","IPv6"], or ["IPv6","IPv4"]. The first family listed is used for the legacy .spec.clusterIP field.
