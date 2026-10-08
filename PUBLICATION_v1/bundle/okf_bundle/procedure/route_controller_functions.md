---
type: Procedure
title: Route Controller Functions
description: The Route controller configures routes in the cloud to enable communication
  between containers on different Kubernetes nodes.
resource: source://architecture__cloud-controller.md
tags:
- route
- controller
- networking
- kubernetes
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- route controller
---

The [route controller](/component/cloud_controller_manager.md) is responsible for configuring routes in the cloud appropriately so that containers on different nodes in your [Kubernetes cluster](/definition/kubernetes_cluster_architecture.md) can communicate with each other.

Depending on the cloud provider, the route [controller](/pattern/kubernetes_controller_pattern.md) might also allocate blocks of IP addresses for the [Pod network](/model/kubernetes_network_model.md).
