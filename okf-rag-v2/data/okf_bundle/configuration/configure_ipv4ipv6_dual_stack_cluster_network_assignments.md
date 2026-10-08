---
type: Configuration
title: Configure IPv4/IPv6 dual-stack cluster network assignments
description: Settings required to configure IPv4/IPv6 dual-stack at the cluster component
  level.
resource: source://services-networking__dual-stack.md
tags:
- networking
- configuration
- cluster components
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- dual-stack configuration
- cluster network assignments
- kube-apiserver configuration
- kube-controller-manager configuration
- kube-proxy configuration
- kubelet configuration
---

To configure IPv4/IPv6 dual-stack, set [dual-stack cluster network](/definition/ipv4ipv6_dual_stack_networking.md) assignments: [kube-apiserver](/definition/kube_apiserver.md) with --[service](/component/service_load_balancing.md)-cluster-ip-range=<IPv4 CIDR>,<IPv6 CIDR>; [kube-controller-manager](/definition/kube_controller_manager.md) with --cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR>, --service-cluster-ip-range=<IPv4 CIDR>,<IPv6 CIDR>, and --node-cidr-mask-size-ipv4|--node-cidr-mask-size-ipv6 defaults to /24 for IPv4 and /64 for IPv6; [kube-proxy](/definition/kube_proxy_optional.md) with --cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR>; and [kubelet](/definition/kubelet.md) with --node-ip=<IPv4 IP>,<IPv6 IP>, which is required for bare metal dual-stack nodes.
