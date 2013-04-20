---
author: admin
comments: true
date: 2011-11-07 19:16:51
layout: post
slug: linux-limit-p2p-ing-host
title: linux下限制局域网内部使用p2p软件的主机
wordpress_id: 1865
categories:
- 服务器
---

windows下有p2p终结者，linux下咱有dsniff，介绍：[here](http://monkey.org/~dugsong/dsniff/)，其的用途之一就是做arp欺骗，具体命令是arpspoof.




作用：



    
    arpspoof将局域网内的目标主机或者是所有主机的发送数据包通过ARP欺骗来重指向。<br></br>在使用交换机的局域网环境下是一个非常有效的方法来嗅探数据：)




注意：kernel的ip转发必须要提前打开




使用：



    
    arpspoof [-i interface] [-t target] host



    
    -i 用来指示要使用的网卡接口，一般是eth0,



    
    -t 用来指示要欺骗的目标主机，如果不表明则默认为局域网内部的所有主机



    
    host 你要截取数据包的主机，通常是网关




具体使用：




环境archlinux ,要限制的ip为192.168.0.29，本机ip为192.168.0.24,实验室网管为192.168.0.1




1 安装



    
    sudo pacman -S dsniff




2 开启内核转发和欺骗



    
    #echo 1 > /proc/sys/net/ipv4/ip_forward




#欺骗192.168.0.29，告诉这台机器网关192.168.0.1的MAC地址是自己(192.168.0.24)。



    
    $sudo arpspoof -i eth0 -t 192.168.0.29 192.168.0.1




#欺骗192.168.0.1，告诉网关192.168.0.29的MAC地址是自己(192.168.0.24)



    
    $sudo arpspoof -i eth0 -t 192.168.0.1 192.168.0.29




_192.168.0.29以为192.168.0.24就是192.168.0.1，192.168.0.1以为192.168.0.24就是192.168.0.29_




3 利用iptables开始限速




#192.168.0.29被限制每秒只能传输3个数据包了



    
    $sudo iptables -A FORWARD -s 192.168.0.29  -m limit --limit 3/s -j ACCEPT           <br></br>$sudo iptables -A FORWARD -d 192.168.0.29 -m limit --limit 3/s -j ACCEPT                  <br></br>$sudo iptables -A FORWARD -s 192.168.0.29  -j DROP                                                 <br></br>$sudo iptables -A FORWARD -d 192.168.0.29  -j DROP   




4 当然，如果你想干坏事的话可以用 urlsnarf 或者wireshark之类的。。。。恩







参考资料：




[http://microcai.gsalex.net/archives/2010/11/p2p-killer-for-linux.html](http://microcai.gsalex.net/archives/2010/11/p2p-killer-for-linux.html)




[http://www.yuanma.org/data/2006/0914/article_1536.htm](http://www.yuanma.org/data/2006/0914/article_1536.htm)
