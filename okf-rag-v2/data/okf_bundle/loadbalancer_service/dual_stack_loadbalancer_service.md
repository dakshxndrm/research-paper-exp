---
type: LoadBalancer Service
title: Dual-stack LoadBalancer Service
description: Configuration requirements for provisioning dual-stack load balancers.
resource: source://services-networking__dual-stack.md
tags:
- networking
- services
- loadbalancer
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- LoadBalancer dual-stack
- dual-stack load balancer
- Service type LoadBalancer dual-stack
---

To provision a dual-stack load balancer for a [Service](/component/service_load_balancing.md), set the .spec.type field to [LoadBalancer](/definition/external_access_mechanisms.md) and set .spec.[ipFamilyPolicy](/service_configuration/service_address_family_policy.md) field to PreferDualStack or RequireDualStack. The cloud provider must support IPv4 and IPv6 load balancers to use a dual-stack LoadBalancer type Service.
