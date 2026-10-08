---
type: Procedure
title: Monitoring Applications with Kubernetes
description: The process of monitoring applications using Kubernetes.
resource: source://overview.md
tags:
- kubernetes
- monitoring
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kubernetes monitoring
- application monitoring
---

To monitor an application in [Kubernetes](/policy/garbage_collection_in_kubernetes.md), you can use the `[kubectl](/tool/kubectl_command_line_tool.md)` command-line tool to create a new [deployment](/entity/deployment.md) configuration and apply it to your cluster. This will automatically collect metrics and logs for the application.
