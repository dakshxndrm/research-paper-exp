---
type: Metric
title: Maximum Addresses per Subset
description: A maximum of 1000 addresses per subset will be mirrored to EndpointSlices.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- control-plane
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- max addresses per subset
- subset size
---

This is intended to limit the number of changes that need to be sent to every [Node](/entity/node.md), even if it may result with multiple EndpointSlices that are not full.
