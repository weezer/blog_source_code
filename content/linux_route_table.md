Title: Intro to linux route table
Date: 2017-02-15 00:01
Category: Tech
Tags: tech
Slug: linux_route_table
Authors: Weezer Su
Summary: Linux route table intro
转的，去年做了一个一模一样的，居然给忘了，哎。

[原链接](http://www.cnblogs.com/gergro/archive/2008/12/25/1362450.html)
这个更好 [Linux as a router](http://wiki.fatduck.org/networking/linux-as-a-router)

you can have all kinds of devices on your computer, switch(bridge), pc, think about how to make a linux server to a router,
think about tha difference between tap device and phsical network card. at the time when you create a bridge, it's the same
as you create a vNIC on the host but has more features.

```
apt-get install brctl-utils
sudo ip netns add ns1 
sudo ip netns add ns2 
sudo brctl addbr br-test
sudo brctl stp br-test off 
sudo ip link set dev br-test up
sudo ip link add tap1 type veth peer name br-tap1
sudo ip link set tap1 netns ns1
sudo brctl addif br-test br-tap1
sudo ip netns exec ns1 ip link set dev tap1 up
sudo ip link set dev br-tap1 up 
sudo ip link add tap2 type veth peer name br-tap2
sudo ip link set tap2 netns ns2
sudo brctl addif br-test br-tap2 
sudo ip netns exec ns2 ip link set dev tap2 up
sudo ip link set dev br-tap2 up 
sudo ip netns exec ns1 ip addr add 192.168.1.1/24 dev tap1
sudo ip netns exec ns2 ip addr add 192.168.1.2/24 dev tap2
sudo ip netns exec ns1 ping 192.168.1.2 -c 1
sudo echo 1 > /proc/sys/net/ipv4/ip_forward
sudo ip addr add 192.168.1.3/24 dev br-test
sudo iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i br-test -o eth0 -j ACCEPT
sudo iptables -A FORWARD -o br-test -i eth0 -j ACCEPT
sudo ip netns exec ns1 ip route add default via 192.168.1.3
sudo ip netns exec ns2 ip route add default via 192.168.1.3
```

现在有五个设备，PC1接ROUT1，ROUT1再接ROUT2，ROUT2再接ROUT3，ROUT3再接PC2，拓扑图见下：

□————○————○————○————□

PC1 ROUT1 ROUT2 ROUT3 PC2

五个设备的静态IP地址分别为：

PC1 192.168.1.88/24

ROUT1 192.168.1.128/24 192.168.2.128/24

ROUT2 192.168.2.66/24 192.168.3.66/24

ROUT3 192.168.3.100/24 192.168.4.33/24

PC2 192.168.4.66/24

PC1配置如下：

#ifconfig eth0 192.168.1.88 netmask 255.255.255.0

#route add default gw 192.168.1.128

ROUT1配置如下：

#ifconfig eth0 192.168.1.128 netmask 255.255.255.0

#ifconfig eth0: 1 192.168.2.128 netmask 255.255.255.0

#route add -net 192.168.4.0/24 gw 192.168.2.66

ROUT2配置如下：

#ifconfig eth0 192.168.2.66 netmask 255.255.255.0

#ifconfig eth0: 1 192.168.3.66 netmask 255.255.255.0

#route add -net 192.168.1.0/24 gw 192.168.2.128

#route add -net 192.168.4.0/24 gw 192.168.3.100

ROUT3配置如下：

#ifconfig eth0 192.168.3.100 netmask 255.255.255.0

#ifconfig eth0: 1 192.168.4.33 netmask 255.255.255.0

#route add -net 192.168.1.0/24 gw 192.168.3.66

PC2配置如下：

#ifconfig eth0 192.168.4.66 netmask 255.255.255.0

#route add default gw 192.168.4.33

这样PC1就能ping通PC2了。

注：

上面三个路由器这里用三台PC代替。用电脑代替路由器，必须要启用电脑的IP转发功能，改/proc/sys/net/ipv4/ip_forward里的内容为1（默认为0），用下面的命令完成

＃e cho 1 > /proc/sys/net/ipv4/ip_forward

网络重启后，上面的文件自动改为0

补充几个命令：

1、删除默认路由

#route del default

2、查看路由

#route -n

3、设置指定网段路由

#route add -net 192.168.3.0 netmask 255.255.255.0 gw 192.168.6.66

或者

#route add -net 192.168.3.0/24 gw 192.168.6.66

4、删除指定网段路由

#route del -net 192.168.3.0 netmask 255.255.255.0

或者

#route del -net 192.168.3.0/24
