---
type: Definition
title: External Components Implementing Kubernetes Networking
description: Lists the external components responsible for implementing networking
  functionality defined by Kubernetes APIs, including CNI plugins, service proxies,
  and Gateway API implementations.
resource: source://services-networking.md
tags:
- networking
- components
- infrastructure
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- external networking components
- CNI plugins
- service proxy
- Gateway API implementations
---

# External Components Implementing Kubernetes [Networking](/definition/application_exposure_service_and_ingress.md)

Only a few parts of this model are implemented by Kubernetes itself. For the other parts, Kubernetes defines the APIs, but the corresponding functionality is provided by external components, some of which are optional:

* [Pod network namespace](/definition/pod_ip_addressing_and_namespaces.md) setup is handled by system-level software implementing the [Container Runtime](/definition/container_runtime.md) Interface.
* The pod network itself is managed by a pod network implementation. On Linux, most container runtimes use the Container Networking Interface (CNI) to interact with the pod network implementation, so these implementations are often called CNI [plugins](/extensibility/kubectl_plugins.md).
* Kubernetes provides a default implementation of [service proxying](/definition/service_api_and_stable_endpoints.md), called kube-proxy, but some pod network implementations instead use their own [service proxy](/definition/kube_proxy_optional.md) that is more tightly integrated with the rest of the implementation.
* [NetworkPolicy](/definition/network_policies.md) is generally also implemented by the pod network implementation. (Some simpler pod network implementations don't implement NetworkPolicy, or an administrator may choose to configure the pod network without NetworkPolicy support. In these cases, the API will still be present, but it will have no effect.)
* There are many implementations of the [Gateway API](/entity/gateway_api.md), some of which are specific to particular cloud environments, some more focused on "bare metal" environments, and others more generic.
