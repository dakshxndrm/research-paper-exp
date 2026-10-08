---
type: Policy
title: Service Controller API Permissions
description: The Service controller requires specific access to Service objects to
  manage load balancers and other infrastructure components.
resource: source://architecture__cloud-controller.md
tags:
- service controller
- authorization
- rbac
- service object
- api access
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Service controller authorization
---

The [service controller](/component/cloud_controller_manager.md) watches for [Service](/entity/kubernetes_service.md) object **create**, **update** and **[delete](/procedure/deleting_resources_in_kubernetes.md)** events and then configures load balancers for those [Services](/procedure/configuring_load_balancing_and_services.md) appropriately.

To access Services, it requires **list**, and **watch** access. To update Services, it requires **patch** and **update** access to the `status` subresource.

`v1/Service`:

- list
- get
- watch
- patch
- update
