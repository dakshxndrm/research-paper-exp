---
type: Extensibility
title: kubectl plugins
description: kubectl can be extended with plugins that add new sub-commands, managed
  via the Krew plugin manager or standalone binaries following naming conventions.
resource: source://overview__kubectl.md
tags:
- plugins
- extensibility
- krew
- sub-commands
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- plugins
- plugin manager
- Krew
- sub-commands
- plugin-name
---

You can extend `[kubectl](/definition/kubectl_command_line_tool.md)` with plugins that add new sub-commands. Plugins are standalone binaries that follow the `kubectl-<plugin-name>` naming convention. The Kubernetes community maintains many plugins, and you can manage them with the Krew plugin manager.
