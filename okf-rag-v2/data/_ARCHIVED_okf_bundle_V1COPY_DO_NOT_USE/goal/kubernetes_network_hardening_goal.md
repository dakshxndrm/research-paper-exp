---
type: Goal
title: Kubernetes Network Hardening Goal
description: Describes the objective of customizing Kubernetes installations to secure
  network communication for untrusted or public networks.
resource: source://architecture__control-plane-node-communication.md
tags:
- network
- security
- installation
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- harden the network configuration
- run on an untrusted network
- run on fully public IPs
---

The intent of cataloging communication paths is to allow users to customize their [Kubernetes](/policy/garbage_collection_in_kubernetes.md) [installation](/installation/installing_gateway_api_crds.md) to harden the network configuration. This enables the cluster to be run on an untrusted network or on fully public IPs on a cloud provider.
