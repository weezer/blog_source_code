Title: Netflix 的 simian army 
Date: 2017-01-19 22:07
Category: tech
Tags: tech
Slug:Netflix_Simian_Army 
Authors: Weezer Su
Summary: netflix 的云工具。

是从这篇文章抄的，感觉很有意思。[simian army](http://techblog.netflix.com/2011/07/netflix-simian-army.html)

Members of the Simian Army include:
-----------------------------------

1. Chaos Monkey - randomly shuts down virtual machines (VMs) to ensure that small disruptions will not affect the overall service.
2. Latency Monkey - simulates a degradation of service and checks to make sure that upstream services react appropriately.
3. Conformity Monkey - detects instances that aren’t coded to best-practices and shuts them down, giving the service owner the opportunity to re-launch them properly.
4. Security Monkey - searches out security weaknesses, and ends the offending instances. It also ensures that SSL and DRM certificates are not expired or close to expiration.
5. Doctor Monkey - performs health checks on each instance and monitors other external signs of process health such as CPU and memory usage.
6. Janitor Monkey - searches for unused resources and discards them.


这些工具都是用来测试netflix的云的稳定性和可用性，值得参考.

下面是openstack的chaosmonkey

[os-faults](https://github.com/openstack/os-faults)
[os-client-config](https://github.com/openstack/os-client-config)

