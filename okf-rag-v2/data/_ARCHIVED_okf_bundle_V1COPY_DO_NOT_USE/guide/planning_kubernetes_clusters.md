---
type: Guide
title: Planning Kubernetes Clusters
description: Outlines considerations and resources for planning, setting up, and configuring
  Kubernetes clusters.
resource: source://cluster-administration.md
tags:
- kubernetes
- cluster
- planning
- setup
- configuration
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- planning a cluster
- cluster planning
---

Guides in Setup provide examples for planning, setting up, and configuring [Kubernetes](/policy/garbage_collection_in_kubernetes.md) clusters. Before choosing a guide, consider the following:
- Do you want to try out Kubernetes on your computer, or do you want to build a high-availability, multi-[node](/entity/node.md) cluster? Choose [distros](/definition/kubernetes_distros.md) best suited for your needs.
- Will you be using a hosted [Kubernetes cluster](/definition/kubernetes_cluster_architecture.md), such as Google Kubernetes Engine, or hosting your own cluster?
- Will your cluster be on-premises, or in the cloud (IaaS)? Kubernetes does not directly support hybrid clusters; instead, you can set up multiple clusters.
- If you are configuring Kubernetes on-premises, consider which networking model fits best.
- Will you be running Kubernetes on "bare metal" hardware or on virtual machines (VMs)?
- Do you want to run a cluster, or do you expect to do active development of Kubernetes project code? If the latter, choose an actively-developed distro. Some distros only use binary releases, but offer a greater variety of choices.
- Familiarize yourself with the components needed to run a cluster.
