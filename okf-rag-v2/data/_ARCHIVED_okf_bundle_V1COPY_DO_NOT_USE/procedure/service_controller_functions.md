---
type: Procedure
title: Service Controller Functions
description: The Service controller interacts with cloud provider APIs to set up load
  balancers and other infrastructure components for Kubernetes Services.
resource: source://architecture__cloud-controller.md
tags:
- service
- controller
- load balancer
- kubernetes
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- service controller
---

[Services](/procedure/configuring_load_balancing_and_services.md) integrate with cloud infrastructure components such as managed load balancers, IP addresses, network packet filtering, and target health checking. The [service controller](/component/cloud_controller_manager.md) interacts with your cloud provider's APIs to set up load balancers and other infrastructure components when you declare a [Service](/entity/kubernetes_service.md) [resource](/resource/cluster_resources.md) that requires them.
