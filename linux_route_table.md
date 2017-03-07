Title:Some Computer Science and devops books 
Date: 2016-12-29 17:32
Category: Tech
Tags: tech
Slug:
Authors: Weezer Su
Summary: Intro to linux route table
转的，去年做了一个一模一样的，居然给忘了，哎。

[原链接](http://www.cnblogs.com/gergro/archive/2008/12/25/1362450.html)


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
