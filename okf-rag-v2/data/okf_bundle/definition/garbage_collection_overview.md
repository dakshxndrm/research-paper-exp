---
type: Definition
title: Garbage Collection Overview
description: Garbage collection in Kubernetes cleans up resources such as terminated
  pods, completed jobs, objects without owner references, unused containers and images,
  and node lease objects.
resource: source://architecture__garbage-collection.md
tags:
- garbage-collection
- overview
timestamp: '2026-09-02T17:04:11+00:00'
---

# [Garbage Collection](/definition/supporting_concepts_garbage_collection.md)

This allows the clean up of resources like the following:

* Terminated pods
* Completed Jobs
* Objects without [owner references](/definition/owner_references_and_dependents.md)
* Unused containers and container images
* Dynamically provisioned PersistentVolumes with a StorageClass reclaim policy of [Delete](/operations/kubectl_resource_management_operations.md)
* Stale or expired CertificateSigningRequests (CSRs)
* Nodes deleted in the following scenarios:
  * On a cloud when the cluster uses a [cloud controller manager](/definition/cloud_controller_manager_overview.md)
  * On-premises when the cluster uses an addon similar to a cloud [controller manager](/definition/kube_controller_manager.md)
* Node Lease objects
