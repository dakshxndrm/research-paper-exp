---
type: Procedure
title: Configure Node Selector and Tolerations
description: Instructions for configuring node selector and tolerations.
resource: source://containers__runtime-class.md
tags:
- kubernetes
- nodes
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- node configuration
- tolerations
---

To ensure pods land on [nodes](/definition/kubernetes_cluster_architecture.md) supporting a specific [RuntimeClass](/entity/runtimeclass.md), set the `[scheduling](/concept/scheduling.md)` field for a RuntimeClass.
