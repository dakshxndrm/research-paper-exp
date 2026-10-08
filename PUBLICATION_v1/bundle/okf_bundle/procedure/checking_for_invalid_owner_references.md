---
type: Procedure
title: Checking for Invalid Owner References
description: How to check for invalid owner references in Kubernetes.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- ownership
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- invalid owner reference
- ownerReference
---

You can check for that kind of Event by running `[kubectl](/tool/kubectl_command_line_tool.md) get events -A --field-selector=reason=[OwnerRefInvalidNamespace](/rule/owner_reference_namespace_rules.md)`.
