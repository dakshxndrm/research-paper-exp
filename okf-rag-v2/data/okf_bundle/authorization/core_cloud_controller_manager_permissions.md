---
type: Authorization
title: Core Cloud Controller Manager Permissions
description: The cloud controller manager requires create access to v1/Event and v1/ServiceAccount
  objects for event generation and secure operation.
resource: source://architecture__cloud-controller.md
tags:
- authorization
- rbac
- cloud-controller-manager
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- event creation
- service account creation
- ccm core permissions
---

## Others

The implementation of the core of the [cloud controller manager](/definition/cloud_controller_manager_overview.md) requires access to [create](/operations/kubectl_resource_management_operations.md) Event objects, and to ensure secure operation, it requires access to create ServiceAccounts.

`v1/Event`: create, patch, update

`v1/ServiceAccount`: create
