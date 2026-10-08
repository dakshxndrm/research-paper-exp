---
type: Component
title: Pod Network Namespace
description: Private network namespace for each pod.
resource: source://services-networking.md
tags:
- kubernetes
- networking
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- pod network
- cluster network
---

A pod has its own private network [namespace](/definition/api_group_resource_type_namespace_and_name.md) which is shared by all of the containers within the pod. Processes running in different containers in the same pod can communicate with each other over `localhost`.
