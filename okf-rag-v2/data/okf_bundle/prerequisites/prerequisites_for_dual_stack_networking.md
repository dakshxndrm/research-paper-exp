---
type: Prerequisites
title: Prerequisites for dual-stack networking
description: Requirements that must be met before configuring IPv4/IPv6 dual-stack
  in a Kubernetes cluster.
resource: source://services-networking__dual-stack.md
tags:
- networking
- requirements
- cluster configuration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- dual-stack prerequisites
- cluster prerequisites
- network requirements
---

The following prerequisites are needed to utilize IPv4/IPv6 dual-stack Kubernetes clusters: Kubernetes 1.20 or later, provider support for [dual-stack networking](/definition/ipv4ipv6_dual_stack_networking.md) (cloud provider or otherwise must be able to provide Kubernetes nodes with routable IPv4/IPv6 network interfaces), and a network plugin that supports dual-stack [networking](/definition/application_exposure_service_and_ingress.md).
