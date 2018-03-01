Title: What's the difference between ClusterIP, NodePort and LoadBalancer service types in Kubernetes?
Date: 2017-09-21 15:04
Category: tech
Tags: tech, kubernetes
Slug: kubernetes-1 
Authors: Weezer Su
Summary: ClusterIP, NodePort, LoadBalancer


A ClusterIP exposes the following:

```spec.clusterIp:spec.ports[*].port```

You can only access this service while inside the cluster. It is accessible from its spec.clusterIp port. If a spec.ports[*].targetPort is set it will route from the port to the targetPort. The CLUSTER-IP you get when calling kubectl get services is the IP assigned to this service within the cluster internally.

A NodePort exposes the following:

```<NodeIP>:spec.ports[*].nodePort
spec.clusterIp:spec.ports[*].port```
If you access this service on a nodePort from the node's external IP, it will route the request to spec.clusterIp:spec.ports[*].port, which will in turn route it to your spec.ports[*].targetPort, if set. This service can also be accessed in the same way as ClusterIP.

Your NodeIPs are the external IP addresses of the nodes. You cannot access your service from <ClusterIP>:spec.ports[*].nodePort.

A LoadBalancer exposes the following:

```spec.loadBalancerIp:spec.pops[*].port
<NodeIP>:spec.ports[*].nodePort
spec.clusterIp:spec.ports[*].port```
You can access this service from your load balancer's IP address, which routes your request to a nodePort, which in turn routes the request to the clusterIP port. You can access this service as you would a NodePort or a ClusterIP service as well.

in my case, ```ssh -i id_rsa_core -L 4443:10.3.178.15:443 core@172.99.77.15``` then i can open the webpage on brower by localhost:4443 to verify that within the same cluster you do can reach the service by clusterIP:port 
