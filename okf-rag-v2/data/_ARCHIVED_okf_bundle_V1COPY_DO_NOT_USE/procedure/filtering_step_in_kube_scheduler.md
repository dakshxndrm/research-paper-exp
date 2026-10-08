---
type: Procedure
title: Filtering Step in kube-scheduler
description: The process of finding suitable nodes for a pod.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- node filtering
- pod placement filtering
---

The _filtering_ step finds the set of [Nodes](/definition/kubernetes_cluster_architecture.md) where it's feasible to schedule the Pod.
