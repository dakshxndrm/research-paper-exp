---
type: Rule
title: Cross-Namespace Owner References
description: The rules for cross-namespace owner references in Kubernetes.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- cross-namespace
- owner reference
---

[Cross-namespace owner references](/rule/owner_reference_namespace_rules.md) are disallowed by [design](/design_principle/controller_design_principles.md). Namespaced dependents can specify cluster-scoped or namespaced owners.
