---
type: Component
title: cloud-controller-manager
description: Explains the purpose of the cloud-controller-manager, its deployment
  conditions, and the types of cloud-dependent controllers it runs.
resource: source://architecture.md
tags:
- kubernetes
- component
- control plane
- cloud provider
- controller
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Node controller
- Route controller
- Service controller
---

The `cloud-controller-manager` only runs [controllers](/pattern/kubernetes_controller_pattern.md) that are specific to your cloud provider. If [Kubernetes](/policy/garbage_collection_in_kubernetes.md) is running on premises, or in a learning environment inside a PC, the cluster does not have a `cloud-controller-manager`. As with the `[kube-controller-manager](/component/kube_controller_manager.md)`, it combines several logically independent control loops into a single binary that runs as a single [process](/concept/pod_definition.md). You can scale horizontally (run more than one copy) to improve performance or to help tolerate failures. The following controllers can have cloud provider dependencies:
- [Node controller](/procedure/node_controller_functions.md): For checking the cloud provider to determine if a [node](/entity/node.md) has been deleted in the cloud after it stops responding.
- [Route controller](/procedure/route_controller_functions.md): For setting up routes in the underlying cloud infrastructure.
- [Service controller](/procedure/service_controller_functions.md): For creating, updating and deleting cloud provider load balancers.
