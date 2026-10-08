---
type: Extension
title: External State Control
description: Controllers that manage external cluster resources, such as node scaling,
  obtain desired state from the API server and communicate directly with external
  systems to align current state.
resource: source://architecture__controller.md
tags:
- kubernetes
- external system
- node scaling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- external controller
- cluster scaling controller
- node management
---

In contrast with Job, some controllers need to make changes to things outside of your cluster. For example, if you use a [control loop](/definition/control_loop.md) to make sure there are enough Nodes in your cluster, then that controller needs something outside the current cluster to set up new Nodes when needed. Controllers that interact with external state find their [desired state](/concept/desired_versus_current_state.md) from the [API server](/definition/kube_apiserver.md), then communicate directly with an external system to bring the current state closer in line. There actually is a controller that horizontally scales the nodes in your cluster.
