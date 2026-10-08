---
type: Definition
title: Kubernetes Cluster Networking Types
description: 'Kubernetes clusters are categorized by IP families: IPv4 only, IPv6
  only, or dual-stack (IPv4/IPv6) where all components must agree on the primary IP
  family.'
resource: source://cluster-administration__networking.md
tags:
- ip families
- cluster types
timestamp: '2026-09-02T17:04:11+00:00'
---

# Kubernetes Cluster [Networking](/definition/application_exposure_service_and_ingress.md) Types

Kubernetes clusters, attending to the IP families configured, can be categorized into:

- IPv4 only: The network plugin, [kube-apiserver](/definition/kube_apiserver.md) and [kubelet](/definition/kubelet.md)/[cloud-controller-manager](/definition/cloud_controller_manager.md) are configured to assign only IPv4 addresses.
- IPv6 only: The network plugin, kube-apiserver and kubelet/cloud-controller-manager are configured to assign only IPv6 addresses.
- IPv4/IPv6 or IPv6/IPv4 dual-stack: The network plugin is configured to assign IPv4 and IPv6 addresses, the kube-apiserver is configured to assign IPv4 and IPv6 addresses, and the kubelet or cloud-controller-manager is configured to assign IPv4 and [IPv6 address](/address_types/endpointslice_address_types_ipv4_and_ipv6.md). All components must agree on the configured primary IP family.

Kubernetes clusters only consider the IP families present on the Pods, Services and Nodes objects, independently of the existing IPs of the represented objects.
