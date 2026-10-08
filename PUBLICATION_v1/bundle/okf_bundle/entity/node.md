---
type: Entity
title: Node
description: A Node represents a physical host.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- nodes
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- physical host
---

In cases when objects represent a physical entity, like a [Node](/entity/worker_node.md) representing a physical host, when the host is re-created under the same [name](/definition/api_group_resource_type_namespace_and_name.md) without deleting and re-creating the Node, [Kubernetes](/policy/garbage_collection_in_kubernetes.md) treats the new host as the old one, which may lead to inconsistencies.
