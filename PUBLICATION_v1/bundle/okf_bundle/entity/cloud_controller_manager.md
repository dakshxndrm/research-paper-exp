---
type: Entity
title: Cloud Controller Manager
description: The Cloud Controller Manager integrates Kubernetes with cloud infrastructure
  technologies using a plugin mechanism.
resource: source://architecture__cloud-controller.md
tags:
- kubernetes
- cloud
- control plane
- plugin
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- cloud-controller-manager
---

Cloud infrastructure technologies let you run [Kubernetes](/policy/garbage_collection_in_kubernetes.md) on public, private, and hybrid clouds. Kubernetes believes in automated, API-driven infrastructure without tight coupling between components.

The [cloud-controller-manager](/component/cloud_controller_manager.md) is structured using a [plugin](/plugin/gangscheduling_plugin.md) mechanism that allows different cloud providers to integrate their platforms with Kubernetes.

The cloud controller manager runs in the [control plane](/definition/kubernetes_cluster_architecture.md) as a replicated set of processes (usually, these are containers in Pods). Each cloud-controller-manager implements multiple [controllers](/pattern/kubernetes_controller_pattern.md) in a single [process](/concept/pod_definition.md).

You can also run the cloud controller manager as a Kubernetes [addon](/entity/addon.md) rather than as part of the control plane.
