---
type: Procedure
title: Configuring Services and Load Balancing Behavior
description: Steps to configure services and load balancing behavior on Windows.
resource: source://services-networking__windows-networking.md
tags:
- windows
- kubernetes
- services
- load balancing
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- service configuration
- load balancing
---

On Windows, you can use the following settings to configure [Services](/procedure/configuring_load_balancing_and_services.md) and load balancing behavior:

| Feature | Description | Minimum Supported Windows OS build | How to enable |
| ------- | ----------- | -------------------------- | ------------- |
| Session affinity | Ensures that connections from a particular client are passed to the same Pod each time. | Windows Server 2022 | Set `[service](/entity/kubernetes_service.md).spec.sessionAffinity` to "ClientIP" |
| Direct Server Return (DSR) | See DSR notes above. | Windows Server 2019 | Set the following command line argument (assuming version ): ` --enable-dsr=true` |
| Preserve-Destination | Skips DNAT of service traffic, thereby preserving the virtual IP of the target service in packets reaching the backend Pod. Also disables [node](/entity/node.md)-[node](/entity/worker_node.md) forwarding. | Windows Server, version 1903 | Set ""preserve-destination": "true"" in service annotations and enable DSR in [kube-proxy](/component/kube_proxy.md). |
| [IPv4/IPv6 dual-stack](/classification/kubernetes_cluster_networking_types.md) networking | Native IPv4-to-IPv4 in parallel with IPv6-to-IPv6 communications to, from, and within a cluster | Windows Server 2019 | See [IPv4/IPv6](/policy/dual_stack_networking_policy.md) dual-stack |
| Client IP preservation | Ensures that source IP of incoming [ingress](/api/gateway_api.md) traffic gets preserved. Also disables node-node forwarding. |  Windows Server 2019  | Set `service.spec.externalTrafficPolicy` to "Local" and enable DSR in kube-[proxy](/entity/kube_proxy.md) |
