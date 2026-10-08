---
type: Procedure
title: Node Controller Functions
description: The Node controller updates Node objects with cloud provider information,
  obtains node details, and verifies node health.
resource: source://architecture__cloud-controller.md
tags:
- node
- controller
- cloud provider
- kubernetes
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- node controller
- node lifecycle controller
---

The [node controller](/component/kube_controller_manager.md) is responsible for updating [Node](/entity/node.md) objects when new servers are created in your cloud infrastructure. The [node](/entity/worker_node.md) [controller](/pattern/kubernetes_controller_pattern.md) obtains information about the hosts running inside your tenancy with the cloud provider. The node controller performs the following functions:

1.  Update a Node object with the corresponding server's unique identifier obtained from the cloud provider API.
2.  Annotating and labelling the Node object with cloud-specific information, such as the region the node is deployed into and the resources (CPU, memory, etc) that it has available.
3.  Obtain the node's hostname and network addresses.
4.  Verifying the node's health. In case a node becomes unresponsive, this controller checks with your cloud provider's API to see if the server has been deactivated / deleted / terminated. If the node has been deleted from the cloud, the controller deletes the Node object from your [Kubernetes cluster](/definition/kubernetes_cluster_architecture.md).

Some cloud provider implementations split this into a node controller and a separate node [lifecycle](/policy/podgroup_ownership_and_lifecycle.md) controller.
