---
type: Verification
title: Verifying Pod Overhead in Resource Quotas
description: ResourceQuota counts both container requests and the overhead field;
  scheduler verified overhead against observed node requests.
resource: source://scheduling-eviction__pod-overhead.md
tags:
- kubernetes
- resourcequota
- verification
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- ResourceQuota overhead
- 2250m CPU and 320MiB observed
- requests include overhead
---

If a ResourceQuota is defined, the sum of container requests as well as the [overhead field](/definition/pod_overhead_in_kubernetes.md) are counted. Looking at our example, verify the container requests for the workload: The total container requests are 2000m CPU and 200MiB of memory: Check this against what is observed by the node: The output shows requests for 2250m CPU, and for 320MiB of memory. The requests include [Pod overhead](/definition/pod_overhead.md).
