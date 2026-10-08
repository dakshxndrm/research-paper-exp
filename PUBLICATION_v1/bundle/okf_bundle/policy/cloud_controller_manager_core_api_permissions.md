---
type: Policy
title: Cloud Controller Manager Core API Permissions
description: The core implementation of the Cloud Controller Manager requires access
  to create Event objects and ServiceAccounts for secure operation.
resource: source://architecture__cloud-controller.md
tags:
- cloud controller manager
- authorization
- rbac
- event object
- serviceaccount
- api access
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- CCM core authorization
- miscellaneous authorization
---

The implementation of the core of the [cloud controller manager](/entity/cloud_controller_manager.md) requires access to create Event objects, and to ensure secure operation, it requires access to create ServiceAccounts.

`v1/Event`:

- create
- patch
- update

`v1/ServiceAccount`:

- create

The RBAC ClusterRole for the cloud [controller](/pattern/kubernetes_controller_pattern.md) manager looks like:
