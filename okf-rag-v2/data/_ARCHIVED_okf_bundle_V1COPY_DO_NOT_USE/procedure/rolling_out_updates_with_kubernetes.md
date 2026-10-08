---
type: Procedure
title: Rolling Out Updates with Kubernetes
description: The process of rolling out updates using Kubernetes.
resource: source://overview.md
tags:
- kubernetes
- updates
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kubernetes update
- application update
---

To roll out an update in [Kubernetes](/policy/garbage_collection_in_kubernetes.md), you can use the `[kubectl](/tool/kubectl_command_line_tool.md)` command-line tool to create a new [deployment](/entity/deployment.md) configuration and apply it to your cluster. This will automatically update the application without downtime.
