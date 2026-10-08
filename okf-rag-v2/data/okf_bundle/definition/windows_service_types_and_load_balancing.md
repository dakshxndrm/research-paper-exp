---
type: Definition
title: Windows Service Types and Load Balancing
description: Lists the supported Service types on Windows nodes and describes configuration
  options for Services and load balancing behavior.
resource: source://services-networking__windows-networking.md
tags:
- windows
- service
- load balancing
- clusterip
- nodeport
- loadbalancer
- externalname
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Windows Service
- Kubernetes Service Windows
- service types Windows
- load balancing Windows
---

On Windows, you can use the following types of Service: NodePort, ClusterIP, [LoadBalancer](/definition/external_access_mechanisms.md), ExternalName. [Windows container networking](/definition/windows_container_networking_architecture.md) differs in some important ways from Linux [networking](/definition/application_exposure_service_and_ingress.md). The Microsoft documentation for Windows Container Networking provides additional details and background. On Windows, you can use the following settings to configure Services and [load balancing](/component/service_load_balancing.md) behavior: [table with columns: Feature, Description, Minimum Supported Windows OS build, How to enable]. Features include session affinity, [Direct Server Return](/definition/windows_direct_server_return_dsr.md) (DSR), Preserve-Destination, [IPv4/IPv6 dual-stack networking](/definition/ipv4ipv6_dual_stack_networking.md), and Client IP preservation.
