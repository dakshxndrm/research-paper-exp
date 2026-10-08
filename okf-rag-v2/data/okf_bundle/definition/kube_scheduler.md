---
type: Definition
title: kube-scheduler
description: The default scheduler for Kubernetes that watches for newly created Pods
  with no assigned node and selects a node for them to run on.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- scheduling
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- scheduler
- Kubernetes scheduler
---

kube-scheduler is the [default scheduler](/entity/kube_scheduler.md) for Kubernetes. It watches for newly created Pods with no assigned node and selects a node for them to run on based on resource requirements, constraints, and other factors.
