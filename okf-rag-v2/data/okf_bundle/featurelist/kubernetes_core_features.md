---
type: FeatureList
title: Kubernetes Core Features
description: Kubernetes provides a framework for container orchestration including
  service discovery, storage, automated deployments, and self-healing capabilities.
resource: source://overview.md
tags:
- features
- orchestration
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- Kubernetes capabilities
- container features
---

Kubernetes provides you with:
* **Service discovery and [load balancing](/component/service_load_balancing.md)**: Kubernetes can expose a container using a DNS name or its own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the [deployment](/definition/workload_resources.md) is stable.
* **Storage orchestration**: Kubernetes allows you to automatically mount a storage system of your choice, such as local storage, public cloud providers, and more.
* **Automated rollouts and rollbacks**: You can describe the [desired state](/concept/desired_versus_current_state.md) for your deployed containers using Kubernetes, and it can change the actual state to the desired state at a controlled rate.
* **Automated bin packing**: You provide Kubernetes with a cluster of nodes that it can use to run containerized tasks. You tell Kubernetes how much CPU and memory (RAM) each container needs. Kubernetes can fit containers onto your nodes to make the best use of your resources.
* **Self-healing**: Kubernetes restarts containers that fail, replaces containers, kills containers that don't respond to your user-defined health check, and doesn't advertise them to clients until they are ready to serve.
* **Secret and [configuration management](/operations/kubectl_cluster_maintenance_operations.md)**: Kubernetes lets you store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys. You can deploy and [update](/operations/kubectl_resource_management_operations.md) secrets and application configuration without rebuilding your container images, and without exposing secrets in your stack configuration.
* **Batch execution**: In addition to services, Kubernetes can manage your batch and CI workloads, replacing containers that fail, if desired.
* **Horizontal scaling**: Scale your application up and down with a simple command, with a UI, or automatically based on CPU usage.
* **[IPv4/IPv6 dual-stack](/definition/ipv4ipv6_dual_stack_networking.md)**: Allocation of IPv4 and IPv6 addresses to Pods and Services.
* **Designed for extensibility**: Add features to your Kubernetes cluster without changing upstream source code.
