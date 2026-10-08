---
type: Procedure
title: Specify Pod Runtime using a Runtime Class
description: Assign a RuntimeClass to a Pod.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- kubernetes
- pods
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- assign runtime class
- pod runtime assignment
---

To specify pod [runtime](/entity/container_runtime_1.md) using a [RuntimeClass](/entity/runtimeclass.md), add the `runtimeClassName` field to the Pod specification and set it to the [name](/definition/api_group_resource_type_namespace_and_name.md) of the desired RuntimeClass.
