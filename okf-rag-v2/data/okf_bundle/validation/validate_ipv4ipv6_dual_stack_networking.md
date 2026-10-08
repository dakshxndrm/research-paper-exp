---
type: Validation
title: Validate IPv4/IPv6 dual-stack networking
description: Methods for verifying dual-stack networking configuration.
resource: source://services-networking__dual-stack.md
tags:
- networking
- validation
- cluster configuration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- dual-stack validation
- validate dual-stack
- cluster validation
---

Validate [IPv4/IPv6 dual-stack networking](/definition/ipv4ipv6_dual_stack_networking.md) using [kubectl](/definition/kubectl_command_line_tool.md) to inspect existing Services with 'kubectl get svc my-[service](/component/service_load_balancing.md) -o yaml' to check [ipFamilyPolicy](/service_configuration/service_address_family_policy.md), clusterIPs, and ipFamilies fields.
