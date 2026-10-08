---
type: Entity
title: Kubernetes Job Resource
description: A Kubernetes Job is a resource designed to run one or more Pods to complete
  a specific task and then terminate.
resource: source://architecture__controller.md
tags:
- kubernetes
- resource
- workload
- pod
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Job object
---

[Job](/entity/job.md) is a [Kubernetes](/policy/garbage_collection_in_kubernetes.md) [resource](/resource/cluster_resources.md) that runs a pod, or perhaps several [Pods](/definition/kubernetes_cluster_architecture.md), to carry out a task and then stop. (Once scheduled, Pod objects become part of the [desired state](/philosophy/kubernetes_state_management.md) for a [kubelet](/definition/kubernetes_node_components_overview.md)).
