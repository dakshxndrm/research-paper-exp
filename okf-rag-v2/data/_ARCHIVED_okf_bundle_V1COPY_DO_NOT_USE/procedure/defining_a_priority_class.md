---
type: Procedure
title: Defining a Priority Class
description: Create a PriorityClass with a specified name and integer priority value.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- kubernetes
- pods
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- create priority class
- priority class definition
---

To define a [PriorityClass](/entity/priorityclass.md), create an API object with the following fields: `apiVersion`, `kind`, `metadata.[name](/definition/api_group_resource_type_namespace_and_name.md)`, and `spec.priority`. The `spec.priority` field specifies the [integer priority](/metric/priority_value.md) value.
