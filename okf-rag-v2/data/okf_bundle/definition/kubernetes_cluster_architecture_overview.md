---
type: Definition
title: Kubernetes Cluster Architecture Overview
description: Describes the fundamental components of a Kubernetes cluster, including
  the control plane and worker nodes, and their respective responsibilities.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- cluster
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cluster architecture
- Kubernetes components
- cluster components
---

A Kubernetes cluster consists of a [control plane](/definition/control_plane_components.md) plus a set of worker machines, called nodes, that run containerized applications. Every cluster needs at least one worker node in order to run Pods. The worker node(s) host the Pods that are the components of the application workload. The control plane manages the [worker nodes](/definition/node_components.md) and the Pods in the cluster. In production environments, the control plane usually runs across multiple computers and a cluster usually runs multiple nodes, providing fault-tolerance and high availability.
