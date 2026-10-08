---
type: Egress Traffic
title: Egress traffic for dual-stack clusters
description: Mechanisms for enabling off-cluster egress routing from Pods in dual-stack
  configurations.
resource: source://services-networking__dual-stack.md
tags:
- networking
- egress
- ipv6
- cluster configuration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- off-cluster egress
- Internet egress
- IP masquerading
- ip-masq-agent
---

To enable egress traffic to reach off-cluster destinations such as the public Internet from a Pod using non-publicly routable IPv6 addresses, the Pod must use a publicly routed [IPv6 address](/address_types/endpointslice_address_types_ipv4_and_ipv6.md) via mechanisms such as transparent proxying or IP masquerading. The ip-masq-agent project supports IP masquerading on dual-stack clusters. Ensure the CNI provider supports IPv6.
