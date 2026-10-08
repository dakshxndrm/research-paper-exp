---
type: Management
title: EndpointSlice controller managed-by label
description: Kubernetes defines the label endpointslice.kubernetes.io/managed-by to
  indicate the entity managing an EndpointSlice. The endpoint slice controller sets
  endpointslice-controller.k8s.io as the value on all EndpointSlices it manages.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- label
- controller
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- managed-by label
- endpointslice.kubernetes.io/managed-by
---

To ensure that multiple entities can manage EndpointSlices without interfering with each other, Kubernetes defines the label [endpointslice](/definition/service_api_and_stable_endpoints.md).kubernetes.io/managed-by, which indicates the entity managing an EndpointSlice. The [endpoint slice](/definition/endpointslice_api_resource.md) controller sets endpointslice-controller.k8s.io as the value for this label on all EndpointSlices it manages.
