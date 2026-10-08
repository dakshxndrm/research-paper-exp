---
type: Configuration
title: Default endpoint slice size limit
description: By default, the control plane creates and manages EndpointSlices with
  no more than 100 endpoints each, configurable via the --max-endpoints-per-slice
  kube-controller-manager flag up to a maximum of 1000.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- configuration
- controller
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- max-endpoints-per-slice
- endpoint slice size limit
---

By default, the [control plane](/definition/control_plane_components.md) creates and manages EndpointSlices to have no more than 100 endpoints each. You can configure this with the `--max-endpoints-per-slice` [kube-controller-manager](/definition/kube_controller_manager.md) flag, up to a maximum of 1000.
