---
type: Procedure
title: Setting Container Limits
description: How Kubernetes sets limits on containers.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- kubelet
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kubelet
---

If the [resource](/resource/cluster_resources.md) has a limit defined for each container, the [kubelet](/definition/kubernetes_node_components_overview.md) will set an upper limit for the pod cgroup associated with that resource.
