---
type: Definition
title: Kubernetes Network Model Implementation
description: The Kubernetes network model is implemented by the container runtime
  on each node using Container Network Interface (CNI) plugins, which manage network
  and security capabilities ranging from basic interface management to advanced IPAM
  features.
resource: source://cluster-administration__networking.md
tags:
- cni plugins
- network implementation
timestamp: '2026-09-02T17:04:11+00:00'
---

# Kubernetes [Network Model](/definition/kubernetes_network_model_overview.md) Implementation

The network model is implemented by the [container runtime](/definition/container_runtime.md) on each node. The most common container runtimes use Container Network Interface (CNI) [plugins](/extensibility/kubectl_plugins.md) to manage their network and security capabilities. Many different [CNI plugins](/definition/external_components_implementing_kubernetes_networking.md) exist from many different vendors. Some of these provide only basic features of adding and removing network interfaces, while others provide more sophisticated solutions, such as integration with other [container orchestration](/definition/container_management.md) systems, running multiple CNI plugins, advanced IPAM features etc.

See this page for a non-exhaustive list of [networking](/definition/application_exposure_service_and_ingress.md) [addons](/entity/addons.md) supported by Kubernetes.
