---
type: Design Principle
title: Controller Specialization
description: Kubernetes design principle of using many simple controllers rather than
  one monolithic control loop, with each controller managing a particular aspect of
  cluster state and using labels to distinguish resources.
resource: source://architecture__controller.md
tags:
- kubernetes
- design
- control plane
timestamp: '2026-09-02T17:04:11+00:00'
aliases:
- controller design
- separate controllers
- resource management
---

As a tenet of its design, Kubernetes uses lots of controllers that each manage a particular aspect of [cluster state](/concept/desired_versus_current_state.md). Most commonly, a particular [control loop](/definition/control_loop.md) (controller) uses one kind of resource as its desired state, and has a different kind of resource that it manages to make that desired state happen. For example, a controller for Jobs tracks Job objects (to discover new work) and Pod objects (to run the Jobs, and then to see when the work is finished). In this case something else creates the Jobs, whereas the [Job controller](/procedure/job_controller_workflow.md) creates Pods. It's useful to have simple controllers rather than one, monolithic set of control loops that are interlinked. Controllers can fail, so Kubernetes is designed to allow for that. There can be several controllers that [create](/operations/kubectl_resource_management_operations.md) or update the same kind of object. Behind the scenes, Kubernetes controllers make sure that they only pay attention to the resources linked to their controlling resource.
