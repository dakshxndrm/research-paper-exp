---
type: Mechanism
title: Direct External Control
description: Some Kubernetes controllers perform direct control by interacting with
  systems outside the cluster to achieve a desired state, obtaining their desired
  state from the API server and reporting current state back.
resource: source://architecture__controller.md
tags:
- kubernetes
- external systems
- control loop
- integration
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- direct control
- controllers that interact with external state
---

In contrast with [Job](/entity/job.md), some [controllers](/pattern/kubernetes_controller_pattern.md) need to make changes to things outside of your cluster. For example, if you use a [control loop](/definition/control_loop.md) to make sure there are enough Nodes in your cluster, then that controller needs something outside the current cluster to set up new Nodes when needed. Controllers that interact with external state find their [desired state](/philosophy/kubernetes_state_management.md) from the [API server](/policy/api_server_behavior_in_kubernetes.md), then communicate directly with an external system to bring the current state closer in line. (There actually is a controller that horizontally scales the nodes in your cluster.) The important point here is that the controller makes some changes to bring about your desired state, and then reports the current state back to your cluster's API server. Other control loops can observe that reported data and take their own actions. In the thermostat example, if the room is very cold then a different controller might also turn on a frost protection heater. With [Kubernetes](/policy/garbage_collection_in_kubernetes.md) clusters, the [control plane](/definition/kubernetes_cluster_architecture.md) indirectly works with [IP address management](/procedure/configuring_ip_address_management_ipam.md) tools, storage [services](/procedure/configuring_load_balancing_and_services.md), cloud provider APIs, and other services by extending Kubernetes to implement that.
