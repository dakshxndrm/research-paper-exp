---
type: Policy
title: Owner References in Object Specifications
description: How owner references are used in Kubernetes object specifications.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- owner reference
- metadata.ownerReferences
---

Dependent objects have a `metadata.[ownerReferences](/procedure/configuring_owner_relationships_manually.md)` field that references their owner object. A valid [owner reference](/definition/kubernetes_owner_references.md) consists of the object name and a UID within the same [namespace](/definition/api_group_resource_type_namespace_and_name.md) as the dependent object.
