---
type: Definition
title: Windows Networking Limitations
description: Documents the networking functionality not supported on Windows nodes
  and other limitations specific to Windows container networking.
resource: source://services-networking__windows-networking.md
tags:
- windows
- limitations
- unsupported
- networking restrictions
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- unsupported Windows networking
- Windows container networking restrictions
---

The following [networking](/definition/application_exposure_service_and_ingress.md) functionality is not supported on Windows nodes: Host networking mode, Local NodePort access from the node itself (works for other nodes or external clients), More than 64 backend pods (or unique destination addresses) for a single [Service](/component/service_load_balancing.md), IPv6 communication between Windows pods connected to overlay networks, Local Traffic Policy in non-DSR mode, Outbound communication using the ICMP protocol via the win-overlay, win-bridge, or using the Azure-CNI plugin. Other [limitations](/definition/podgroup_scheduling_limitations.md): Windows reference network [plugins](/extensibility/kubectl_plugins.md) win-bridge and win-overlay do not implement CNI spec v0.4.0, due to a missing CHECK implementation. The [Flannel VXLAN](/definition/windows_network_driver_descriptions.md) CNI plugin has the following limitations on Windows: Node-pod connectivity is only possible for local pods with Flannel v0.12.0 (or higher). Flannel is restricted to using VNI 4096 and UDP port 4789.
