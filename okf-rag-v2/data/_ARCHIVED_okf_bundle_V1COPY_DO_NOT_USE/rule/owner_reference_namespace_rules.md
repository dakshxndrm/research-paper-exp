---
type: Rule
title: Owner Reference Namespace Rules
description: Defines the rules and restrictions for owner references across namespaces
  and for cluster-scoped dependents.
resource: source://architecture__garbage-collection.md
tags:
- owner references
- namespaces
- cluster-scoped
- validation
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- cross-namespace owner references
- cluster-scoped owner references
- OwnerRefInvalidNamespace
---

[Cross-namespace owner references](/rule/cross_namespace_owner_references.md) are disallowed by [design](/design_principle/controller_design_principles.md). Namespaced dependents can specify cluster-scoped or namespaced owners, but a namespaced owner **must** exist in the same [namespace](/definition/api_group_resource_type_namespace_and_name.md) as the dependent. If it does not, the [owner reference](/definition/kubernetes_owner_references.md) is treated as absent, and the dependent becomes subject to deletion once all owners are verified absent.

Cluster-scoped dependents can only specify cluster-scoped owners. In v1.20+, if a cluster-scoped dependent specifies a namespaced kind as an owner, it is treated as having an unresolvable owner reference and cannot be garbage collected.

In v1.20+, if the garbage collector detects an invalid cross-namespace `[ownerReference](/metric/invalid_owner_references.md)` or a cluster-scoped dependent with an `ownerReference` [referencing](/rule/referencing_non_existent_podgroups.md) a namespaced kind, a warning Event with a reason of `OwnerRefInvalidNamespace` and an `involvedObject` of the invalid dependent is reported. This can be checked by running `[kubectl](/tool/kubectl_command_line_tool.md) get events -A --field-selector=reason=OwnerRefInvalidNamespace`.
