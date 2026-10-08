---
type: Metric
title: RFC 1123 Label Name Requirements
description: Names must follow specific rules.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- names
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- rfc 1123
- label name
---

Some [resource](/resource/cluster_resources.md) types require their names to follow the DNS label standard as defined in RFC 1123. This means the [name](/definition/api_group_resource_type_namespace_and_name.md) must: - contain at most 63 characters
