---
type: Control
title: Admission Controller for Owner Deletion
description: A Kubernetes admission controller controls user access to change the
  blockOwnerDeletion field for dependent resources based on the delete permissions
  of the owner, preventing unauthorized users from delaying owner object deletion.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- admission controller
- deletion control
- security
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- admission controller
- delete permissions
- owner deletion control
- unauthorized deletion prevention
---

A Kubernetes admission controller controls user access to change this field for dependent resources, based on the [delete](/operations/kubectl_resource_management_operations.md) permissions of the owner. This control prevents unauthorized users from delaying owner object deletion.
