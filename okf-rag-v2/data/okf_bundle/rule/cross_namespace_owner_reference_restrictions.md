---
type: Rule
title: Cross-Namespace Owner Reference Restrictions
description: Cross-namespace owner references are disallowed by design; namespaced
  dependents can only specify owners in the same namespace, and cluster-scoped dependents
  can only specify cluster-scoped owners; in v1.20+, violations trigger an OwnerRefInvalidNamespace
  event.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- namespace
- owner reference
- cross-namespace
- v1.20
- garbage collection
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cross-namespace restriction
- namespace owner reference
- invalid owner reference
- OwnerRefInvalidNamespace event
---

Cross-namespace [owner references](/definition/owner_references_and_dependents.md) are disallowed by design. Namespaced dependents can specify cluster-scoped or namespaced owners. A namespaced owner must exist in the same namespace as the dependent. If it does not, the [owner reference](/mechanism/owner_references_in_object_specifications.md) is treated as absent, and the dependent is subject to deletion once all owners are verified absent. Cluster-scoped dependents can only specify cluster-scoped owners. In v1.20+, if a cluster-scoped dependent specifies a namespaced kind as an owner, it is treated as having an unresolvable owner reference, and is not able to be garbage collected.
