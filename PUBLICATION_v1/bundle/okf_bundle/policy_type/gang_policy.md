---
type: Policy Type
title: Gang Policy
description: The `gang` policy enforces 'all-or-nothing' scheduling.
resource: source://workloads__workload-api__policies.md
tags:
- kubernetes
- workloads
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- all or nothing policy
- gang scheduling
---

The `gang` policy enforces 'all-or-nothing' [scheduling](/concept/scheduling.md). This is essential for tightly-coupled workloads where partial startup results in deadlocks or wasted resources.
