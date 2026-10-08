# Pod Overhead

When you run a Pod on a Node, the Pod itself takes an amount of system resources. These
resources are additional to the resources needed to run the container(s) inside the Pod.
In Kubernetes, _Pod Overhead_ is a way to account for the resources consumed by the Pod
infrastructure on top of the container requests & limits.

In Kubernetes, the Pod's overhead is set at
admission
time according to the overhead associated with the Pod's
RuntimeClass.

A pod's overhead is considered in addition to the sum of container resource requests when
scheduling a Pod. Similarly, the kubelet will include the Pod overhead when sizing the Pod cgroup,
and when carrying out Pod eviction ranking.

## Configuring Pod overhead {#set-up}

You need to make sure a `RuntimeClass` is utilized which defines the `overhead` field.

## Usage example

To work with Pod overhead, you need a RuntimeClass that defines the `overhead` field. As
an example, you could use the following RuntimeClass definition with a virtualization container
runtime (in this example, Kata Containers combined with the Firecracker virtual machine monitor)
that uses around 120MiB per Pod for the virtual machine and the guest OS:

Workloads which are created which specify the `kata-fc` RuntimeClass handler will take the memory and
cpu overheads into account for resource quota calculations, node scheduling, as well as Pod cgroup sizing.

Consider running the given example workload, test-pod:

If only `limits` are specified in the pod definition, kubelet will deduce `requests` from those limits and set them to be the same as the defined `limits`.

At admission time the RuntimeClass admission controller
updates the workload's PodSpec to include the `overhead` as described in the RuntimeClass. If the PodSpec already has this field defined,
the Pod will be rejected. In the given example, since only the RuntimeClass name is specified, the admission controller mutates the Pod
to include an `overhead`.

After the RuntimeClass admission controller has made modifications, you can check the updated
Pod overhead value:

The output is:

If a ResourceQuota is defined, the sum of container requests as well as the
`overhead` field are counted.

When the kube-scheduler is deciding which node should run a new Pod, the scheduler considers that Pod's
`overhead` as well as the sum of container requests for that Pod. For this example, the scheduler adds the
requests and the overhead, then looks for a node that has 2.25 CPU and 320 MiB of memory available.

Once a Pod is scheduled to a node, the kubelet on that node creates a new cgroup for the Pod. It is within this pod that the underlying
container runtime will create containers.

If the resource has a limit defined for each container (Guaranteed QoS or Burstable QoS with limits defined),
the kubelet will set an upper limit for the pod cgroup associated with that resource (cpu.cfs_quota_us for CPU
and memory.limit_in_bytes memory). This upper limit is based on the sum of the container limits plus the `overhead`
defined in the PodSpec.

For CPU, if the Pod is Guaranteed or Burstable QoS, the kubelet will set `cpu.shares` based on the
sum of container requests plus the `overhead` defined in the PodSpec.

Looking at our example, verify the container requests for the workload:

The total container requests are 2000m CPU and 200MiB of memory:

Check this against what is observed by the node:

The output shows requests for 2250m CPU, and for 320MiB of memory. The requests include Pod overhead:

## Verify Pod cgroup limits

Check the Pod's memory cgroups on the node where the workload is running. In the following example,
`crictl`
is used on the node, which provides a CLI for CRI-compatible container runtimes. This is an
advanced example to show Pod overhead behavior, and it is not expected that users should need to check
cgroups directly on the node.

First, on the particular node, determine the Pod identifier:

From this, you can determine the cgroup path for the Pod:

The resulting cgroup path includes the Pod's `pause` container. The Pod level cgroup is one directory above.

In this specific case, the pod cgroup path is `kubepods/podd7f4b509-cf94-4951-9417-d1087c92a5b2`.
Verify the Pod level cgroup setting for memory:

This is 320 MiB, as expected:

### Observability

Some `kube_pod_overhead_*` metrics are available in kube-state-metrics
to help identify when Pod overhead is being utilized and to help observe stability of workloads
running with a defined overhead.

## 

* Learn more about RuntimeClass
* Read the PodOverhead Design
  enhancement proposal for extra context
