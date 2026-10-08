---
type: Definition
title: Kubernetes Control Plane Role
description: Explains the function of the Kubernetes control plane components, which
  make global decisions and respond to cluster events.
resource: source://architecture.md
tags:
- kubernetes
- control plane
- architecture
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- control plane
- control plane components
---

The [control plane](/definition/kubernetes_cluster_architecture.md)'s components make global decisions about the cluster (for example, [scheduling](/concept/scheduling.md)), as well as detecting and responding to cluster events (for example, starting up a new pod when a [Deployment](/entity/deployment.md)'s `replicas` field is unsatisfied). Control plane components can be run on any machine in the cluster. For simplicity, setup scripts typically start all control plane components on the same machine, and do not run user containers on this machine. In production environments, the control plane usually runs across multiple computers, providing fault-tolerance and high availability. Key control plane components include `kube-apiserver`, `etcd`, `[kube-scheduler](/policy/kubernetes_scheduling_overview.md)`, `[kube-controller-manager](/component/kube_controller_manager.md)`, and `[cloud-controller-manager](/component/cloud_controller_manager.md)`.
