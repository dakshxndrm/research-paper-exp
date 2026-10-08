---
type: Definition
title: CNI Plugin Compatibility Requirements
description: Kubernetes requires a Container Network Interface plugin compatible with
  the CNI specification version 0.4.0 or later, with the project recommending compatibility
  with v1.0.0 or later.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- networking
- cni
- compatibility
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- CNI specification
- CNI plugin compatibility
- network model requirements
---

Kubernetes (version 1.3 through to the latest, and likely onwards) lets you use Container Network Interface (CNI) [plugins](/extensibility/kubectl_plugins.md) for cluster [networking](/definition/application_exposure_service_and_ingress.md). A CNI plugin is required to implement the Kubernetes [network model](/definition/kubernetes_network_model_overview.md). You must use a CNI plugin that is compatible with the v0.4.0 or later releases of the CNI specification. The [Kubernetes project](/definition/kubernetes_overview.md) recommends using a plugin that is compatible with the v1.0.0 CNI specification (plugins can be compatible with multiple spec versions).
