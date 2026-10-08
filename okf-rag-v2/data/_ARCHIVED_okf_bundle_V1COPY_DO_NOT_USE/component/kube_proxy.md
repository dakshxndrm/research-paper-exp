---
type: Component
title: kube-proxy
description: Describes the role of kube-proxy as a network proxy component on each
  node and when it might not be required.
resource: source://architecture.md
tags:
- kubernetes
- component
- node
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- network proxy component
---

The `kube-[proxy](/entity/kube_proxy.md)` component is a network proxy that runs on each [node](/entity/node.md) to ensure that the [Service API](/api/service_api.md) and associated behaviors are available on your [cluster network](/component/pod_network_namespace.md). However, some [network plugins](/component/kubernetes_network_plugins.md) provide their own, third-party implementation of proxying. When you use that kind of network [plugin](/plugin/gangscheduling_plugin.md), the [node](/entity/worker_node.md) does not need to run `kube-proxy`.
