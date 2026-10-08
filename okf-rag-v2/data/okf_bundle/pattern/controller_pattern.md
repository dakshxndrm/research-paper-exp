---
type: Pattern
title: Controller Pattern
description: A controller tracks Kubernetes resource types and works to make the current
  state of those resources closer to their desired state defined in the spec field.
resource: source://architecture__controller.md
tags:
- kubernetes
- control plane
- automation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Kubernetes controller
- resource controller
---

A controller tracks at least one Kubernetes resource type. These objects have a spec field that represents the [desired state](/concept/desired_versus_current_state.md). The controller(s) for that resource are responsible for making the current state come closer to that desired state. The controller might carry the action out itself; more commonly, in Kubernetes, a controller will send messages to the [API server](/definition/kube_apiserver.md) that have useful side effects. Some [built-in controllers](/category/built_in_controllers.md), such as the namespace controller, act on objects that do not have a spec. For simplicity, this page omits explaining that detail.
