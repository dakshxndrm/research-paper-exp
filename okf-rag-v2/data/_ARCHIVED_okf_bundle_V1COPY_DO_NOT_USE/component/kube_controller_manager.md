---
type: Component
title: kube-controller-manager
description: Details the function of the kube-controller-manager and provides examples
  of the various controllers it combines.
resource: source://architecture.md
tags:
- kubernetes
- component
- control plane
- controller
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Node controller
- Job controller
- EndpointSlice controller
- ServiceAccount controller
---

The `kube-controller-manager` combines several logically independent control loops into a single binary that runs as a single [process](/concept/pod_definition.md). It makes global decisions about the cluster and detects and responds to cluster events. Examples of [controllers](/pattern/kubernetes_controller_pattern.md) it manages include: 
- [Node controller](/procedure/node_controller_functions.md): Responsible for noticing and responding when [nodes](/definition/kubernetes_cluster_architecture.md) go down.
- [Job](/entity/job.md) controller: Watches for Job objects that represent one-off tasks, then creates Pods to run those tasks to completion.
- [EndpointSlice controller](/entity/endpointslice_controller.md): Populates EndpointSlice objects (to provide a link between [Services](/procedure/configuring_load_balancing_and_services.md) and Pods).
- ServiceAccount controller: Creates default ServiceAccounts for new namespaces.
