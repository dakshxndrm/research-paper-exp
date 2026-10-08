---
type: Metric
title: DNS Subdomain Name Requirements
description: Names must follow specific rules.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- names
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- dns subdomain
- name requirements
---

Most [resource](/resource/cluster_resources.md) types require a [name](/definition/api_group_resource_type_namespace_and_name.md) that can be used as a DNS subdomain name as defined in [RFC 1123](/metric/rfc_1123_label_name_requirements.md). This means the name must: - contain no more than 253 characters - contain only lowercase alphanumeric characters, '-' or '.'
