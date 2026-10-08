---
type: Process
title: How Finalizers Work
description: The process of how finalizers work when deleting a resource.
resource: source://overview__working-with-objects__finalizers.md
tags:
- kubernetes
- finalizers
- resource deletion
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- deletion process
- resource deletion
---

When you attempt to [delete](/procedure/deleting_resources_in_kubernetes.md) a [resource](/resource/cluster_resources.md), the [API server](/policy/api_server_behavior_in_kubernetes.md) handling the delete request notices the values in the `finalizers` field and does the following: ...
