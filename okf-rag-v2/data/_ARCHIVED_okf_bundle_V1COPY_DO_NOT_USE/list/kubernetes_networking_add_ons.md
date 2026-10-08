---
type: List
title: Kubernetes Networking Add-ons
description: This concept lists various add-ons that provide networking and network
  policy services for Kubernetes clusters.
resource: source://cluster-administration__addons.md
tags:
- networking
- network policy
- cni
- kubernetes
- overlay network
- service mesh
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- networking add-ons
- network policy add-ons
- CNI plugins
---

The following [add-ons](/definition/kubernetes_add_ons_overview.md) provide networking and [network policy](/api/networkpolicy.md) capabilities for [Kubernetes](/policy/garbage_collection_in_kubernetes.md):

*   **ACI**: Provides integrated container networking and network security with Cisco ACI.
*   **Antrea**: Operates at Layer 3/4 to provide networking and security [services](/procedure/configuring_load_balancing_and_services.md) for Kubernetes, leveraging Open vSwitch as the networking data plane. Antrea is a CNCF project at the [Sandbox](/definition/loopback_interface.md) level.
*   **Calico**: Is a networking and network policy provider supporting flexible networking options, including non-overlay and overlay networks, with or without BGP. Calico uses the same engine to enforce network policy for hosts, [pods](/definition/kubernetes_cluster_architecture.md), and (if using Istio & Envoy) applications at the [service](/entity/kubernetes_service.md) mesh layer.
*   **Canal**: Unites [Flannel](/entity/flannel_cni_plugin.md) and Calico, providing networking and network policy.
*   **Cilium**: Is a networking, [observability](/procedure/observability_and_runtime_security.md), and security solution with an eBPF-based data plane. Cilium provides a simple flat Layer 3 network with the ability to span multiple clusters in either a native routing or overlay/encapsulation [mode](/definition/disruption_mode.md), and can enforce [network policies](/procedure/implementing_network_policies.md) on L3-L7 using an identity-based security model decoupled from network addressing. Cilium can act as a replacement for [kube-proxy](/component/kube_proxy.md) and offers additional, opt-in observability and security features. Cilium is a CNCF project at the Graduated level.
*   **CNI-Genie**: Enables Kubernetes to seamlessly connect to a choice of CNI plugins, such as Calico, Canal, Flannel, or Weave. CNI-Genie is a CNCF project at the Sandbox level.
*   **Contiv**: Provides configurable networking (native L3 using BGP, overlay using vxlan, classic L2, and Cisco-SDN/ACI) for various use cases and a rich policy framework. The Contiv project is fully open sourced, and its installer provides both kubeadm and non-kubeadm based [installation](/installation/installing_gateway_api_crds.md) options.
*   **Contrail**: Based on Tungsten Fabric, is an open source, multi-cloud network virtualization and policy management platform. Contrail and Tungsten Fabric are integrated with orchestration systems such as Kubernetes, OpenShift, OpenStack and Mesos, and provide isolation modes for virtual machines, containers/pods and bare metal workloads.
*   **Flannel**: Is an overlay network provider that can be used with Kubernetes.
*   **[Gateway API](/api/gateway_api.md)**: Is an open source project managed by the SIG Network community and provides an expressive, extensible, and role-oriented API for modeling service networking.
*   **Knitter**: Is a [plugin](/plugin/gangscheduling_plugin.md) to support multiple network interfaces in a [Kubernetes pod](/entity/pods_in_kubernetes.md).
*   **kube-router**: Is an open source turnkey solution for Kubernetes networking aiming for operational simplicity and high performance. It leverages the [Kubernetes API](/entity/kubernetes_api.md), BGP, and Golang for the control path and Linux networking primitives (IPVS, nftables, etc.) for the data path. It provides a low overhead alternative and is used in both k0s and k3s.
*   **Multus**: Is a Multi plugin for multiple network support in Kubernetes to support all CNI plugins (e.g. Calico, Cilium, Contiv, Flannel), in addition to SRIOV, DPDK, OVS-DPDK and VPP based workloads in Kubernetes.
*   **OVN-Kubernetes**: Is a networking provider for Kubernetes based on OVN (Open Virtual Network), a virtual networking implementation that came out of the Open vSwitch (OVS) project. OVN-Kubernetes provides an overlay based networking implementation for Kubernetes, including an OVS based implementation of [load balancing](/procedure/configuring_services_and_load_balancing_behavior.md) and network policy.
*   **Nodus**: Is an OVN based CNI [controller](/pattern/kubernetes_controller_pattern.md) plugin to provide cloud native based Service function chaining (SFC).
*   **NSX-T Container Plug-in (NCP)**: Provides integration between VMware NSX-T and container orchestrators such as Kubernetes, as well as integration between NSX-T and container-based CaaS/PaaS platforms such as Pivotal Container Service (PKS) and OpenShift.
*   **Nuage**: Is an SDN platform that provides policy-based networking between Kubernetes Pods and non-Kubernetes environments with visibility and security monitoring.
*   **Romana**: Is a Layer 3 networking solution for pod networks that also supports the NetworkPolicy API.
*   **Spiderpool**: Is an underlay and RDMA networking solution for Kubernetes. Spiderpool is supported on bare metal, virtual machines, and public cloud environments.
*   **Terway**: Is a suite of CNI plugins based on AlibabaCloud's VPC and ECS network products. It provides native VPC networking and network policies in AlibabaCloud environments.
*   **Weave Net**: Provides networking and network policy, will carry on working on both sides of a network partition, and does not require an external database.
