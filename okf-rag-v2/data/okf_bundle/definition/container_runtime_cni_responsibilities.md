---
type: Definition
title: Container Runtime CNI Responsibilities
description: The Container Runtime must be configured to load CNI plugins required
  to implement the Kubernetes network model, including providing a loopback interface
  for pod sandboxes.
resource: source://extend-kubernetes__compute-storage-net__network-plugins.md
tags:
- container runtime
- cni
- node configuration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Container Runtime configuration
- CNI plugin management
- loopback interface
---

A [Container Runtime](/definition/container_runtime.md), in the [networking](/definition/application_exposure_service_and_ingress.md) context, is a daemon on a node configured to provide CRI Services for [kubelet](/definition/kubelet.md). In particular, the [Container Runtime](/definition/runtimeclasses.md) must be configured to load the [CNI plugins](/definition/external_components_implementing_kubernetes_networking.md) required to implement the Kubernetes [network model](/definition/kubernetes_network_model_overview.md). Prior to Kubernetes 1.24, the CNI [plugins](/extensibility/kubectl_plugins.md) could also be managed by the kubelet using the `cni-bin-dir` and `network-plugin` command-line parameters. These command-line parameters were removed in Kubernetes 1.24, with management of the CNI no longer in scope for kubelet. In addition to the CNI plugin installed on the nodes for implementing the Kubernetes network model, Kubernetes also requires the container runtimes to provide a loopback interface `lo`, which is used for each sandbox (pod sandboxes, vm sandboxes, ...). Implementing the loopback interface can be accomplished by re-using the [CNI loopback plugin](/definition/loopback_interface_requirement.md) or by developing your own code to achieve this.
