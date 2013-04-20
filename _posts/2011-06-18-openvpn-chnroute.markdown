---
author: admin
comments: true
date: 2011-06-18 22:47:14
layout: post
slug: openvpn-chnroute
title: Linux下OpenVPN+chnroute聪明访问WEB
wordpress_id: 1747
categories:
- 服务器
---

Linux下搭建OpenVPN方法:[here](http://www.freetstar.com/index.php/vps-build-up-openvpn),默认搭建好OpenVPN之后所有流量和数据都是通过VPS上的OpenVPN server提出的,也就是自身的访问IP总是美国的IP,内地网站可能屏蔽外国IP,

还有就是数据绕了一圈之后速度肯定会慢很多,所以聪明访问WEB就很必要了

感谢Chnroutes项目,解决了问题,[here](http://code.google.com/p/chnroutes/wiki/Usage):

第一步,查看OpenVPN版本,本文采用的2.1版本的配置方法,底版本见wiki
    
    openvpn --version
    OpenVPN 2.1.0 x86_64-pc-linux-gnu [SSL] [LZO2] [EPOLL] [PKCS11] [MH] [PF_INET6] [eurephia] built on Jul 12 2010
    Originally developed by James Yonan
    Copyright (C) 2002-2009 OpenVPN Technologies, Inc. <sales@openvpn.net>

第二步:

下载python脚本:[here](http://chnroutes.googlecode.com/files/chnroutes.py),依次运行
    
    python chnroutes_openvpn_v2.1   //产生路由信息文件routes.txt
    sudo cat routes.txt >>/etc/openvpn/client.conf   //将routes.txt文件的内容添加到openvpn客户端的配置文件里
    sudo vim /etc/openvpn/client.conf
    在第一行添加max-routes 3000,保存退出

第三步:

sudo /etc/init.d/openvpn reload    //重新读取配置文件

分别访问[http://www.wangsu123.cn/](http://www.wangsu123.cn/)和[http://formyip.com/](http://formyip.com/),

如果成功,第一个应该显示为国内IP,如天津市XXXX,第二个显示的是VPS的IP地址

注:有特殊情况的可以改/etc/hosts配置文件.手动指定ip和域名

