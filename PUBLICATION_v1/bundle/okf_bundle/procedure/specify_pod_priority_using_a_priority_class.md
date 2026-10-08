---
type: Procedure
title: Specify Pod Priority using a Priority Class
description: Assign a PriorityClass to a Pod.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- kubernetes
- pods
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- assign priority class
- pod priority assignment
---

To specify [pod priority](/policy/priority_classes.md) using a [PriorityClass](/entity/priorityclass.md), add the `priorityClassName` field to the Pod specification and set it to the [name](/definition/api_group_resource_type_namespace_and_name.md) of the desired PriorityClass.
