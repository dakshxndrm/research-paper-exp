---
type: Event
title: OwnerRefInvalidNamespace Event
description: In v1.20+, the garbage collector reports a warning Event with reason
  OwnerRefInvalidNamespace when it detects an invalid cross-namespace ownerReference
  or a cluster-scoped dependent with a namespaced kind as owner; the involvedObject
  is the invalid dependent.
resource: source://overview__working-with-objects__owners-dependents.md
tags:
- kubernetes
- v1.20
- garbage collector
- event
- ownerrefinvalidnamespace
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- OwnerRefInvalidNamespace
- garbage collector event
- invalid namespace event
- warning event
---

In v1.20+, if the garbage collector detects an invalid cross-namespace ownerReference, or a cluster-scoped dependent with an ownerReference referencing a namespaced kind, a warning Event with a reason of OwnerRefInvalidNamespace and an involvedObject of the invalid dependent is reported. You can check for that kind of Event by running [kubectl](/definition/kubectl_command_line_tool.md) get events -A --field-selector=reason=OwnerRefInvalidNamespace.
