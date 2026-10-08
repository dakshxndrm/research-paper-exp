---
type: Definition
title: Cloud Controller Manager Overview
description: The cloud-controller-manager is a control plane component that runs replicated
  processes to integrate Kubernetes with cloud infrastructure through a plugin mechanism.
resource: source://architecture__cloud-controller.md
tags:
- architecture
- control-plane
- cloud-provider
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cloud controller manager
- cloud infrastructure integration
---

## Design

The cloud [controller manager](/definition/kube_controller_manager.md) runs in the [control plane](/definition/control_plane_components.md) as a replicated set of processes (usually containers in Pods). Each [cloud-controller-manager](/definition/cloud_controller_manager.md) implements multiple controllers in a single process. It can also run as a Kubernetes addon rather than as part of the control plane.

## Cloud controller manager functions

The controllers inside the cloud controller manager include:

### Node controller

The node controller is responsible for updating Node objects when new servers are created in your cloud infrastructure. It obtains information about hosts running in your tenancy with the cloud provider and performs the following functions: [update](/operations/kubectl_resource_management_operations.md) a Node object with the server's unique identifier, annotate and label the Node object with cloud-specific information such as region and resources, obtain the node's hostname and network addresses, and verify the node's health by checking with the cloud provider's API if the server has been deactivated/deleted/terminated.

### Route controller

The route controller is responsible for configuring routes in the cloud so that containers on different nodes in the Kubernetes cluster can communicate with each other. Depending on the cloud provider, it might also allocate blocks of IP addresses for the Pod network.

### [Service](/component/service_load_balancing.md) controller

The service controller integrates Services with cloud infrastructure components such as managed load balancers, IP addresses, network packet filtering, and target health checking. It interacts with cloud provider APIs to set up load balancers and other infrastructure components when a Service resource requiring them is declared.
