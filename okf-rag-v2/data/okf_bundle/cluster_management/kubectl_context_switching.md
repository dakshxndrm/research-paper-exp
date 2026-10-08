---
type: Cluster management
title: kubectl context switching
description: kubectl can switch between multiple clusters, users, and contexts defined
  in the kubeconfig file.
resource: source://overview__kubectl.md
tags:
- context
- cluster switching
- kubeconfig
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- context switching
- use-context
- change context
- multiple clusters
- multiple users
---

Because your [kubeconfig](/configuration/kubeconfig_file_location_and_environment.md) can define multiple clusters, users, and contexts, you can use `[kubectl](/definition/kubectl_command_line_tool.md)` to switch between clusters without reconfiguring your environment. Run `kubectl config use-context` to change the active context.
