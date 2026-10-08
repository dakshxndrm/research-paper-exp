---
type: Topology
title: EndpointSlice topology information nodeName and zone
description: Each endpoint within an EndpointSlice can contain topology information
  including nodeName and zone fields that provide location details about the corresponding
  Node and zone.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- topology
- node
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- nodeName
- zone
- topology information
---

Each endpoint within an [EndpointSlice](/definition/service_api_and_stable_endpoints.md) can contain relevant topology information. The topology information includes the location of the endpoint and information about the corresponding Node and zone. These are available in the following per endpoint fields on EndpointSlices: nodeName - The name of the Node this endpoint is on. zone - The zone this endpoint is in.
