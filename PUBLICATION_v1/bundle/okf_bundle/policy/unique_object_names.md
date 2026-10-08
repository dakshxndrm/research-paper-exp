---
type: Policy
title: Unique Object Names
description: Each object must have a unique name within its type and namespace.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- namespaces
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- unique names
- object naming
---

Each object in your cluster has a _Name_ that is unique for that type of [resource](/resource/cluster_resources.md). Every [Kubernetes](/policy/garbage_collection_in_kubernetes.md) object also has a _UID_ that is unique across your whole cluster.
