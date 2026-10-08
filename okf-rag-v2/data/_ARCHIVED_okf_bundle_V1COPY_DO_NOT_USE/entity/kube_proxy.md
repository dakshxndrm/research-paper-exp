---
type: Entity
title: kube-proxy
description: kube-proxy watches EndpointSlices and routes traffic based on them.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- control-plane
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- kube proxy
- proxy
---

Every change to an EndpointSlice becomes relatively expensive since it will be transmitted to every [Node](/entity/node.md) in the cluster.
