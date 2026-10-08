---
type: Definition
title: Kubernetes Networking Model Overview
description: 'Kubernetes addresses four distinct networking problems: container-to-container
  communications via Pod localhost, Pod-to-Pod communications as the primary focus,
  Pod-to-Service communications, and external-to-Service communications.'
resource: source://cluster-administration__networking.md
tags:
- networking
- model
timestamp: '2026-09-02T17:04:11+00:00'
---

# Kubernetes [Networking](/definition/application_exposure_service_and_ingress.md) Model Overview

Networking is a central part of Kubernetes, but it can be challenging to understand exactly how it is expected to work. There are 4 distinct networking problems to address:

1. Highly-coupled container-to-container communications: this is solved by Pods and `localhost` communications.
2. Pod-to-Pod communications: this is the primary focus of this document.
3. Pod-to-[Service](/component/service_load_balancing.md) communications: this is covered by Services.
4. External-to-Service communications: this is also covered by Services.

Kubernetes is all about sharing machines among applications. Typically, sharing machines requires ensuring that two applications do not try to use the same ports. Coordinating ports across multiple developers is very difficult to do at scale and exposes users to cluster-level issues outside of their control.

Dynamic port allocation brings a lot of complications to the system - every application has to take ports as flags, the API servers have to know how to insert dynamic port numbers into configuration blocks, services have to know how to find each other, etc. Rather than deal with this, Kubernetes takes a different approach.

To learn about the Kubernetes networking model, see here.
