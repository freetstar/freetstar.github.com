---
author: admin
comments: true
date: 2010-07-06 22:43:43
layout: post
slug: flashget-linux-1-0
title: 快车(Flashget) for Linux 1.0版(2010.7.06)发布!
wordpress_id: 924
categories:
- ubuntu
- 软件安装
---

![](http://bbs.flashget.com/attachments/day_100706/10070615496740cbfed7dd094d.jpg)

flashget for Linux - Readme

===========================

Flashget 网际快车 for Linux 

Linux下面的多源下载工具

Features

========

- 多线程
- 下载速度快
- 支持快车专用链
- 支持FireFox浏览器
- 下载功能与windows快车一样（bt稍后加入）

测试环境

========

Ubuntu 10.04

Red Hat Enterprise Linux AS4.0

安装

====

    $tar zxvf wxFlashget-1.0.tar.gz

    $sudo make install

wxFlashget就会安装在您的/usr/loca/bin目录下面名称为wxFlashget

配置文件目录位置: ~/.flashget

默认下载保存地址: ~/Download

Bug List

========

1,Ubunt 10.04下面无法启动,提示找不到libexpat.so.0

error while loading shared libraries: libexpat.so.0: cannot open shared object file: No such file or directory

原因,编译flashget使用的是libexpat.so.0版本,系统默认为libexpat.so.1.5.2,做软连接即可.

    $cd /usr/lib

    $sudo ln -s libexpat.so.1.5.2 libexpt.so.0

    $sudo ldconfig

问题反馈

========

http://bbs.flashget.com/forumdisplay.php?fid=31

下载地址:[HERE](http://bbs.flashget.com/attachment.php?aid=MTMxN3w4NWUwZDk3YXwxMjc4NDI2MjIzfDMzYjZ0bHlyRUdLQ2JxK0xaOHFhSjEzSXljaWpZVExXa0ZHUDArSGw4NHFpbWZj)

使用笔记:  

1 附件中README的sudo ln -s libexpat.so.1.5.2 libexpt.so.0拼写错误.

2  我的PC中/usr/lib 只有libexpat.so ,没关系,都是做软链接,同样的道理.运行命令

    sudo ln -s  /usr/lib/libexpat.so /usr/lib/libexpat.so.0

3  做好上述工作后,我直接在文件夹下运行./wxFlashget,提示错误.加权限后sudo ./wxFlashget运行正常

