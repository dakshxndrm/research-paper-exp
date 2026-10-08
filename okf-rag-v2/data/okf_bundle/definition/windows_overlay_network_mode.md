---
type: Definition
title: Windows Overlay Network Mode
description: Describes the Overlay network mode for Windows containers, including
  VXLAN encapsulation, IP subnet isolation, and requirements.
resource: source://services-networking__windows-networking.md
tags:
- windows
- overlay
- vxlan
- ip subnet
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- win-overlay
- overlay network Windows
- VXLAN overlay
- overlay mode Windows
---

Containers are given a vNIC connected to an external vSwitch. Each overlay network gets its own IP subnet, defined by a custom IP prefix. The overlay network driver uses VXLAN encapsulation. This option should be used when virtual container networks are desired to be isolated from underlay of hosts (e.g. for security reasons). Allows for IPs to be re-used for different overlay networks (which have different VNID tags) if you are restricted on IPs in your datacenter. This option requires KB4489899 on Windows Server 2019.
