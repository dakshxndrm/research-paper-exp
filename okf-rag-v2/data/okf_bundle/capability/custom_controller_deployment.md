---
type: Capability
title: Custom Controller Deployment
description: Users can run their own controllers outside the control plane or as a
  set of Pods to extend Kubernetes functionality for specific use cases.
resource: source://architecture__controller.md
tags:
- kubernetes
- custom controller
- extension
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- custom controller
- external controller
- controller as Pods
---

You can find controllers that run outside the [control plane](/definition/control_plane_components.md), to extend Kubernetes. Or, if you want, you can write a new controller yourself. You can run your own controller as a set of Pods, or externally to Kubernetes. What fits best will depend on what that particular controller does.
