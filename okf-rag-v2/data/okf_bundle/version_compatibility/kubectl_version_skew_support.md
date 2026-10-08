---
type: Version compatibility
title: kubectl version skew support
description: kubectl supports a version skew of plus-or-minus one minor version relative
  to the cluster's control plane to avoid unexpected behavior.
resource: source://overview__kubectl.md
tags:
- version
- compatibility
- skew
- control plane
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- version skew
- compatible version
- version compatibility
- control plane version
- minor version
---

The `[kubectl](/definition/kubectl_command_line_tool.md)` tool supports a version skew of plus-or-minus one minor version relative to the cluster's [control plane](/definition/control_plane_components.md). For example, `kubectl` v1.32 works with control planes at v1.31, v1.32, and v1.33. Using a compatible version avoids unexpected behavior.
