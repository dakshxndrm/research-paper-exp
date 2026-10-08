---
type: Metric
title: Maximum Name Length
description: Names must not exceed 253 characters.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- limits
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- max length
- name length
---

Most [resource](/resource/cluster_resources.md) types require a [name](/definition/api_group_resource_type_namespace_and_name.md) that can be used as a [DNS subdomain](/metric/dns_subdomain_name_requirements.md) name as defined in [RFC 1123](/metric/rfc_1123_label_name_requirements.md). This means the name must: - contain no more than 253 characters
