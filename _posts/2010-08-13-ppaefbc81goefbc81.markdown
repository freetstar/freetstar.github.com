---
author: admin
comments: true
date: 2010-08-13 18:03:59
layout: post
slug: ppa%ef%bc%81go%ef%bc%81
title: 寻找PPA
wordpress_id: 1117
categories:
- ubuntu
- 软件安装
---

	PPA的定义：

> 
	
> 
> 
		 Personal Package Archives的缩写，个人软件包档案，Ubuntu Launchpad网站提供的一项源服务，允许个人用户上传软件源代码，通过Launchpad进行编译并发布为2进制软件包，作为apt/新立得源供其他用户下载和更新。
	
> 
> 

	PPA 使用指南：  

> 
	
> 
> 
		 [https://help.launchpad.net/Packaging/PPA](https://help.launchpad.net/Packaging/PPA) 
	
> 
> 

	关于PPA我的理解：

> 
	
> 
> 
		 许多新鲜但是un-stable的软件通常会在放在PPA中，供广大网友使用。要想尝鲜，尝试一些"特别"的程序，尝试新鲜的程序，来使用PPA吧！
	
> 
> 

	寻找PPA：

> 
	
> 
> 
		 1 使用Google Chrome的插件
	
> 
> 
	
> 
> 
		 插件名称：PPAsearch
	
> 
> 
	
> 
> 
		 插件下载：[HERE ](https://chrome.google.com/extensions/detail/jlmhakjgfcifidaaichkfplodeljkmpn?hl=zh-cn )  
	
> 
> 
	
> 
> 
		 插件使用：见下图，直接输入想要查询的软件名称即可
	
> 
> 
	
> 
> 
		 插件图示：    
	
> 
> 
	
> 
> 
		 ![](https://chrome.google.com/extensions/img/jlmhakjgfcifidaaichkfplodeljkmpn/1280069290.86/screenshot/1?hl=zh-cn)
	
> 
> 

> 
	
> 
> 
		 2 通过命令行来寻找和添加PPA 
	
> 
> 
	
> 
> 
		 打开终端，输入：  
	
> 
> 
	
> 
> 
		** sudo add-apt-repository ppa:wrinkliez/ppasearch**
	
> 
> 
	
> 
> 
		** sudo apt-get update && sudo apt-get install ppasearch**
	
> 
> 
	
> 
> 
		 安装好之后，终端输入
	
> 
> 
	
> 
> 
		 ppasearch ppaname  //将ppaname换成你要寻找的ppa，然后根据提示选择和安装PPA，再多的我相信你懂得:)
	
> 
> 

> 
	
> 
> 
		 3  使用Ubuntu-tweak或者Ailurus来添加PPA
	
> 
> 
	
> 
> 
		 打开Ubuntu-tweak的软件源中心，如下图
	
> 
> 
	
> 
> 
		 ![](http://www.ubuntugeek.com/wp-content/uploads/2010/07/ubuntu-tweak-055-ppa-purge.png)
	
> 
> 
	
> 
> 
		 然后就是添加PPA了    
	
> 
> 
	
> 
> 
		 打开Ailurus的第三放软件源
	
> 
> 
	
> 
> 
		 ![](http://tdt.sjtu.edu.cn/ailurus/wp-content/uploads/2009/12/Screenshot-Ailurus-cn.png)
	
> 
> 
	
> 
> 
		 见图中的第三方源即是PPA
	
> 
> 

	PPA的基本使用命令：

> 
	
> 
> 
		 第一步：sudo add-apt-repository  ppa  //添加PPA，请参考找到的ppa的说明填写"ppa"
	
> 
> 
	
> 
> 
		 第二步：sudo apt-get update  //更新
	
> 
> 
	
> 
> 
		 第三步 ： sudo apt-get install packagename  //packagename就是你要安装的软件包 
	
> 
> 

	 注意："寻找ppa 1"中基本上都需要运行上述命令来完成ppa的添加和软件的下载  "寻找ppa2,3"基本不需要  

	 记：万变不离其宗

