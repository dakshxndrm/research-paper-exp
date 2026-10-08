---
type: Definition
title: Kubernetes Owner References
description: Explains how owner references link Kubernetes objects, indicating dependencies
  for cleanup.
resource: source://architecture__garbage-collection.md
tags:
- owner references
- dependencies
- object management
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- owner references
- owner reference
- Ownership
---

Many objects in [Kubernetes](/policy/garbage_collection_in_kubernetes.md) link to each other through *owner references*. These references inform the [control plane](/definition/kubernetes_cluster_architecture.md) which objects are dependent on others, allowing for the cleanup of related resources before an object is deleted. Kubernetes typically manages owner references automatically.

[Ownership](/policy/podgroup_ownership_and_lifecycle.md) differs from the [labels](/concept/owner_references_and_labels.md) and [selectors](/definition/owner_references_vs_labels_and_selectors.md) mechanism. For instance, a [Service](/entity/kubernetes_service.md) uses *labels* to identify its `EndpointSlice` objects, but each `EndpointSlice` also has an owner reference to the Service. This helps different parts of Kubernetes avoid interfering with objects they do not control.
