---
type: Definition
title: CloudProvider Interface for CCM
description: The `CloudProvider` interface in `kubernetes/cloud-provider` defines
  how cloud providers can implement their specific integrations with the Cloud Controller
  Manager.
resource: source://architecture__cloud-controller.md
tags:
- interface
- plugin
- cloud provider
- development
- extension
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- CloudProvider interface
- cloud.go
- kubernetes/cloud-provider
- developing Cloud Controller Manager
---

The [cloud controller manager](/entity/cloud_controller_manager.md) uses Go interfaces, specifically, `CloudProvider` interface defined in `cloud.go` from [kubernetes](/policy/garbage_collection_in_kubernetes.md)/cloud-provider to allow implementations from any cloud to be plugged in.

The implementation of the shared [controllers](/pattern/kubernetes_controller_pattern.md) highlighted in this document ([Node](/entity/node.md), Route, and [Service](/entity/kubernetes_service.md)), and some scaffolding along with the shared cloudprovider interface, is part of the Kubernetes core. Implementations specific to cloud providers are outside the core of Kubernetes and implement the `CloudProvider` interface.

For more information about developing plugins, see Developing Cloud Controller Manager.
