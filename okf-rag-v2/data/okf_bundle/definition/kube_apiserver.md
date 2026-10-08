---
type: Definition
title: kube-apiserver
description: The front-end for the Kubernetes control plane that exposes the Kubernetes
  API.
resource: source://architecture.md
tags:
- architecture
- kubernetes
- api
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Kubernetes API server
- API server
---

The kube-apiserver is the front-end for the Kubernetes [control plane](/definition/control_plane_components.md). It exposes the Kubernetes API. The API server can be horizontally scaled out by deploying multiple instances, and it serves as the front-end for the shared state of the cluster, through which all other components communicate.
