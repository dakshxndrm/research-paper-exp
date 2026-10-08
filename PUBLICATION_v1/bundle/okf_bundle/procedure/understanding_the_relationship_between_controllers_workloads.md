---
type: Procedure
title: Understanding the Relationship between Controllers, Workloads, and Pods
description: A step-by-step guide to understanding the relationship between controllers,
  workloads, and pods.
resource: source://workloads__podgroup-api.md
tags:
- kubernetes
- controller-workload-pod-relationship
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- relationship between controllers and workloads
- controllers and workloads
---

The relationship between [controllers](/pattern/kubernetes_controller_pattern.md), Workloads, PodGroups, and [Pods](/definition/kubernetes_cluster_architecture.md) follows this pattern: 1. The [workload](/entity/workload.md) controller creates a Workload that defines [PodGroupTemplates](/template/podgrouptemplates.md) with [scheduling policies](/policy/scheduling_policies_in_kube_scheduler.md).
