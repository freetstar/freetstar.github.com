---
author: admin
comments: true
date: 2010-06-27 00:37:15
layout: post
slug: ubuntu-optimize-your-boot
title: ubuntu 开机启动优化
wordpress_id: 811
categories:
- ubuntu
- 软件安装
---

	 ubuntu10.04刚全新安装时开机时间只用25-30秒,可是用了一段时间后开机启动启动时间升到了1m20s左右.桌面壁纸出现后,面板的载入速度很慢,于是想到了优化开机启动项目

	 方法一:**利用系统自带的启动应用程序**
 
		 打开系统->首选项->启动应用程序,
 
		 一种是系统默认但是日常不经常使用的都可以停止掉,大概有:远程桌面,视觉辅助,蓝牙管理器,个人文件夹共享,硬件更新,电源管理,打印队列.Ubuntu one,Evolution 提醒,登录声音提醒,磁盘报告
 
		 另一种是安装软件后,程序自动加到启动应用程序中的,比如说小熊猫,conky,都可以自己删除

	 方法二:**使用boot-up  manager(推荐)**
 
		 以下boot-up manager简称为BUM
 
		 BUM简介:
 
		 在Debian系列的发行版里,系统启动时读取/etc/init.d 中的脚本文件,如果要让这些脚本不工作,需要改变脚本权限,但是这个很复杂,为了方便您搞乱自己的电脑,BUM用图形界面配置你系统的启动脚本
 
		 BUM安装:
 
		 sudo apt-get install bum
 
		 BUM使用:
 
		 在系统->应用程序 中找到bootup-manager
 
		 第一次使用多等待会,待软件生成磁盘缓存
 
		 选择"Advance",会出现3个选项卡summary,service,startup and shutdown script
 
		 ![](http://www.marzocca.net/Immagini/bum1.png)
 
		 在summary选项卡中,对系统的启动项进行配置
 
		 udevmonitor系统设备-留着,nvidia-kernel显卡内核-留着模块,plymouth开机动画-留着,network-manager网络管理器-留着,acpi-support电源以及热键管理-留着,pulseaudio声音管理-留着,kernleloops没明白什么作用-留着,preload开机预加载-留着,acpid-电源管理-关闭,apache2服务器-关闭,atd定时任务-关闭,bootlog开机log-关闭,cron定时任务-打开,cups打印机-关闭,mysql数据库-关闭,openvpn-关闭,ssh-关闭,tor中继服务-关闭,winbind-关闭........
 
		 系统安装的程序和软件不一样的话,summary选项卡中的内容也会有所不同,应根据个人情况调整.

	附:**查看系统开机时间方法**
 
		 打开软件中心,搜索bootchart,然后把搜索出来的两个软件都安装.
 
		 开机启动会后在**/var/log/bootchart文件夹下有一张PNG格式的图,如果是.****tgz的文件,可以执行**pybootchartgui开/var/log/bootchar/文件夹下的tgz文件.其中PNG的图记录了系统启动的一些列行为
 
		 bootchart是默认开机启动,如果你不喜欢,可以删除
 
		 sudo apt-get autoremvoe bootchart pybootchartgui --purge

	参考资料:

	[http://www.marzocca.net/linux/bumdocs.html](http://www.marzocca.net/linux/bumdocs.html)

	[http://www.marzocca.net/linux/bum.html](http://www.marzocca.net/linux/bum.html)

	[http://www.omgubuntu.co.uk/2010/06/bootchart-ubuntu-how-to.html](http://www.omgubuntu.co.uk/2010/06/bootchart-ubuntu-how-to.html)

