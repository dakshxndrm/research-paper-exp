---
type: Constraint
title: RFC 1035 Label Name Requirements
description: Resource names must follow DNS label standards per RFC 1035, with a maximum
  of 63 characters, allowing only lowercase alphanumeric characters or '-', starting
  with an alphabetic character and ending with an alphanumeric character.
resource: source://overview__working-with-objects__names.md
tags:
- kubernetes
- naming-conventions
- dns
- rfc 1035
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- RFC 1035 label naming
- DNS label constraints
- resource name format
---

Some resource types require their names to follow the DNS label standard as defined in RFC 1035. This means the name must:
- contain at most 63 characters
- contain only lowercase alphanumeric characters or '-'
- start with an alphabetic character
- end with an alphanumeric character

While RFC 1123 technically allows labels to start with digits, the current Kubernetes implementation requires both RFC 1035 and RFC 1123 labels to start with an alphabetic character. The exception is when the `RelaxedServiceNameValidation` feature gate is enabled for [Service](/component/service_load_balancing.md) objects, which allows Service names to start with digits.
