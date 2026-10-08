---
type: Entity
title: Flannel CNI Plugin
description: Description of the Flannel CNI plugin.
resource: source://services-networking__windows-networking.md
tags:
- windows
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- flannel
---

The Flannel [CNI plugin](/implementation/pod_network_implementation_cni.md) is also supported on Windows via the VXLAN network backend (**Beta support** ; delegates to win-overlay) and host-[gateway](/api_kind/gateway.md) network backend (stable support; delegates to win-bridge).
