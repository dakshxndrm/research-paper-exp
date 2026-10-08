---
type: Definition
title: Windows Container Networking Architecture
description: Explains how Windows containers use CNI plugins, Hyper-V virtual switches,
  and the Host Networking Service for network configuration and management.
resource: source://services-networking__windows-networking.md
tags:
- windows
- container networking
- architecture
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- windows container networking
- HNS networking
- Windows container network mode
---

[Networking](/definition/application_exposure_service_and_ingress.md) for Windows containers is exposed through [CNI plugins](/definition/external_components_implementing_kubernetes_networking.md). Windows containers function similarly to virtual machines in regards to networking. Each container has a virtual network adapter (vNIC) which is connected to a Hyper-V virtual switch (vSwitch). The Host Networking [Service](/component/service_load_balancing.md) (HNS) and the Host Compute Service (HCS) work together to [create](/operations/kubectl_resource_management_operations.md) containers and attach container vNICs to networks. HCS is responsible for the management of containers whereas HNS is responsible for the management of networking resources such as virtual networks, endpoints/vNICs, namespaces, and policies including packet encapsulations, load-balancing rules, ACLs, and NAT rules. The Windows HNS and vSwitch implement namespacing and can create virtual NICs as needed for a pod or container. However, many configurations such as DNS, routes, and metrics are stored in the Windows registry database rather than as files inside /etc, which is how Linux stores those configurations. The Windows registry for the container is separate from that of the host, so concepts like mapping /etc/resolv.conf from the host into a container don't have the same effect they would on Linux. These must be configured using Windows APIs run in the context of that container. Therefore CNI implementations need to call the HNS instead of relying on file mappings to pass network details into the pod or container.
