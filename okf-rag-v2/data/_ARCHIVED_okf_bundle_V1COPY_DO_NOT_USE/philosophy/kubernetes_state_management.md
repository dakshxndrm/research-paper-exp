---
type: Philosophy
title: Kubernetes State Management
description: Kubernetes embraces a cloud-native philosophy where the cluster is constantly
  changing, and controllers continuously work to reconcile desired and current states,
  making progress even if a stable state is never fully achieved.
resource: source://architecture__controller.md
tags:
- kubernetes
- state management
- cloud-native
- philosophy
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- desired versus current state
- desired state
- current state
- Kubernetes takes a cloud-native view
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) takes a cloud-native view of systems, and is able to handle constant change. Your cluster could be changing at any point as work happens and control loops automatically fix failures. This means that, potentially, your cluster never reaches a stable state. As long as the [controllers](/pattern/kubernetes_controller_pattern.md) for your cluster are running and able to make useful changes, it doesn't matter if the overall state is stable or not.
