---
type: Procedure
title: Node Controller Functions
description: The node controller manages Node objects by updating identifiers, annotations,
  hostnames, and verifying node health through cloud provider API checks.
resource: source://architecture__cloud-controller.md
tags:
- procedure
- node-controller
- lifecycle
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- node management
- node update process
- node health verification
---

## Node controller

The node controller is responsible for updating Node objects when new servers are created in your cloud infrastructure. It obtains information about the hosts running inside your tenancy with the cloud provider and performs the following functions:

1. [Update](/operations/kubectl_resource_management_operations.md) a Node object with the corresponding server's unique identifier obtained from the cloud provider API.
1. Annotating and labelling the Node object with cloud-specific information, such as the region the node is deployed into and the resources (CPU, memory, etc) that it has available.
1. Obtain the node's hostname and network addresses.
1. Verifying the node's health. In case a node becomes unresponsive, this controller checks with your cloud provider's API to see if the server has been deactivated / deleted / terminated. If the node has been deleted from the cloud, the controller deletes the Node object from your Kubernetes cluster.

Some cloud provider implementations split this into a node controller and a separate [node lifecycle](/authorization/node_controller_api_access.md) controller.
