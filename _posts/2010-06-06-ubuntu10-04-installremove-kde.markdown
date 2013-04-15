---
author: admin
comments: true
date: 2010-06-06 22:14:28
layout: post
slug: ubuntu10-04-installremove-kde
title: ubuntu10.04 安装卸载KDE桌面之折腾记
wordpress_id: 279
categories:
- ubuntu
tags:
- ubuntu10.04 卸载KDE
---


	 记得09年7月份刚开始用的是Opensuse，桌面环境好像是KED1.5的，经常性崩溃阿，太让人无语了，动不动就崩溃，但是对linux也不熟悉，没有比较好的方法，后来就转ubuntu了






	今天看到[nenew](http://www.nenew.net/ubuntu-kde-444.html)的一片日志，加之网上对KDE华丽效果的赞美和KED的新闻，我心动了，小试牛刀了下。






	我没有用[nenew](http://www.nenew.net/ubuntu-kde-444.html)的使用PPA源的方式（此方法会安装最新的额KDE桌面），而是直接打开终端，运行命令





> 
	
> 
> 
	[code langague="bash"]sudo apt-get installl kubuntu-desktop[/code]
	
> 
> 






	 实验室网速很快，几分钟下载安装完毕。重启机器，发现开机图片变成蓝色的"Kubuntu"，直接进去的系统，没有之前的登录框






	 进去之后发现仍然是Gnome，再次重启发现仍然是直接进Gnome，无奈只好手动注销，然后在登录框选择KDE桌面，登录后一切正常。。后续略。。。。。鉴于1自己不怎么使用KDE2习惯了Gnome，就开始进行卸载KDE桌面环境。 试了试网上种种的卸载方法，都不成功






	我的方法





> 
	
> 
> 
		 打开新立得软件包管理器，在组别中选择KDE 桌面环境，把其中所有的标记删除即可。然后在搜索plymouth-theme-kubuntu-logo删除即可，个人认为是比较完美的方法
	
> 
> 






	折腾记完毕呼，，，unix shell 范例精解第八章页数好多。。。![;)](http://www.freetstar.com/wp-content/plugins/fckeditor-for-wordpress-plugin/ckeditor/plugins/smiley/images/wink_smile.gif)




