---
type: Definition
title: NetworkPolicy for Traffic Control
description: Defines the NetworkPolicy API for controlling traffic between pods and
  to the outside world at the IP address or port level.
resource: source://services-networking.md
tags:
- networking
- security
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- NetworkPolicy
- traffic control
- IP address policy
- port level policy
---

# [NetworkPolicy](/definition/network_policies.md) for Traffic Control

NetworkPolicy is a built-in Kubernetes API that allows you to control traffic between pods, or between pods and the outside world.

* NetworkPolicy is generally also implemented by the pod network implementation. (Some simpler pod network implementations don't implement NetworkPolicy, or an administrator may choose to configure the pod network without NetworkPolicy support. In these cases, the API will still be present, but it will have no effect.)
