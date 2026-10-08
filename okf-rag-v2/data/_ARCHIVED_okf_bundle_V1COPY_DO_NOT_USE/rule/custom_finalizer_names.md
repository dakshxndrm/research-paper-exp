---
type: Rule
title: Custom Finalizer Names
description: Requirements for custom finalizer names.
resource: source://overview__working-with-objects__finalizers.md
tags:
- kubernetes
- finalizers
- custom finalizers
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- qualified finalizer names
- custom finalizers
---

Custom [finalizer](/procedure/using_finalizers_in_kubernetes.md) names **must** be publicly qualified finalizer names, such as `example.com/finalizer-[name](/definition/api_group_resource_type_namespace_and_name.md)`. [Kubernetes](/policy/garbage_collection_in_kubernetes.md) enforces this format; the [API server](/policy/api_server_behavior_in_kubernetes.md) rejects writes to objects where the change does not use qualified finalizer names for any custom finalizer.
