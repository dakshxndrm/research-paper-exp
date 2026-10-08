---
type: Category
title: Built-in Controllers
description: Core controllers included in Kubernetes kube-controller-manager that
  provide essential cluster behaviors such as Deployment and Job management.
resource: source://architecture__controller.md
tags:
- kubernetes
- control plane
- built-in
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kube-controller-manager
- core controllers
---

Kubernetes comes with a set of built-in controllers that run inside the [kube-controller-manager](/definition/kube_controller_manager.md). These built-in controllers provide important core behaviors. The [Deployment controller](/component/replicaset_and_deployment_controllers.md) and [Job controller](/procedure/job_controller_workflow.md) are examples of controllers that come as part of Kubernetes itself. Kubernetes lets you run a resilient [control plane](/definition/control_plane_components.md), so that if any of the built-in controllers were to fail, another part of the control plane will take over the work.
