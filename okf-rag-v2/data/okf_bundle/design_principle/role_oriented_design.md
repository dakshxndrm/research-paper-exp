---
type: Design Principle
title: Role-Oriented Design
description: Gateway API kinds are modeled after organizational roles responsible
  for managing Kubernetes service networking.
resource: source://services-networking__gateway.md
tags:
- design
- principle
- role-oriented
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- organizational roles
---

[Gateway API](/entity/gateway_api.md) kinds are modeled after organizational roles responsible for managing Kubernetes [service](/component/service_load_balancing.md) [networking](/definition/application_exposure_service_and_ingress.md). The three primary roles are Infrastructure Provider, who manages infrastructure for multiple isolated clusters and tenants; Cluster Operator, who manages clusters and concerns itself with policies and network access; and Application Developer, who manages an application running in a cluster and concerns itself with application-level configuration and Service composition.
