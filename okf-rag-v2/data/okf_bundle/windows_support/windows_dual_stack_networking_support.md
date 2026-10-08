---
type: Windows Support
title: Windows dual-stack networking support
description: Limitations and capabilities of dual-stack networking on Windows nodes.
resource: source://services-networking__dual-stack.md
tags:
- networking
- windows
- node configuration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Windows networking
- Windows dual-stack
- Windows IPv4/IPv6
---

Kubernetes on Windows does not support single-stack IPv6-only [networking](/definition/application_exposure_service_and_ingress.md). Dual-stack IPv4/IPv6 networking for pods and nodes with single-family services is supported. Dual-stack can be used with l2bridge networks. Overlay (VXLAN) networks on Windows do not support [dual-stack networking](/definition/ipv4ipv6_dual_stack_networking.md).
