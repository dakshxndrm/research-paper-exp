---
type: Metric
title: Maximum Attempts for Unique Name Generation
description: The server will make up to 8 attempts.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- limits
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- max attempts
- unique name generation
---

Even though the [name](/definition/api_group_resource_type_namespace_and_name.md) is generated, it may conflict with existing names resulting in an HTTP 409 response. This became far less likely to happen in [Kubernetes](/policy/garbage_collection_in_kubernetes.md) v1.31 and later, since the server will make up to 8 attempts to generate a unique name before returning an HTTP 409 response.
