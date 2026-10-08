---
type: Metric
title: Invalid Owner References
description: What happens when an invalid owner reference is detected in Kubernetes.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- invalid owner reference
- ownerReference
---

In v1.20+, if a cluster-scoped dependent specifies a namespaced kind as an owner, it is treated as having an unresolvable [owner reference](/definition/kubernetes_owner_references.md), and is not able to be garbage collected.
