---
type: Metric
title: Path Segment Name Requirements
description: Names must not contain specific characters.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- names
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- path segment
- name requirements
---

Some [resource](/resource/cluster_resources.md) types require their names to be able to be safely encoded as a path segment. In other words, the [name](/definition/api_group_resource_type_namespace_and_name.md) may not be "." or ".." and the name may not contain "/" or "%".
