---
author: admin
comments: true
date: 2011-05-28 23:22:47
layout: post
slug: pygtk-linux-server
title: PyGTK做的Linux Server管理毕业设计
wordpress_id: 1718
categories:
- PROGRAM
---

很菜,我真的很菜,把项目公布出来我表示压力特别大,这个毕业设计软件最后写得越来越不知道该写什么,功能模块不知道要添加那些,已经实现的也不想再修改,可能自己惰性太大了

项目简单说明: 一个Linux Server的管理系统,可以添加服务器,将服务器添加到特定的组里,然后选定服务器,填好服务器的ip地址,端口号,用户名和密码,保存之后才能进行更多的操作,代码里并没有对ip地址这些东西做非法字符检测:(,可以通过点击按钮来获取服务器的实时信息,比如说内存,硬盘等等,还有就是通过发起TCP半链接来查看做简单的portscan,最后的功能是嵌入一个本地的虚拟终端

项目bug:硬盘信息获取之后图一直保留着,图形界面的显示有问题, 项目想法:其实还想实现一些这样的功能的,1:可以获取服务器整个快照,每天晚上获取一次 2 获取服务器关键文件比如说/etc/passwd的md5值,这样可以侦测服务器的/etc/passwd是否被更改,比如说被入侵的情况 3 利用expect实现本地终端自动登录服务器,省去手动输入ssh的过程 4 利用pychartdir等实现服务器流量的实时体现,但是网速是个问题 5 等等.... 6 状态栏是否能用的更好点

项目截图:     主界面:左侧是服务器的列表 右侧是主功能区 下边是状态栏     ![](http://i.imgur.com/xKLql.png)

硬盘情况显示:

![](http://i.imgur.com/kUCpV.png)

系统信息获取:

![](http://i.imgur.com/ryxYL.png)

传说中的跨平台的软件,实际上好多模块要移植,懒得弄了,这只是个皮子    ![](http://i.imgur.com/fZpAa.png)

总结:从3月开始正式学Python,到现在了,基本上把Python基础教程2来回翻了n次,Python在Unix和Linux系统管理这本书也给了我很多想法,想一步有可能的话我想做一个基于Python Django的一个这样的东西,当练手了.    项目整体不成熟,也是我代码水平不高的体现,许多bug还待修改,但是实在没感觉和兴趣了,有兴趣的话接手吧:

github:[ ](https://github.com/freetstar/Linux-Server-Management)[https://github.com/freetstar/Linux-Server-Management](https://github.com/freetstar/Linux-Server-Management)

google code:[https://code.google.com/p/linux-server-management-software/](https://code.google.com/p/linux-server-management-software/)
