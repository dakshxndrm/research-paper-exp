---
type: Procedure
title: Container Request Calculation
description: How Kubernetes calculates container requests for Pods.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- scheduler
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kube-scheduler
---

When the [kube-scheduler](/policy/kubernetes_scheduling_overview.md) is deciding which [node](/entity/node.md) should run a new Pod, the scheduler considers that Pod's `overhead` as well as the sum of container requests for that Pod.
