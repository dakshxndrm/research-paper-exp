---
type: Headless Services
title: Headless Services without selector
description: Behavior of headless Services without selectors in dual-stack configurations.
resource: source://services-networking__dual-stack.md
tags:
- networking
- services
- ip family policy
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- headless Services
- headless Service without selector
- headless Service IP family
---

For Headless Services without selectors and without .spec.[ipFamilyPolicy](/service_configuration/service_address_family_policy.md) explicitly set, the .spec.ipFamilyPolicy field defaults to RequireDualStack. Existing headless Services with selectors are configured by the [control plane](/definition/control_plane_components.md) to set .spec.ipFamilyPolicy to SingleStack and .spec.ipFamilies to the address family of the first [service](/component/service_load_balancing.md) cluster IP range, even though .spec.clusterIP is set to None.
