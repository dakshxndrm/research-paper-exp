---
type: Procedure
title: Binding in kube-scheduler
description: The process of assigning a pod to a node.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- pod binding
- node assignment
---

The scheduler then notifies the [API server](/policy/api_server_behavior_in_kubernetes.md) about this [decision](/decision/scheduling_decision.md) in a [process](/concept/pod_definition.md) called _binding_.
