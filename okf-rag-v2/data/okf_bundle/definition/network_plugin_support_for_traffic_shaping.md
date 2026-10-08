---
type: Definition
title: Network Plugin Support for Traffic Shaping
description: The CNI networking plugin provides experimental support for pod ingress
  and egress traffic shaping via the bandwidth plugin and corresponding annotations.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- networking
- traffic shaping
- bandwidth
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- traffic shaping
- bandwidth plugin
- kubernetes.io/ingress-bandwidth
- kubernetes.io/egress-bandwidth
---

The CNI [networking](/definition/application_exposure_service_and_ingress.md) plugin also supports pod [ingress](/definition/gateway_api_and_cluster_ingress.md) and egress traffic shaping. This is an experimental feature. You can use the official [bandwidth plugin](/definition/traffic_shaping_capability.md) offered by the CNI plugin team or use your own plugin with bandwidth control functionality. If you want to enable traffic shaping support, you must add the bandwidth plugin to your CNI configuration file (default `/etc/cni/net.d`) and ensure that the binary is included in your CNI bin dir (default `/opt/cni/bin`). Now you can add the `kubernetes.io/ingress-bandwidth` and `kubernetes.io/egress-bandwidth` annotations to your Pod.
