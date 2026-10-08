---
type: Entity
title: Control Plane Components
description: Core components that manage the overall state of a Kubernetes cluster.
resource: source://overview__components.md
tags:
- kubernetes
- architecture
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- control plane
- master components
---

A Kubernetes cluster consists of a control plane and one or more [worker nodes](/definition/node_components.md). The [control plane components](/definition/control_plane_components.md) manage the overall state of the cluster. Key components include [kube-apiserver](/definition/kube_apiserver.md), which exposes the Kubernetes HTTP API; [etcd](/definition/etcd.md), a consistent and highly-available key value store for all API server data; [kube-scheduler](/definition/kube_scheduler.md), which assigns Pods to [suitable nodes](/definition/feasible_nodes.md); and [kube-controller-manager](/definition/kube_controller_manager.md), which runs controllers to implement Kubernetes API behavior. The [cloud-controller-manager](/definition/cloud_controller_manager.md) is an optional component that integrates with underlying cloud provider(s).
