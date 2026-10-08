---
type: Deployment
title: Running Kubernetes Controllers
description: Kubernetes controllers can be deployed as built-in components within
  the `kube-controller-manager`, as extensions running outside the control plane,
  or as custom controllers deployed as Pods or externally.
resource: source://architecture__controller.md
tags:
- kubernetes
- deployment
- extension
- control plane
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- running controllers
- built-in controllers
- custom controllers
- kube-controller-manager
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) comes with a set of [built-in controllers](/mechanism/api_server_control.md) that run inside the [kube-controller-manager](/component/kube_controller_manager.md). These built-in [controllers](/pattern/kubernetes_controller_pattern.md) provide important core behaviors. The [Deployment controller](/component/controller_roles_in_self_healing.md) and [Job](/entity/job.md) controller are examples of controllers that come as part of Kubernetes itself ("built-in" controllers). Kubernetes lets you run a resilient [control plane](/definition/kubernetes_cluster_architecture.md), so that if any of the built-in controllers were to fail, another part of the control plane will take over the work. You can find controllers that run outside the control plane, to extend Kubernetes. Or, if you want, you can write a new controller yourself. You can run your own controller as a set of Pods, or externally to Kubernetes. What fits best will depend on what that particular controller does.
