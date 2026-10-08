---
type: Procedure
title: Route Controller Functions
description: The route controller configures cloud routes to enable inter-container
  communication and may allocate IP blocks for the Pod network.
resource: source://architecture__cloud-controller.md
tags:
- procedure
- route-controller
- networking
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- route configuration
- network routing
- pod IP allocation
---

## Route controller

The route controller is responsible for configuring routes in the cloud appropriately so that containers on different nodes in your Kubernetes cluster can communicate with each other. Depending on the cloud provider, the route controller might also allocate blocks of IP addresses for the Pod network.
