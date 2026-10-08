---
type: Definition
title: Windows Network Modes
description: 'Lists and describes the five networking drivers/modes supported on Windows:
  L2bridge, L2tunnel, Overlay, Transparent, and NAT.'
resource: source://services-networking__windows-networking.md
tags:
- windows
- network mode
- l2bridge
- l2tunnel
- overlay
- transparent
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- windows network mode
- L2bridge mode
- L2tunnel mode
- overlay mode
- transparent mode
- NAT mode
---

Windows supports five different [networking](/definition/application_exposure_service_and_ingress.md) drivers/modes: L2bridge, L2tunnel, Overlay (Beta), Transparent, and NAT. In a heterogeneous cluster with Windows and Linux [worker nodes](/definition/node_components.md), you need to select a networking solution that is compatible on both Windows and Linux. The following table lists the out-of-tree [plugins](/extensibility/kubectl_plugins.md) are supported on Windows, with recommendations on when to use each CNI: [table omitted for brevity - see source]. As outlined above, the Flannel CNI plugin is also supported on Windows via the VXLAN network backend (Beta support; delegates to [win-overlay](/definition/windows_network_driver_descriptions.md)) and host-[gateway](/api_kind/gateway_resource.md) network backend (stable support; delegates to win-bridge). This plugin supports delegating to one of the reference [CNI plugins](/definition/external_components_implementing_kubernetes_networking.md) (win-overlay, win-bridge), to work in conjunction with Flannel daemon on Windows (Flanneld) for automatic node subnet lease assignment and HNS network creation.
