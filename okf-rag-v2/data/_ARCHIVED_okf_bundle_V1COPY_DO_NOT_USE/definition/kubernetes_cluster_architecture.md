---
type: Definition
title: Kubernetes Cluster Architecture
description: Describes the fundamental components of a Kubernetes cluster, including
  the control plane and worker nodes, and their basic functions.
resource: source://architecture.md
tags:
- kubernetes
- cluster
- architecture
- control plane
- node
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Kubernetes cluster
- cluster architecture
- worker machines
- nodes
- Pods
- control plane
---

A [Kubernetes](/policy/garbage_collection_in_kubernetes.md) cluster consists of a control plane plus a set of worker machines, called nodes, that run containerized applications. Every cluster needs at least one [worker node](/entity/worker_node.md) in order to run Pods. The worker [node](/entity/node.md)(s) host the Pods that are the components of the application [workload](/entity/workload.md). The control plane manages the worker nodes and the Pods in the cluster. In production environments, the control plane usually runs across multiple computers and a cluster usually runs multiple nodes, providing fault-tolerance and high availability.
