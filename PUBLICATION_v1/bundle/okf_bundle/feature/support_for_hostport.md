---
type: Feature
title: Support for hostPort
description: The CNI networking plugin supports `hostPort`.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- hostport
- cni support
---

The CNI networking [plugin](/plugin/gangscheduling_plugin.md) supports `hostPort`. You can use the official portmap plugin offered by the [CNI plugin](/implementation/pod_network_implementation_cni.md) team or use your own plugin with portMapping functionality.
