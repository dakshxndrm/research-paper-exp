---
type: CRIConfiguration
title: Container Runtime Interface Configuration
description: How container runtime configurations are set up for containerd and CRI-O
  through their respective configuration files.
resource: source://containers__runtime-class.md
tags:
- cri
- configuration
- containerd
- cri-o
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- CRI configuration
- containerd config
- crio config
- runtime handlers
---

## CRI Configuration

For more details on setting up CRI runtimes, see CRI installation.

### containerd

[Runtime](/definition/container_runtime.md) handlers are configured through containerd's configuration at `/etc/containerd/config.toml`. Valid handlers are configured under the runtimes section.

### CRI-O

Runtime handlers are configured through CRI-O's configuration at `/etc/crio/crio.conf`. Valid handlers are configured under the `crio.runtime` table.
