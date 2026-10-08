---
type: Plugins
title: Extending kubectl with Plugins
description: How to extend kubectl with plugins that add new sub-commands.
resource: source://overview__kubectl.md
tags:
- kubernetes
- plugins
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kubectl plugin
- k8s plugin
---

You can extend `[kubectl](/tool/kubectl_command_line_tool.md)` with plugins that add new sub-commands. Plugins are standalone binaries that follow the `kubectl-<[plugin](/plugin/gangscheduling_plugin.md)-[name](/definition/api_group_resource_type_namespace_and_name.md)>` naming convention.
