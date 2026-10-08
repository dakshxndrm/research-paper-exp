---
type: Feature
title: Support for Traffic Shaping
description: The CNI networking plugin supports pod ingress and egress traffic shaping.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- traffic shaping
- cni feature
---

The CNI networking [plugin](/plugin/gangscheduling_plugin.md) also supports pod [ingress](/api/gateway_api.md) and egress traffic shaping. You can use the official bandwidth plugin offered by the [CNI plugin](/implementation/pod_network_implementation_cni.md) team or use your own plugin with bandwidth control functionality.
