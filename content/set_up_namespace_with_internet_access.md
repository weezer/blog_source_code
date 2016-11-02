Title: Setup a network namespace with internet access 
Date: 2016-10-14 12:00
Category: Tech
Tags: code, python, network
Slug: set_up_namespace_with_internet_access 
Authors: Weezer Su
Summary: Setup a network namespace with internet access.


```bash
#!/usr/bin/env bash

#namespace="ns1"
#VETH="veth1"
#VPEER="vpeer1"
#VETH_ADDR="192.168.0.1"
#VPEER_ADDR="192.168.0.2"


# Create namespace
ip netns add ns1

# Create veth link.
ip link add veth0 type veth peer name vpeer1

# Add peer-1 to NS.
ip link set vpeer1 netns ns1

# Setup IP address of veth.
ip addr add 192.168.0.1/24 dev veth0
ip link set veth0 up

# Setup IP for peer.
ip netns exec ns1 ip addr add 192.168.0.2/24 dev vpeer1
ip netns exec ns1 ip link set vpeer1 up
ip netns exec ns1 ip link set lo up
ip netns exec ns1 ip route add default via 192.168.0.1

# Enable IP-forwarding.
echo 1 > /proc/sys/net/ipv4/ip_forward
#or permenant
# /etc/sysctl.conf:
# net.ipv4.ip_forward = 1


# Flush forward rules.
iptables -P FORWARD DROP
iptables -F FORWARD
 
# Flush nat rules.
iptables -t nat -F

# Enable masquerading of 192.168.0.0.
iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -o eth0 -j MASQUERADE
 
iptables -A FORWARD -i eth0 -o veth0 -j ACCEPT
iptables -A FORWARD -o eth0 -i veth0 -j ACCEPT

# Get into namespace
ip netns exec ns1 ping 8.8.8.8 
```

