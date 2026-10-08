---
type: Finalizer
title: Ownership and Finalizers
description: When deleting a Kubernetes resource, the API server allows the managing
  controller to process finalizer rules; finalizers prevent accidental deletion of
  resources the cluster may still need, such as PersistentVolume with kubernetes.io/pv-protection
  finalizer that remains in Terminating status until released from all bound Pods.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- finalizer
- deletion
- resource management
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- finalizer
- foreground finalizer
- orphan finalizer
- kubernetes.io/pv-protection
- deletion finalizer
---

When you tell Kubernetes to [delete](/operations/kubectl_resource_management_operations.md) a resource, the [API server](/definition/kube_apiserver.md) allows the managing controller to process any finalizer rules for the resource. [Finalizers](/definition/what_are_finalizers.md) prevent accidental deletion of resources your cluster may still need to function correctly. For example, if you try to delete a [PersistentVolume](/component/persistentvolume_controller.md) that is still in use by a Pod, the deletion does not happen immediately because the PersistentVolume has the [kubernetes.io/pv-protection](/example/persistentvolume_protection_finalizer.md) finalizer on it. Instead, the volume remains in the Terminating status until Kubernetes clears the finalizer, which only happens after the PersistentVolume is no longer bound to a Pod.
