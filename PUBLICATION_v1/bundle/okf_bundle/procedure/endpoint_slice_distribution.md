---
type: Procedure
title: Endpoint Slice Distribution
description: The control plane tries to fill EndpointSlices as full as possible.
resource: source://services-networking__endpoint-slices.md
tags:
- kubernetes
- control-plane
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- endpoint slice filling
---

The logic is fairly straightforward: 1. Iterate through existing EndpointSlices, remove endpoints that are no longer desired and update matching endpoints that have changed. 2. Iterate through EndpointSlices that have been modified in the first step and fill them up with any new endpoints needed.
