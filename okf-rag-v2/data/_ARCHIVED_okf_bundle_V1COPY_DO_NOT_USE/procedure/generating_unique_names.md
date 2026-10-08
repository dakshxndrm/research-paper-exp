---
type: Procedure
title: Generating Unique Names
description: Kubernetes can generate a unique name when provided with a prefix.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- names
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- generate name
- unique name generation
---

The server may generate a [name](/definition/api_group_resource_type_namespace_and_name.md) when `generateName` is provided instead of `name` in a [resource](/resource/cluster_resources.md) create request. When `generateName` is used, the provided value is used as a name prefix, which server appends a generated suffix to.
