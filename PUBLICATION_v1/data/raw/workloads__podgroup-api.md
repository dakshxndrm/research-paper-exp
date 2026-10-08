# PodGroup API

A PodGroup is a runtime object that represents a group of Pods scheduled together as a single unit.
While the Workload API defines scheduling policy
templates, PodGroups are the runtime counterparts that carry both the policy and the scheduling status
for a specific instance of that group.

## What is a PodGroup?

The PodGroup API resource is part of the `scheduling.k8s.io/v1alpha2`
API group
and your cluster must have that API group enabled, as well as the `GenericWorkload`
feature gate,
before you can use this API.

A PodGroup is a self-contained scheduling unit. It defines the group of Pods that should be scheduled together, carries the
scheduling policy that governs placement, and records the runtime status of that
scheduling decision.

## API structure

A PodGroup consists of a `spec` that defines the desired scheduling behavior and
a `status` that reflects the current scheduling state.

### Scheduling policy

Each PodGroup carries a scheduling policy
(`basic` or `gang`) in `spec.schedulingPolicy`. When a workload controller creates
the PodGroup, this policy is copied from the Workload's PodGroupTemplate at creation time.
For standalone PodGroups, you set the policy directly.

### Template reference

The optional `spec.podGroupTemplateRef` links the PodGroup back to the PodGroupTemplate
in the Workload it was created from. This is useful for observability and tooling.

### Requesting DRA devices for a PodGroup

Devices available through
Dynamic Resource Allocation (DRA)
can be requested by a PodGroup through its `spec.resourceClaims` field:

ResourceClaims
associated with PodGroups can be shared by all Pods belonging to the group. With
only a reference to the PodGroup in the ResourceClaim's `status.reservedFor`
instead of each individual Pod, any number of Pods in the same PodGroup can
share a ResourceClaim. ResourceClaims can also be generated from
ResourceClaimTemplates
for each PodGroup, allowing the devices allocated to each generated
ResourceClaim to be shared by the Pods in each PodGroup.

For more details and a more complete example, see the
DRA documentation.

### Status

The scheduler updates `status.conditions` to report whether the group has been
successfully scheduled. The primary condition is `PodGroupScheduled`, which is `True`
when all required Pods have been placed and `False` when scheduling fails.

The `PodGroupScheduled` condition reflects the initial scheduling decision only.
The scheduler does not update it if Pods later fail or are evicted. See
Limitations
for details.

See the PodGroup lifecycle
page for the full list of conditions and reasons.

## Creating a PodGroup

A PodGroup API resource is part of the `scheduling.k8s.io/v1alpha2`
API group.
(and your cluster must have that API group enabled, as well as the `GenericWorkload`
feature gate,
before you can use this API).

The following manifest creates a PodGroup with a gang scheduling policy that requires
at least 4 Pods to be schedulable simultaneously:

You can inspect PodGroups in your cluster:

To see the full status including scheduling conditions:

## How it fits together

The relationship between controllers, Workloads, PodGroups, and Pods follows this pattern:

1. The workload controller creates a Workload that defines PodGroupTemplates with scheduling policies.
2. For each runtime instance, the controller creates a PodGroup from one of the Workload's PodGroupTemplates.
3. The controller creates Pods that reference the PodGroup
   via the `spec.schedulingGroup.podGroupName` field.

The Job controller is the only built-in
workload controller that follows this pattern for now.
Custom controllers can implement the same flow for their own workload types.

The Workload acts as a long-lived policy definition, while PodGroups handle the 
transient, per-instance runtime state. This separation means that status updates for
individual PodGroups do not contend on the shared Workload object.

## 

* Learn about the PodGroup lifecycle in detail.
* Read about the Workload API that provides PodGroupTemplates.
* See how Pods reference their PodGroup via the scheduling group field.
* Understand the gang scheduling algorithm.
