---
type: Procedure
title: Service Controller Functions
description: The service controller configures cloud load balancers and infrastructure
  components when Service resources are created, updated, or deleted.
resource: source://architecture__cloud-controller.md
tags:
- procedure
- service-controller
- load-balancer
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- service configuration
- load balancer setup
- infrastructure integration
---

## [Service](/component/service_load_balancing.md) controller

Services integrate with cloud infrastructure components such as managed load balancers, IP addresses, network packet filtering, and target health checking. The service controller interacts with your cloud provider's APIs to set up load balancers and other infrastructure components when you declare a Service resource that requires them.
