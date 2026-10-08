---
type: Mechanism
title: API Server Mediation
description: Controllers communicate desired state changes to the Kubernetes API server,
  which then propagates changes to relevant cluster components such as kubelet for
  Pod scheduling.
resource: source://architecture__controller.md
tags:
- kubernetes
- api server
- control plane
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- API server interaction
- controller API communication
---

The [job controller](/procedure/job_controller_workflow.md) tells the [API server](/definition/kube_apiserver.md) to [create](/operations/kubectl_resource_management_operations.md) or remove Pods. Other components in the [control plane](/definition/control_plane_components.md) act on the new information (there are new Pods to schedule and run), and eventually the work is done. The Job controller does not run any Pods or containers itself; it communicates with the API server which coordinates the [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) and running of Pods.
