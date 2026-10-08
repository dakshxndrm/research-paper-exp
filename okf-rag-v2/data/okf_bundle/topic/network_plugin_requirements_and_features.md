---
type: Topic
title: Network Plugin Requirements and Features
description: Kubernetes network model requirements including loopback interface, hostPort
  support, and traffic shaping capabilities.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- networking
- requirements
- features
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- network requirements
- CNI features
- plugin capabilities
---

Kubernetes [network model requirements](/definition/cni_plugin_compatibility_requirements.md) include the [loopback interface](/definition/container_runtime_cni_responsibilities.md) `lo` for sandboxes, support for [hostPort](/definition/network_plugin_support_for_hostport.md) via [portMappings capability](/definition/hostport_support_via_port_mapping.md), and experimental support for pod [ingress](/definition/gateway_api_and_cluster_ingress.md) and egress traffic shaping via the [bandwidth plugin](/definition/traffic_shaping_capability.md). Additional resources are available for Cluster [Networking](/definition/application_exposure_service_and_ingress.md), [Network Policies](/definition/network_policies.md), and Troubleshooting CNI plugin-related errors.
