---
type: Policy
title: Finalizer Purpose
description: Purpose of finalizers in controlling garbage collection.
resource: source://overview__working-with-objects__finalizers.md
tags:
- kubernetes
- finalizers
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- garbage collection
- cleanup tasks
---

You can use finalizers to control [garbage collection](/concept/garbage_collection.md) of objects by alerting [controllers](/pattern/kubernetes_controller_pattern.md) to perform specific cleanup tasks before deleting the target [resource](/resource/cluster_resources.md).
