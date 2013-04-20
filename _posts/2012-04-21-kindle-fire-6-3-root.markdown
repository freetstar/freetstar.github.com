---
author: admin
comments: true
date: 2012-04-21 22:55:20
layout: post
slug: kindle-fire-6-3-root
title: kindle fire 6.3 root记
wordpress_id: 1896
categories:
- 转载翻译
---

入了一个二手的kindlefire，￥950大洋，kindle fire的系统版本是6.3。附上自己的root过程。

参考的是[http://www.92kindle.com/thread-10746-1-1.html](http://www.92kindle.com/thread-10746-1-1.html)和[http://www.92kindle.com/thread-10607-1-1.html](http://www.92kindle.com/thread-10607-1-1.html)和[http://www.92kindle.com/thread-4631-1-1.html](http://www.92kindle.com/thread-4631-1-1.html)

准备工作，下载[http://115.com/file/dpfuifcq#Fire-6.3-ROOT.rar](http://115.com/file/dpfuifcq%23Fire-6.3-ROOT.rar) 和[http://115.com/file/aqufms4w#快速搭建KF的ADB环境.rar](http://115.com/file/aqufms4w#%E5%BF%AB%E9%80%9F%E6%90%AD%E5%BB%BAKF%E7%9A%84ADB%E7%8E%AF%E5%A2%83.rar)和[http://115.com/file/e7h6uzt2#U-Boot磁盘修复.rar](http://115.com/file/e7h6uzt2%23U-Boot%E7%A3%81%E7%9B%98%E4%BF%AE%E5%A4%8D.rar)

第一步：搭建ADB环境（什么是ADB：[here](http://www.anzhuoba.com/thread-12866-1-1.html)）

1 Kindle Fire连接至计算机，点击Disconnect断开Kindle Fire U盘模式

2 解压“快速搭建KF的ADB环境文件.rar”文件和“U-Boot磁盘修复.rar”文件

3复制文件夹里的.android文件夹至当前用户名文件夹下C:\用户\Administrator(win7用户)

4 打开控制面板->设备管理器，会有一个黄色叹号的Kindle设备，点击更新驱动程序软件，点击“浏览计算机以查找驱动程序软件”，选择“U-Boot磁盘修复”文件夹中的Drivers文件夹，选择“始终安装此驱动程序软件”（不使用快速搭建KF的ADB环境文件中的驱动，可能是驱动太老，有问题）

 

第二步：开始root

解压“Fire-6.3-ROOT.rar”文件，进入文件夹后按住shift并单击右键，打开命令窗口。

1 输入

**adb push fbmode /data/local/fbmode**  
  
**adb shell chmod 755 /data/local/fbmode**  
  
**adb shell /data/local/fbmode**  
  
**adb reboot**

2 Fire自动重启进入Fastboot模式，继续输入以下命令：  
  
**fastboot -i 0x1949 boot twrp-blaze-2.0.0RC0.img**

3 Fire自动进入TWRP安装，等Fire显示屏上出现Reboot按钮，点击Reboot继续输入以下命令  
  
**fastboot oem idme bootmode 5002**  
  
**fastboot reboot**

4 Fire自动重启，进入TWRP界面后，输入以下命令：  
  
**adb shell mount system**  
  
**adb push su /system/xbin/su**  
  
**adb shell chown 0.0 /system/xbin/su**  
  
**adb shell chmod 06755 /system/xbin/su**  
  
**adb shell idme bootmode 4000**  
  
**adb reboot**

5 Fire自动重启进入系统，输入以下命令安装Superuser：  
  
**adb install Superuser.apk**  
  
**adb install RE.apk**

6 重启后打开RE管理器，试着把/分区挂载成R/W，成功的话说明root成功

本身92kindle论坛的步骤大部分是ok的，但是kindle fire驱动那部分有问题，建议采用我说的方法。另外还有[kindle fire utility](http://forum.xda-developers.com/showthread.php?t=1399889)可以一键root，不过我没有成功。

ead.php?t=1399889)可以一键root，不过我没有成功。

