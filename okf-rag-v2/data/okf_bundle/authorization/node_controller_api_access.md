---
type: Authorization
title: Node Controller API Access
description: The node controller requires full read/write access to v1/Node objects
  to manage node lifecycle and attributes.
resource: source://architecture__cloud-controller.md
tags:
- authorization
- rbac
- node-controller
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- node lifecycle
- node object management
- v1/Node operations
---

## Authorization

The Node controller only works with Node objects. It requires full access to read and modify Node objects.

`v1/Node`: get, list, [create](/operations/kubectl_resource_management_operations.md), update, patch, watch, delete
