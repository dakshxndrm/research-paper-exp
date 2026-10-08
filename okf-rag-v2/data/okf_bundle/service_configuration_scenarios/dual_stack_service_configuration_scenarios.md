---
type: Service Configuration Scenarios
title: Dual-stack Service configuration scenarios
description: Examples demonstrating various dual-stack Service configuration behaviors.
resource: source://services-networking__dual-stack.md
tags:
- networking
- services
- ip address assignment
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Service dual-stack scenarios
- Service IP family policy examples
- Service configuration examples
---

Scenarios include: new Services without explicit .spec.[ipFamilyPolicy](/service_configuration/service_address_family_policy.md) default to SingleStack using the first configured [service](/component/service_load_balancing.md)-cluster-ip-range; Services with PreferDualStack assigned both IPv4 and IPv6 cluster IPs when dual-stack is enabled; Services with explicit IPv6 and IPv4 in .spec.ipFamilies and PreferDualStack set .spec.clusterIP to the [IPv6 address](/address_types/endpointslice_address_types_ipv4_and_ipv6.md) as the first element; existing Services reconfigured by [control plane](/definition/control_plane_components.md) to SingleStack when dual-stack is enabled; and Services switching between single-stack and dual-stack by changing .spec.ipFamilyPolicy.
