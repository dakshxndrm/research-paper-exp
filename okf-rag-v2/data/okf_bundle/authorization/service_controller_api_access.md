---
type: Authorization
title: Service Controller API Access
description: The service controller requires list and watch access to v1/Service objects,
  and patch/update access to the status subresource for Service management.
resource: source://architecture__cloud-controller.md
tags:
- authorization
- rbac
- service-controller
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- service lifecycle
- load balancer management
- v1/Service operations
---

## Authorization

The [service](/component/service_load_balancing.md) controller watches for Service object [create](/operations/kubectl_resource_management_operations.md), update and delete events and then configures load balancers for those Services appropriately. To access Services, it requires list, and watch access. To update Services, it requires patch and update access to the `status` subresource.

`v1/Service`: list, get, watch, patch, update
