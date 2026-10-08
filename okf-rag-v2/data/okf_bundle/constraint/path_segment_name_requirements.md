---
type: Constraint
title: Path Segment Name Requirements
description: Resource names must be safely encodable as path segments, excluding the
  reserved strings '.' and '..' and preventing inclusion of '/' or '%' characters.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- naming-conventions
- path-segments
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- path segment naming
- path-safe naming
- resource name encoding
---

Some resource types require their names to be able to be safely encoded as a path segment. In other words, the name may not be "." or ".." and the name may not contain "/" or "%".
