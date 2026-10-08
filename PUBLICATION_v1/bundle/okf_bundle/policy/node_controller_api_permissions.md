---
type: Policy
title: Node Controller API Permissions
description: The Node controller requires full access to read and modify Node objects
  to perform its operations.
resource: source://architecture__cloud-controller.md
tags:
- node controller
- authorization
- rbac
- node object
- api access
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Node controller authorization
---

The [Node controller](/component/kube_controller_manager.md) only works with [Node](/entity/node.md) objects. It requires full access to read and modify [Node](/entity/worker_node.md) objects.

`v1/Node`:

- get
- list
- create
- update
- patch
- watch
- [delete](/procedure/deleting_resources_in_kubernetes.md)
