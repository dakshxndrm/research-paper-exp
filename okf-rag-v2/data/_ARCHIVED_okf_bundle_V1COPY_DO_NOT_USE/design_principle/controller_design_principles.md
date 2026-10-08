---
type: Design Principle
title: Controller Design Principles
description: Kubernetes is designed with numerous simple, independent controllers,
  each managing a specific aspect of cluster state, to enhance resilience and allow
  for individual controller failures.
resource: source://architecture__controller.md
tags:
- kubernetes
- design
- architecture
- resilience
- modularity
timestamp: '2026-07-27T19:53:46+00:00'
aliases:
- design
- tenet of its design
- Kubernetes controller design
---

As a tenet of its design, [Kubernetes](/policy/garbage_collection_in_kubernetes.md) uses lots of [controllers](/pattern/kubernetes_controller_pattern.md) that each manage a particular aspect of cluster state. Most commonly, a particular [control loop](/definition/control_loop.md) (controller) uses one kind of [resource](/resource/cluster_resources.md) as its [desired state](/philosophy/kubernetes_state_management.md), and has a different kind of resource that it manages to make that desired state happen. For example, a controller for Jobs tracks [Job](/entity/job.md) objects (to discover new work) and Pod objects (to run the Jobs, and then to see when the work is finished). In this case something else creates the Jobs, whereas the [Job controller](/component/kube_controller_manager.md) creates [Pods](/definition/kubernetes_cluster_architecture.md). It's useful to have simple controllers rather than one, monolithic set of control loops that are interlinked. Controllers can fail, so Kubernetes is designed to allow for that. There can be several controllers that create or update the same kind of object. Behind the scenes, [Kubernetes controllers](/component/controller_roles_in_self_healing.md) make sure that they only pay attention to the resources linked to their controlling resource. For example, you can have Deployments and Jobs; these both create Pods. The Job controller does not [delete](/procedure/deleting_resources_in_kubernetes.md) the Pods that your [Deployment](/entity/deployment.md) created, because there is information ([labels](/concept/owner_references_and_labels.md)) the controllers can use to tell those Pods apart.
