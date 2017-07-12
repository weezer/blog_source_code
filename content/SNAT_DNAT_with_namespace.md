Title:SNAT and DNAT within namespace.
Date:2017-04-10
Category: tech
Tags: tech
Slug: SNAT_DNAT_with_namespace
Authors: Weezer Su
Summary: Simulate floating ip address with SNAT and DNAT

Neutron with linux bridge gives vm instance floting ip address by doing snat and dnat, showing a example of the snat and dnat job below

```
ip add netns ns1
ip add netns ns2
ip add netns router

ip link add veth0 type veth peer name peer0
ip link add veth1 type veth peer name peer1

ip link set dev veth0 netns ns1
ip link set dev veth1 netns ns2
ip link set dev peer0 netns router
ip link set dev peer1 netns router

ip netns exec ns1 ip addr add 10.0.0.1/24 dev veth0

ip netns exec ns2 ip addr add 192.168.1.1/24 dev veth1

ip netns exece router ip addr add 10.0.0.2/24 dev peer1
ip netns exece router ip addr add 192.168.1.2/24 dev peer2
ip netns exece router ip addr add 10.0.0.99/24 dev peer2

#enable forward
echo "1" > /proc/sys/net/ipv4/ip_forward

#adding iptables snat and dnat

iptables -A PREROUTING -t nat -p icmp -d 10.0.0.99 -j DNAT --to 192.168.1.1

iptables -A POSTROUTING -t nat -p icmp -s 192.168.0.1 -j SNAT --to 10.0.0.99
#or
iptables -t nat -A POSTROUTING -j MASQUERADE

```
