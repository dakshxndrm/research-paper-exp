---
type: Policy
title: Route Controller API Permissions
description: The Route controller requires Get access to Node objects to configure
  routes appropriately.
resource: source://architecture__cloud-controller.md
tags:
- route controller
- authorization
- rbac
- node object
- api access
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Route controller authorization
---

The [route controller](/component/cloud_controller_manager.md) listens to [Node](/entity/node.md) [object creation](/procedure/creation_ordering_of_objects.md) and configures routes appropriately. It requires Get access to [Node](/entity/worker_node.md) objects.

`v1/Node`:

- get
