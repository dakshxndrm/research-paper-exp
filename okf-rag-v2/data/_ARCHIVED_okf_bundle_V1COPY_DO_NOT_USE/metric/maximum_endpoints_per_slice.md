---
type: Metric
title: Maximum Endpoints per Slice
description: The control plane creates and manages EndpointSlices to have no more
  than 100 endpoints each.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- control-plane
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- max endpoints per slice
- endpoint slice size
---

You can configure this with the `--max-endpoints-per-slice` [kube-controller-manager](/component/kube_controller_manager.md) flag, up to a maximum of 1000.
