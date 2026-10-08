---
type: Definition
title: Windows Container Network Configuration
description: Explains how Windows container network configuration differs from Linux,
  including registry-based configuration and the need for Windows APIs.
resource: source://services-networking__windows-networking.md
tags:
- windows
- network configuration
- registry
- hns
- apis
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Windows network configuration
- container network configuration Windows
- HNS configuration
- registry-based network config
---

Many configurations such as DNS, routes, and metrics are stored in the Windows registry database rather than as files inside /etc, which is how Linux stores those configurations. The Windows registry for the container is separate from that of the host, so concepts like mapping /etc/resolv.conf from the host into a container don't have the same effect they would on Linux. These must be configured using Windows APIs run in the context of that container. Therefore CNI implementations need to call the HNS instead of relying on file mappings to pass network details into the pod or container.
