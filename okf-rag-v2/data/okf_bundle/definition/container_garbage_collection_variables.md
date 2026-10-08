---
type: Definition
title: Container Garbage Collection Variables
description: The kubelet garbage collects unused containers based on MinAge, MaxPerPodContainer,
  and MaxContainers settings, with conflict resolution between per-pod and global
  container limits.
resource: source://architecture__garbage-collection.md
tags:
- container-gc-variables
- definition
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- container gc variables
- dead container retention
---

# [Container garbage collection](/procedure/container_and_image_garbage_collection.md)

The [kubelet](/definition/kubelet.md) garbage collects unused containers based on the following variables, which you can define:

* MinAge: the minimum age at which the kubelet can garbage collect a container. Disable by setting to 0.
* MaxPerPodContainer: the maximum number of dead containers each Pod can have. Disable by setting to less than 0.
* MaxContainers: the maximum number of dead containers the cluster can have. Disable by setting to less than 0.

In addition to these variables, the kubelet garbage collects unidentified and deleted containers, typically starting with the oldest first.

MaxPerPodContainer and MaxContainers may potentially conflict with each other in situations where retaining the maximum number of containers per Pod (MaxPerPodContainer) would go outside the allowable total of global dead containers (MaxContainers). In this situation, the kubelet adjusts MaxPerPodContainer to address the conflict. A worst-case scenario would be to downgrade MaxPerPodContainer to 1 and evict the oldest containers. Additionally, containers owned by pods that have been deleted are removed once they are older than MinAge.

The kubelet only garbage collects the containers it manages.
