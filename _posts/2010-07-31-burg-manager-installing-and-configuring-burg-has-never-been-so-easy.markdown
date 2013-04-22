---
author: admin
comments: true
date: 2010-07-31 12:10:29
layout: post
slug: burg-manager-installing-and-configuring-burg-has-never-been-so-easy
title: Burg-manager:让安装和配置Burg如此简单
wordpress_id: 1040
categories:
- 生活
---

	` 之前写过一篇文章：[用burg来美化你的ubuntu开机菜单](http://www.freetstar.com/index.php/burg-make-ur-ubuntu-bootloader)，burg的作用和Grub的作用一样，都是开机引导程序。上篇文章只是介绍了下Burg的基本安装和使用，本篇主要是介绍Burg-manager这个管理burg的软件。`

## 
	` 在我发表[用burg来美化你的ubuntu开机菜单](http://www.freetstar.com/index.php/burg-make-ur-ubuntu-bootloader)之后，Burg-manager软件的意大利作者[Ingalex](http://www.sourceslist.eu/)联系到我，说是否可以帮忙。一：翻译Burg-manager的软件简介 二：汉化Burg-manager，我欣然答应了（感觉我的英语应该基本够用吧）`

	 一：Burg-manager翻译

	 英文：[http://www.sourceslist.eu/page/2/](http://www.sourceslist.eu/page/2/)

	 中文：

	//Translation Begin

	 ![](http://www.sourceslist.eu/wp-content/uploads/2010/06/logoburgmanager.png)

	 由Ingalex & Canopus0003编写的Burg-manager，以[BUC](http://buc.billeragroup.net/?page_id=15)为基础。此软件的目标是通过简单直观的图形界面，来管理BURG 引导器，而无须使用终端命令。

	 这个对用户友好的发行版有以下功能：

	 --安装Burg，Burg主题和Burg模拟器

	 --设置超时时间

	 --设置您最喜欢的主题

	 --设置屏幕分辨率

	 --添加您在本站上找到的Burg主题

	 --移除Burg

	 --恢复Grub2

	 --设置默认启动系统

	 --设置高级参数

	 这些只需要轻轻一点！

	 以下功能将会很快实现：

	 --设置启动项，实现直接通过iso文件来启动系统

	 如果你想帮助我们发展这个项目，请[联系我们](http://www.sourceslist.eu/page/info/contattami/)。欢迎任何新的建议和想法。

	 以下是一些关于burg-manager的截屏

	 ![](http://www.sourceslist.eu/wp-content/uploads/2010/07/bm-150x150.png) ![](http://www.sourceslist.eu/wp-content/uploads/2010/07/bm1-150x150.png)![](http://www.sourceslist.eu/wp-content/uploads/2010/07/bm2-150x150.png)![](http://www.sourceslist.eu/wp-content/uploads/2010/07/bm3-150x150.png)

	 ![](http://www.sourceslist.eu/wp-content/uploads/2010/07/bm4-150x150.png)![](http://www.sourceslist.eu/wp-content/uploads/2010/07/bm5-150x150.png)![](http://www.sourceslist.eu/wp-content/uploads/2010/07/bm6-150x150.png)

	 如果您想使用Burg-Manager，首先您需要安装BUC，安装方法：

	 1 [源](http://buc.intilinux.com/wiki/index.php?title=Installare_BUC_tramite_repository)

	 2 [debian包](http://buc.intilinux.com/wiki/index.php?title=Installare_BUC_tramite_deb)

	 3 编译源代码

	 当您安装好BUC之后，下载对应你PC架构的Burg-Manager

				**Arch**

				**Name**

				**Version**

				**Download**

				**Downloads  

				**

				**i386**

				**burg-manager**

				**0.2.3**

					**[![download](http://www.sourceslist.eu/wp-content/uploads/2009/12/download.png)](http://www.sourceslist.eu/ccount/click.php?id=2)**

				4466

				**amd64**

				**burg-manager**

				**0.2.3**

					**[![download](http://www.sourceslist.eu/wp-content/uploads/2009/12/download.png)](http://www.sourceslist.eu/ccount/click.php?id=1)**

				1645  

	 运行命令

	 sudo dpkg -i burg-manager×

	 安装成功之后，您会在应用程序-系统工具中找到Burg-Manger

	 这个项目处在"胚胎"阶段，因此我将不会为任何因为Burg-manager导致的问题负任何责任

	** 从源中安装Burg-Manager**

> 
	
> 
> 
		 sudo gedit /etc/apt/sources.list
	
> 
> 

	 将下面添加进去

> 
	
> 
> 
		 deb http://www.sourceslist.eu/repo/ubuntu lucid main non-free
	
> 
> 

	 当然也可以这样

> 
	
> 
> 
		echo "deb http://www.sourceslist.eu/repo/ubuntu lucid main non-free" | sudo tee -a /etc/apt/sources.list
	
> 
> 

	 添加gpg key

> 
	
> 
> 
		 `sudo gpg --keyserver hkp://pgp.mit.edu --recv-keys FA088BA5 && sudo gpg --armor --export FA088BA5 | sudo apt-key add -`>
	
> 
> 

	 或者 

> 
	
> 
> 
		 wget http://www.sourceslist.eu/?download=public.key -O- | sudo apt-key add -
	
> 
> 

	 然后运行

> 
	
> 
> 
		 sudo apt-get update && sudo apt-get install burg-manager
	
> 
> 

	 想跟上Burg-manager发行版的脚步吗？假如facebook的[fan page](http://www.facebook.com/pages/Sourceslisteu/366814072412)吧

	//Translation end

	 二：软件汉化

	 汉化之初，[Ingalex](http://www.sourceslist.eu/) 提示我要更换中文编码以此来显示中文，我把所有中文编码都尝试了，可是显示出来的都还是乱码。。

	 之前自己也没有汉化的经验，故也在此求救，忘高人指点！

	 HELP！！！！！！！

