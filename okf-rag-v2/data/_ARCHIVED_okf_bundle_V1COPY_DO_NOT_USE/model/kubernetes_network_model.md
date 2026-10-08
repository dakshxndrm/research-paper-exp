---
type: Model
title: Kubernetes Network Model
description: Overview of the Kubernetes network model and its components.
resource: source://services-networking.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- cluster networking
- pod network
---

The [Kubernetes network model](/policy/kubernetes_cluster_networking_requirements.md) is built out of several pieces. Each pod in a cluster gets its own unique cluster-wide IP address. A pod has its own private network [namespace](/definition/api_group_resource_type_namespace_and_name.md) which is shared by all of the containers within the pod.
