---
type: Constraint
title: DNS Subdomain Name Requirements
description: Resource names must be valid DNS subdomain names per RFC 1123, with a
  maximum of 253 characters, allowing only lowercase alphanumeric characters, '-',
  or '.', and starting and ending with an alphanumeric character.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- naming-conventions
- dns
- rfc 1123
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- DNS subdomain naming
- RFC 1123 name constraints
- resource name format
---

Most resource types require a name that can be used as a DNS subdomain name as defined in RFC 1123. This means the name must:
- contain no more than 253 characters
- contain only lowercase alphanumeric characters, '-' or '.'
- start with an alphanumeric character
- end with an alphanumeric character
