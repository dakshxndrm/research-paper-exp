---
type: Definition
title: Windows Direct Server Return (DSR)
description: Explains Direct Server Return load balancing mode where IP address fixups
  and LBNAT occur at the container vSwitch port directly, providing performance optimizations.
resource: source://services-networking__windows-networking.md
tags:
- windows
- dsr
- load balancing
- performance
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Direct Server Return
---

[Load balancing](/component/service_load_balancing.md) mode where the IP address fixups and the LBNAT occurs at the container vSwitch port directly; service traffic arrives with the source IP set as the originating [pod IP](/definition/pod_ip_addressing_and_namespaces.md). This provides performance optimizations by allowing the return traffic routed through load balancers to bypass the load balancer and respond directly to the client; reducing load on the load balancer and also reducing overall latency.
