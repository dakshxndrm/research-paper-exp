---
type: Definition
title: Owner References vs Labels and Selectors
description: The difference between owner references and labels and selectors in Kubernetes.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- labels
- selectors
---

[Ownership](/policy/podgroup_ownership_and_lifecycle.md) is different from the [labels](/concept/owner_references_and_labels.md) and selectors mechanism that some resources also use. [Owner references](/definition/kubernetes_owner_references.md) help different parts of [Kubernetes](/policy/garbage_collection_in_kubernetes.md) avoid interfering with objects they don’t control.
