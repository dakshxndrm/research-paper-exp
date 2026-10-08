---
type: Procedure
title: Specify Node Selectors for a Pod
description: Assign node selectors to a Pod.
resource: source://workloads__pods__advanced-pod-config.md
tags:
- kubernetes
- pods
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- assign node selector
- pod node assignment
---

To specify [node selectors](/policy/node_selectors.md) for a Pod, add the `nodeSelector` field to the Pod specification and set it with the desired [node](/entity/node.md) [selectors](/definition/owner_references_vs_labels_and_selectors.md).
