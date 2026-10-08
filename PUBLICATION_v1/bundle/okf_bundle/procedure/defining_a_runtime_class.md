---
type: Procedure
title: Defining a Runtime Class
description: Create a RuntimeClass with a specified name and handler.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- kubernetes
- pods
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- create runtime class
- runtime class definition
---

To define a [RuntimeClass](/entity/runtimeclass.md), create an API object with the following fields: `apiVersion`, `kind`, `metadata.[name](/definition/api_group_resource_type_namespace_and_name.md)`, and `spec.[handler](/concept/runtimeclass_resource.md)`. The `spec.handler` field specifies the handler for the RuntimeClass.
