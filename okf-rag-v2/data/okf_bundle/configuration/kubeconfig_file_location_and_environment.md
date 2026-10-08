---
type: Configuration
title: kubeconfig file location and environment
description: kubectl looks for a config file in the $HOME/.kube directory and can
  use environment variables or flags to specify alternative configuration files.
resource: source://overview__kubectl.md
tags:
- configuration
- kubeconfig
- environment variable
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- kubeconfig
- KUBECONFIG environment variable
- --kubeconfig flag
- kubeconfig file
---

For configuration, `[kubectl](/definition/kubectl_command_line_tool.md)` looks for a file named `config` in the `$HOME/.kube` directory. You can specify other kubeconfig files by setting the `KUBECONFIG` environment variable or by setting the `--kubeconfig` flag.
