---
type: Definition
title: Windows Flannel CNI Plugin Support
description: Describes the Flannel CNI plugin support on Windows including VXLAN and
  host-gateway backends, configuration aggregation, and version limitations.
resource: source://services-networking__windows-networking.md
tags:
- windows
- flannel
- cni plugin
- vxlan
- host-gateway
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Flannel Windows
- Flannel CNI Windows
- Flannel daemon Windows
- Flannel VXLAN Windows
---

The Flannel CNI plugin is also supported on Windows via the VXLAN network backend (Beta support; delegates to [win-overlay](/definition/windows_network_driver_descriptions.md)) and host-[gateway](/api_kind/gateway_resource.md) network backend (stable support; delegates to win-bridge). This plugin supports delegating to one of the reference [CNI plugins](/definition/external_components_implementing_kubernetes_networking.md) (win-overlay, win-bridge), to work in conjunction with Flannel daemon on Windows (Flanneld) for automatic node subnet lease assignment and HNS network creation. This plugin reads in its own configuration file (cni.conf), and aggregates it with the environment variables from the FlannelD generated subnet.env file. It then delegates to one of the reference CNI [plugins](/extensibility/kubectl_plugins.md) for network plumbing, and sends the correct configuration containing the node-assigned subnet to the IPAM plugin (for example: host-local). Node-pod connectivity is only possible for local pods with Flannel v0.12.0 (or higher). Flannel is restricted to using VNI 4096 and UDP port 4789.
