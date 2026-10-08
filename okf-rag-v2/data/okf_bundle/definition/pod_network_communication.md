---
type: Definition
title: Pod Network Communication
description: Describes how pods communicate within a cluster, including namespace
  sharing and cross-node connectivity.
resource: source://services-networking.md
tags:
- networking
- pods
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- pod communication
- cluster network
- pod-to-pod networking
---

# Pod Network Communication

The _pod network_ (also called a cluster network) handles communication between pods. It ensures that (barring intentional network segmentation):

* All pods can communicate with all other pods, whether they are on the same node or on different nodes. Pods can communicate with each other directly, without the use of proxies or address translation (NAT).
  * On Windows, this rule does not apply to host-network pods.
* Agents on a node (such as system daemons, or [kubelet](/definition/kubelet.md)) can communicate with all pods on that node.
