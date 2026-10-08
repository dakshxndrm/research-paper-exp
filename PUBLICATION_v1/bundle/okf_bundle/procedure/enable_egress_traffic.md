---
type: Procedure
title: Enable Egress Traffic
description: Procedure to enable egress traffic for Kubernetes clusters.
resource: source://services-networking__dual-stack.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- enable egress
- dual-stack egress
---

If you want to enable egress traffic in order to reach off-cluster destinations, ensure your CNI provider supports IPv6 and use a mechanism such as transparent proxying or IP masquerading.
