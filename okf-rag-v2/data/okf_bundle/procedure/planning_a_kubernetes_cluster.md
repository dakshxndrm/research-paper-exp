---
type: Procedure
title: Planning a Kubernetes Cluster
description: Outlines considerations for planning a Kubernetes cluster including hosted
  vs self-hosted, on-premises vs cloud, networking models, hardware choices, and development
  vs production use cases.
resource: source://cluster-administration.md
tags:
- kubernetes
- cluster planning
- distro
- deployment
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- cluster planning
- Kubernetes cluster planning
- distro selection
- cluster deployment planning
---

# Planning a Kubernetes Cluster

See the guides in Setup for examples of how to plan, set up, and configure Kubernetes clusters. The solutions listed in this article are called *distros*.

Not all distros are actively maintained. Choose distros which have been tested with a recent version of Kubernetes.

Before choosing a guide, here are some considerations:

- Do you want to try out Kubernetes on your computer, or do you want to build a high-availability, multi-node cluster? Choose distros best suited for your needs.
- Will you be using **a hosted Kubernetes cluster**, such as Google Kubernetes Engine, or **hosting your own cluster**?
- Will your cluster be **on-premises**, or **in the cloud (IaaS)**? Kubernetes does not directly support hybrid clusters. Instead, you can set up [multiple clusters](/cluster_management/kubectl_context_switching.md).
- **If you are configuring Kubernetes on-premises**, consider which [networking](/definition/application_exposure_service_and_ingress.md) model fits best.
- Will you be running Kubernetes on **"bare metal" hardware** or on **virtual machines (VMs)**?
- Do you **want to run a cluster**, or do you expect to do **active development of [Kubernetes project](/definition/kubernetes_overview.md) code**? If the latter, choose an actively-developed distro. Some distros only use binary releases, but offer a greater variety of choices.
- Familiarize yourself with the components needed to run a cluster.
