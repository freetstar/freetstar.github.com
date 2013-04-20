---
author: admin
comments: true
date: 2011-04-04 10:53:37
layout: post
slug: let-rfkill-control-your-linux-wireless-devices
title: 用rfkill来控制linux下的无线设备
wordpress_id: 1656
categories:
- 软件安装
---

我的hpv3608,ubuntu从10.04升级到10.10之后，无线控制的那个开关就一直没有办法用，无论拨向那一边都无法打开无线。在ubuntu中文论文找到了rfkill这一个线索

rfkill的安装

sudo apt-get install rfkill

使用：
	
  1. man rfkill
	
  2. [看红帽的文档](http://docs.redhat.com/docs/zh-CN/Red_Hat_Enterprise_Linux/6/html/Power_Management_Guide/RFKill.html)
	
  3. [看kernel的介绍](http://www.mjmwired.net/kernel/Documentation/rfkill.txt)
	
  4. 具体实践

rfkill list//查看了有那些设备

rfkill unblock all//将所有的无线设备都unblock

开机启动后无线设备运行良好

