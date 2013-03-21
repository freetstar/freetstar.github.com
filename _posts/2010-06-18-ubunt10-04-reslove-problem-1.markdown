---
comments: true
date: 2010-06-18 20:19:59
layout: post
slug: ubunt10-04-reslove-problem-1
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 252
categories:
- 生活
---


	从ubuntu9.04初使，到ubuntu10.04期间，，遇到了很多问题，学习了很多东西，解决了很多问题。这次着重以ubuntu10.04为重点讲自己以来解决问题的方法。本文会不断更新。





> 
	
> 
> 
		1.系统升级问题
	
> 
> 
	
> 
> 
		我的电脑是ubuntu9。10，从9.10直接升级到10.04 ，参考此帖<!-- more -->
	
> 
> 
	
> 
> 
		[https://help.ubuntu.com/community/LucidUpgrades](https://help.ubuntu.com/community/LucidUpgrades)
	
> 
> 
	
> 
> 
		就是要打开更新管理器，单击检查更新，查看是否有需要更新的，如果有，安装更新，目的是保持系统最新。右上角会提示有最新版本可用，直接点击更新即可，静待系统更新完毕。
	
> 
> 
	
> 
> 
		PS：我直接从9.10更新到10.04，期间一切顺利，安装完毕后显卡驱动提示已经激活，可是却无法使用。于是在硬件驱动里卸载驱动，重启后再在新立得软件管理器中安装，安装完毕后重启进入系统，发现标题栏消失，只好打开终端输入 metacity -replace & ，使标题栏重现，但是这样一直无法开启3D效果。加上想体验ubuntu10.04的最新安装界面，于是系统重装。之前因为把/home目录独立分出来的，所以没有格式化/home分区，安装系统后标题栏依旧消失，同时和3D效果有冲突，灵光一现，突然想起来用户主目录下的.隐藏文件有许多配置文件，会不会产生冲突，于是删除了许多隐藏的配置文件，注销后进入系统，发现正常，标题栏重现，3D正常。至于是哪个隐藏文件导致的还不清楚，但是因为自己删除了很多的隐藏文件，导致google，firefox的一些书签，和一些软件原有的配置文件都消失了，吸取经验把，下次的时候要保存好了，做个备份.
	
> 
> 





> 
	
> 
> 
		2.9.10和10.04手动安装显卡驱动的问题
	
> 
> 
	
> 
> 
		[http://www.linuxidc.com/Linux/2010-05/25867.htm](http://www.linuxidc.com/Linux/2010-05/25867.htm)
	
> 
> 
	
> 
> 
		 卡驱动有俩种，来自官方和第三方。第三方的驱动为系统软件仓库里的那个版本。第三方的版本有很多显示问题。我的显卡配置为Nvidia 8400GS
	
> 
> 
	
> 
> 
		第一步：备份xorg.conf  

		sudo cp /ect/X11/xorg.conf /ect/X11/xorg.conf.backup
	
> 
> 
	
> 
> 
		第二部： 下载官方驱动
	
> 
> 
	
> 
> 
		网址：[http://www.nvidia.cn/object/linux-display-ia32-195.36.24-cn.html](http://www.nvidia.cn/object/linux-display-ia32-195.36.24-cn.html)
	
> 
> 
	
> 
> 
		第三步、安装头文件  

		sudo apt-get install linux-headers-$(uname -r) build-essential
	
> 
> 
	
> 
> 
		第四步、删除已安装的旧版Nvidia驱动程序  

		打开Ubuntu软件中心，在"已安装的软件"中搜索Nvidia，即可见到受限驱动，选择将其删除，然后 删除与之相关的不再被需要的程序。或者使用新立得软件包管理器  

		sudo apt-get autoremove 
	
> 
> 
	
> 
> 
		第五步、关闭gdm  

		按住Ctrl+alt+F1，进入文本模式，登录后关闭gdm。 这里推荐你将这篇文章复制到root下，去除一些中文，在文本模式下可以用vi查看，如果你记不住命令的话  

		sudo /etc/init.d/gdm stop 
	
> 
> 
	
> 
> 
		第六步、删除旧版驱动残余  

		sudo rmmod nvidia  

		sudo rm -r -f /lib/modules/2.6.31-14-generic/kernel /drivers/video/nvidia /*注意此处2.6.31-14-generic为内核版本，不同的内核此处不一样*/ 
	
> 
> 
	
> 
> 
		第七步、安装新版驱动  

		sudo sh *.run
	
> 
> 





> 
	
> 
> 
		3.10.04安装flash之后仍然有方格的解决办法
	
> 
> 
	
> 
> 
		我的解决办法 sudo rm /etc/fonts/conf.d/49-sansserif.Conf
	
> 
> 
	
> 
> 
		网址：[http://wwwww.ylmf.net/read.php?tid=1604327](http://wwwww.ylmf.net/read.php?tid=1604327)
	
> 
> 
	
> 
> 
		打开ubuntu软件中心，安装Adobe Flash  

		安装好官方的flash player后，却发现其中的动态中文字体显示为方块，用以下方法解决  

		方法一：（不推荐，因为某些情况下会造成字体混乱）  

		删除一个字体的设置文件后，重新启动firefox解决问题。  

		终端执行命令：  

		$ sudo rm /etc/fonts/conf.d/49-sansserif.Conf  

		方法二：（推荐）  

		终端执行命令：  

		sudo mv /etc/fonts/conf.d/49-sansserif.conf /etc/fonts/conf.d/99-sansserif.Conf  

		方法三：（强力推荐）  

		终端执行命令：sudo gedit /etc/fonts/conf.d/49-sansserif.conf  

		将倒数第4行内容替换成：<string>文泉驿正黑</string>  

		保存之后，重启firefox，flash乱码解决。
	
> 
> 





> 
	
> 
> 
		4.10.04 安装显卡驱动后开机关机启动logo字体大的解决办法
	
> 
> 
	
> 
> 
		网址：[http://forum.ubuntu.org.cn/viewtopic.php?f=49&t=265686](http://forum.ubuntu.org.cn/viewtopic.php?f=49&t=265686)
	
> 
> 
	
> 
> 
		/etc/default/grub中 缺省是#GRUB_GFXMODE=640x480, 去掉#, 数字改为显卡支持的分辨率（我的没驱动时不支持宽屏分辨率，选择了1024x768x32，注意要加色深16或32，否则色深是4位的,很难看）。  

		/etc/grub.d/00_header中找到set gfxmode=${GRUB_GFXMODE}，后面加一行让plymouth和grub分辨率一样：
	
> 
> 
	
> 
> 
		代码: set gfxpayload=keep
	
> 
> 
	
> 
> 
		保存后更新一下grub.cfg：
	
> 
> 
	
> 
> 
		代码: sudo update-grub
	
> 
> 
	
> 
> 
		ubuntu中的adobe reader在一定的情况下无法显示中文和日文等情况
	
> 
> 
	
> 
> 
		网址：[**http://hi.baidu.com/lbxthinker/blog/item/a44ec71a07290ff3af51338f.html**](http://hi.baidu.com/lbxthinker/blog/item/a44ec71a07290ff3af51338f.html)
	
> 
> 






	  

	





> 
	
> 
> 
		5.Adobe Reader打开中文和日文等出现乱码情况
	
> 
> 
	
> 
> 
		在ubuntu10.04 中文平台上，通过ubuntu-tweak安装装了个Adobe Reader9英文版，可是打开中文pdf文档时，显示缺乏中文字体支持，故按照提示在官网
	
> 
> 
	
> 
> 
		[http://www.adobe.com/products/acrobat/acrrasianfontpack.html](http://www.adobe.com/products/acrobat/acrrasianfontpack.html)
	
> 
> 
	
> 
> 
		下了个简体中文包FontPack81_chs_i486-linux.tar.gz，在终端输入 sudo ./INSTALL,其中INSTALL是解压后的sh安装脚本。按照提示安装，出现这一步让你选adobe的安装目录，  

		Enter the location where you installed the Adobe Reader [/opt]：  

		但是输入/opt不成功，故去检查INSTALL脚本，跟踪到TestInstallDir这个安装目录测试函数，发现 if [ ! -d "$dir/Adobe/Reader8/Reader" -o ! -d "$dir/Adobe/Reader8/Resource" ] ，说明此语言包是针对adobe Reader8的，而adobe Reader9的目录是/opt/Adobe/Reader9,归根结底是版本问题，可是官网没有9.0的语言安装包，并且官网跟安装提示都说FontPack81_chs_i486-linux.tar.gz要求adobe reader 的版本为8.0或者更高版本，太搞了，大bug一个。所以解决途径是要么修改INSTALL脚本，要么先修改/opt/Adobe/Reader9为/opt/Adobe/Reader8，然后改回来。这样，问题得以解决。
	
> 
> 





> 
	
> 
> 
		6  前端时间重做系统后又安装了一遍nvidia显卡驱动，开机的时候显示有nvidia的logo。
	
> 
> 
	
> 
> 
		下面附解决方案：[http://wiki.ubuntu.org.cn/index.phptitle=Index/guide/DisableNVIDIALogo&variant=zh-hant](http://wiki.ubuntu.org.cn/index.phptitle=Index/guide/DisableNVIDIALogo&variant=zh-hant)
	
> 
> 
	
> 
> 
		首先留个备份，然后编辑
	
> 
> 
	
> 
> 
		sudo cp /etc/X11/xorg.conf /etc/X11/xorg.conf_backup
	
> 
> 
	
>     
>     <span style="font-size:14px;"><span style="font-family:comic sans ms,cursive;"><span style="color: #000000;">sudo gedit /etc/X11/xorg.conf</span>
>     <span style="color: #000000;">找到Section "Device"。俺的是10.04的。所以可能与原网页的不太一样。</span><span style="color: #000000;"> </span></span></span>
>     
>     <span style="font-size:14px;"><span style="font-family:comic sans ms,cursive;"><span style="color: #000000;"> </span>增加：Option "NoLogo"</span></span>
>     
>     <span style="font-size:14px;"><span style="font-family:comic sans ms,cursive;"><span style="color: #000000;">保存后重启，发现一切ok。</span></span></span>
> 
> 






	  

	






	  

	






	  

	




