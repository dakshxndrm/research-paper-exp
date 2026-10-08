---
type: Constraint
title: RFC 1123 Label Name Requirements
description: Resource names must follow DNS label standards per RFC 1123, with a maximum
  of 63 characters, allowing only lowercase alphanumeric characters or '-', starting
  with an alphabetic character and ending with an alphanumeric character, with exceptions
  when RelaxedServiceNameValidation is enabled.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- naming-conventions
- dns
- rfc 1123
- relaxedservicenamevalidation
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- RFC 1123 label naming
- DNS label constraints
- resource name format
---

Some resource types require their names to follow the DNS label standard as defined in RFC 1123. This means the name must:
- contain at most 63 characters
- contain only lowercase alphanumeric characters or '-'
- start with an alphabetic character
- end with an alphanumeric character

When the `RelaxedServiceNameValidation` feature gate is enabled, [Service](/component/service_load_balancing.md) object names are allowed to start with a digit.
