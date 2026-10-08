---
type: Procedure
title: Configure Node Affinity for a Pod
description: Set node affinity rules for a Pod.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- kubernetes
- pods
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- configure node affinity
- pod node affinity
---

To configure [node](/entity/node.md) affinity for a Pod, add the `affinity` field to the Pod specification and set it with the desired [node](/entity/worker_node.md) affinity rules.
