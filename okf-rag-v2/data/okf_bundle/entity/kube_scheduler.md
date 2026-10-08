---
type: Entity
title: kube-scheduler
description: The default Kubernetes scheduler that runs as part of the control plane
  and selects optimal nodes for newly created or unscheduled Pods.
resource: source://scheduling-eviction__kube-scheduler.md
tags:
- scheduler
- control plane
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kube scheduler
- default scheduler
- scheduling component
---

# [kube-scheduler](/definition/kube_scheduler.md)

kube-scheduler is the default scheduler for Kubernetes and runs as part of the [control plane](/definition/control_plane_components.md). kube-scheduler is designed so that, if you want and need to, you can write your own [scheduling](/scheduling/runtimeclass_scheduling_constraints.md) component and use that instead. Kube-scheduler selects an optimal node to run newly created or not yet scheduled (unscheduled) pods. Since containers in pods - and pods themselves - can have different requirements, the scheduler filters out any nodes that don't meet a Pod's specific scheduling needs. Alternatively, the API lets you specify a node for a Pod when you [create](/operations/kubectl_resource_management_operations.md) it, but this is unusual and is only done in special cases.
