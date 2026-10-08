---
type: Definition
title: Kubernetes Garbage Collection Purpose
description: Describes the function of Kubernetes garbage collection and lists the
  types of resources it cleans up.
resource: source://architecture__garbage-collection.md
tags:
- garbage collection
- cleanup
- resources
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Garbage Collection
- clean up of resources
---

[Kubernetes](/policy/garbage_collection_in_kubernetes.md) [Garbage Collection](/concept/garbage_collection.md) allows the clean up of resources such as:

*   Terminated pods
*   Completed Jobs
*   Objects without [owner references](/definition/kubernetes_owner_references.md)
*   Unused containers and container images
*   Dynamically provisioned PersistentVolumes with a StorageClass reclaim policy of [Delete](/procedure/deleting_resources_in_kubernetes.md)
*   Stale or expired CertificateSigningRequests (CSRs)
*   [Nodes](/definition/kubernetes_cluster_architecture.md) deleted in the following scenarios:
    *   On a cloud when the cluster uses a [cloud controller manager](/entity/cloud_controller_manager.md)
    *   On-premises when the cluster uses an [addon](/entity/addon.md) similar to a cloud [controller](/pattern/kubernetes_controller_pattern.md) manager
*   [Node](/entity/node.md) Lease objects
