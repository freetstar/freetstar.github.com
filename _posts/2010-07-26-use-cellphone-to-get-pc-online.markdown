---
author: admin
comments: true
date: 2010-07-26 10:32:31
layout: post
title: 小记：ubuntu下用手机做猫上网
wordpress_id: 1028
categories:
- 软件安装
---

从学校回到家，家里却没有网，很悲剧的没有网。。。

想办法吧，记得同学以前在XP下用NOKIA的PC套件把手机做为猫上网 ：（，我电脑中没有XP也没有WIN 7,只能另想办法。google一下，发现真还有在ubuntu下通过手机上网的方法。

环境：Nokia 5320  Ubuntu 10.04  手机cmnet上网

1.工具准备

    sudo apt-get install gnome-ppp

    sudo apt-get install wvdial  (系统应该是默认安装了)

2.使用usb数据线,将手机连接到电脑.本人选择的是PC套件模式  

运行dmesg 或 cat /var/log/messages 命令，查看识别出的tty设备名称...一般是ttyACM0或ttyACM1...

    tty设备名称需要仔细查找  

3.打开应用程序->互联网->gnome-ppp. 点击Setup, 并在modem命令栏中Device配置旁点击Detect. 

此时gnome-ppp将自动查找modem设备...应该能查找到刚刚看到的ttyACM0或ttyACM1.

4.同样在gnome-ppp的Setup中,设置init Strings的init3为  

AT+CGDCONT=1,"IP","cmnet" （注意标点符号和双引号）

5.回到gnome-ppp主窗口,  

Phone numbers 为*99***1#，.随意填写用户名和密码,然后点击connect... 等待connect成功...可以在"Detail"中查看连接情况,,或者使用cat /var/log/messages查看...

应该会出现.  

GNOME PPP: STDERR: --> PPP negotiation detected.

GNOME PPP: STDERR: --> Starting pppd at Mon Jul 26 10:02:04 2010

GNOME PPP: STDERR: --> Pid of pppd: 7809

GNOME PPP: STDERR: --> Using interface ppp0

GNOME PPP: STDERR: --> local  IP address 10.40.60.76

GNOME PPP: STDERR: --> remote IP address 10.6.6.6

GNOME PPP: STDERR: --> primary  DNS address 211.138.106.2

GNOME PPP: STDERR: --> secondary DNS address 211.136.17.107

类似的信息。

6 设置完这些，我已经能够上网了 :)

参考资料：[http://sardis.ycool.com/post.2911493.html](http://sardis.ycool.com/post.2911493.html)

[http://forum.ubuntu.org.cn/viewtopic.php?t=107532](http://forum.ubuntu.org.cn/viewtopic.php?t=107532)

