---
type: Authorization
title: Route Controller API Access
description: The route controller requires Get access to v1/Node objects to listen
  for creation events and configure routes.
resource: source://architecture__cloud-controller.md
tags:
- authorization
- rbac
- route-controller
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- route configuration
- node route monitoring
- v1/Node get access
---

## Authorization

The route controller listens to Node [object creation](/definition/admission_control_modules.md) and configures routes appropriately. It requires Get access to Node objects.

`v1/Node`: get
