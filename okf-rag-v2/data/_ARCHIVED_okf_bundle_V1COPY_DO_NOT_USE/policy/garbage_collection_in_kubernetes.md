---
type: Policy
title: Garbage Collection in Kubernetes
description: How garbage collection works in Kubernetes.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- garbage collection
- kubernetes
---

When you tell Kubernetes to [delete](/procedure/deleting_resources_in_kubernetes.md) a [resource](/resource/cluster_resources.md), the [API server](/policy/api_server_behavior_in_kubernetes.md) allows the managing [controller](/pattern/kubernetes_controller_pattern.md) to [process](/concept/pod_definition.md) any [finalizer](/procedure/using_finalizers_in_kubernetes.md) rules for the resource.
