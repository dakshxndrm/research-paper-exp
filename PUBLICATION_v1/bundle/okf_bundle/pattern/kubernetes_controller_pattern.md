---
type: Pattern
title: Kubernetes Controller Pattern
description: The Kubernetes controller pattern involves a controller tracking at least
  one resource type, using its `spec` field to represent the desired state and working
  to bring the current state closer to that desired state.
resource: source://architecture__controller.md
tags:
- kubernetes
- design pattern
- resource management
- architecture
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- controller pattern
- controller
- controllers
---

A controller tracks at least one [Kubernetes](/policy/garbage_collection_in_kubernetes.md) [resource type](/definition/api_group_resource_type_namespace_and_name.md). These objects have a spec field that represents the [desired state](/philosophy/kubernetes_state_management.md). The controller(s) for that [resource](/resource/cluster_resources.md) are responsible for making the current state come closer to that desired state. The controller might carry the action out itself; more commonly, in Kubernetes, a controller will send messages to the [API server](/policy/api_server_behavior_in_kubernetes.md) that have useful side effects. Some [built-in controllers](/mechanism/api_server_control.md), such as the namespace controller, act on objects that do not have a spec. For simplicity, this page omits explaining that detail.
