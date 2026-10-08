---
type: Procedure
title: Scaling Applications with Kubernetes
description: The process of scaling applications using Kubernetes.
resource: source://overview.md
tags:
- kubernetes
- scaling
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kubernetes scaling
- application scaling
---

To scale an application in [Kubernetes](/policy/garbage_collection_in_kubernetes.md), you can use the `[kubectl](/tool/kubectl_command_line_tool.md)` command-line tool to update the [deployment](/entity/deployment.md) configuration and apply it to your cluster. This will automatically adjust the number of replicas based on the specified scaling policy.
