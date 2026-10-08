---
type: Procedure
title: Scoring Step in kube-scheduler
description: The process of ranking nodes for a pod.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- kubernetes
- scheduling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- node scoring
- pod placement scoring
---

In the _scoring_ step, the scheduler ranks the remaining [nodes](/definition/kubernetes_cluster_architecture.md) to choose the most suitable [Pod placement](/concept/scheduling.md).
