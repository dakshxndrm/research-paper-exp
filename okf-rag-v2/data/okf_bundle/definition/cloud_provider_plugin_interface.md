---
type: Definition
title: Cloud Provider Plugin Interface
description: The cloud controller manager uses Go interfaces from the kubernetes/cloud-provider
  package to allow cloud provider implementations to be plugged into Kubernetes.
resource: source://architecture__cloud-controller.md
tags:
- architecture
- plugin
- cloud-provider
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cloud provider interface
- CloudProvider Go interface
- plugin mechanism
---

## Authorization

* The [cloud controller manager](/definition/cloud_controller_manager_overview.md) uses Go interfaces, specifically, `CloudProvider` interface defined in `cloud.go` from kubernetes/cloud-provider to allow implementations from any cloud to be plugged in.
* The implementation of the shared controllers highlighted in this document (Node, Route, and [Service](/component/service_load_balancing.md)), and some scaffolding along with the shared cloudprovider interface, is part of the Kubernetes core. Implementations specific to cloud providers are outside the core of Kubernetes and implement the `CloudProvider` interface.
* For more information about developing [plugins](/extensibility/kubectl_plugins.md), see Developing Cloud [Controller Manager](/definition/kube_controller_manager.md).
