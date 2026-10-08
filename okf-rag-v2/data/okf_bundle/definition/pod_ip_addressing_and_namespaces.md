---
type: Definition
title: Pod IP Addressing and Namespaces
description: Defines how each pod receives a unique IP address and shares a network
  namespace with its containers.
resource: source://services-networking.md
tags:
- networking
- pods
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- pod IP
- container namespace
- pod network namespace
---

# Pod IP Addressing and Namespaces

* Each pod in a cluster gets its own unique cluster-wide IP address.
  * A pod has its own private network namespace which is shared by all of the containers within the pod. Processes running in different containers in the same pod can communicate with each other over `localhost`.
