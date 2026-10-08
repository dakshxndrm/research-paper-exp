---
type: Procedure
title: Deploying Applications with Kubernetes
description: The process of deploying applications using Kubernetes.
resource: source://overview.md
tags:
- kubernetes
- deployment
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kubernetes deployment
- application deployment
---

To deploy an application with [Kubernetes](/policy/garbage_collection_in_kubernetes.md), you first need to create a container image and push it to a registry. Then, you can use the `[kubectl](/tool/kubectl_command_line_tool.md)` command-line tool to create a [deployment](/entity/deployment.md) configuration and apply it to your cluster.
