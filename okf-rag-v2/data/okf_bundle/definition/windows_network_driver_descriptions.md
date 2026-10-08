---
type: Definition
title: Windows Network Driver Descriptions
description: Provides detailed descriptions of each Windows network driver including
  L2bridge, L2tunnel, Overlay, Transparent, and NAT modes, and their characteristics.
resource: source://services-networking__windows-networking.md
tags:
- windows
- network driver
- l2bridge
- l2tunnel
- overlay
- transparent
- nat
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- win-bridge
- win-overlay
- Azure-CNI
- Flannel VXLAN
- Flannel host-gateway
- ovn-kubernetes
---

The following table lists the out-of-tree [plugins](/extensibility/kubectl_plugins.md) supported on Windows, with recommendations on when to use each CNI: [table with columns: Network Driver, Description, Container Packet Modifications, Network Plugins, Network Plugin Characteristics]. L2bridge: Containers attached to an external vSwitch, connected to the underlay network with MAC rewritten to host MAC. L2tunnel: Special case of l2bridge used on Azure, all packets sent to virtualization host where SDN policy is applied. Overlay: Containers given vNIC connected to external vSwitch, each overlay network gets its own IP subnet defined by custom IP prefix, uses VXLAN encapsulation. Transparent: Requires external vSwitch, enables intra-[pod communication](/definition/pod_network_communication.md) via logical networks, packets encapsulated via GENEVE or STT tunneling. NAT: Containers given vNIC connected to internal vSwitch, DNS/DHCP provided using internal component called WinNAT.
