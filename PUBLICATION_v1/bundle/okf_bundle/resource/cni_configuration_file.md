---
type: Resource
title: CNI Configuration File
description: The file that contains the CNI configuration.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- cni config
- config file
---

You must add the `bandwidth` [plugin](/plugin/gangscheduling_plugin.md) to your CNI configuration file (default `/etc/cni/net.d`) and ensure that the binary is included in your [CNI bin dir](/resource/cni_bin_dir.md) (default `/opt/cni/bin`).
