---
type: Relationship
title: Finalizers and owner references
description: Finalizers are processed when deletion targets have owner references,
  which can block deletion of dependent objects.
resource: source://overview__working-with-objects__finalizers.md
tags:
- owner-reference
- deletion-blocking
- troubleshooting
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- owner reference finalizer interaction
- finalizer blocking dependent deletion
- stuck deletion troubleshooting
---

Like labels, [owner references](/definition/owner_references_and_dependents.md) describe relationships between objects, but are used for a different purpose. When a controller manages objects like Pods, it uses owner references to determine which Pods need cleanup if the creator is deleted. Kubernetes processes [finalizers](/definition/what_are_finalizers.md) when it identifies owner references on a resource targeted for deletion. Finalizers can block the deletion of [dependent objects](/definition/owner_and_dependent_objects.md), causing the targeted owner object to remain longer than expected. In cases where objects are stuck in a deleting state, manually removing finalizers should be avoided as it can lead to issues in the cluster.
