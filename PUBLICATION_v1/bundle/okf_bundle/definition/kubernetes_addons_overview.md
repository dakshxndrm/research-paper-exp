---
type: Definition
title: Kubernetes Addons Overview
description: Defines Kubernetes addons as cluster features implemented using Kubernetes
  resources, residing in the `kube-system` namespace, and lists common examples.
resource: source://architecture.md
tags:
- kubernetes
- addon
- feature
- kube-system
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- Addons
- cluster features
- kube-system namespace
- Cluster DNS
- Web UI
- Dashboard
- Container resource monitoring
- Cluster-level Logging
---

Addons use [Kubernetes](/policy/garbage_collection_in_kubernetes.md) resources ([daemonset](/entity/daemonset.md), [deployment](/entity/deployment.md), etc.) to implement cluster features. Because these are providing cluster-level features, namespaced resources for addons belong within the `kube-system` [namespace](/definition/api_group_resource_type_namespace_and_name.md). Selected addons include:
- DNS: A DNS server, in addition to other DNS servers in your environment, which serves DNS records for Kubernetes [services](/procedure/configuring_load_balancing_and_services.md). Containers started by Kubernetes automatically include this DNS server in their DNS searches.
- Web UI (Dashboard): A general purpose, web-based UI for Kubernetes clusters that allows users to manage and troubleshoot applications and the cluster itself.
- Container [resource](/resource/cluster_resources.md) monitoring: Records generic time-series metrics about containers in a central database, and provides a UI for browsing that data.
- Cluster-level Logging: A mechanism responsible for saving container logs to a central log store with a search/browsing interface.
