---
author: admin
comments: true
date: 2010-10-20 19:28:28
layout: post
slug: ubuntu10-04-upgrade-to-ubuntu10-10-resolving-problems
title: ubuntu10.04升级至ubuntu10.10后解决的几个问题
wordpress_id: 1349
categories:
- 问题解决
---

> 
	
> 
> 
		 
	
> 
> 
	
> 
> 
		 
	
> 
> 
	
> 
> 
		之前被ubuntu9.10升级到10.04，出现了很多问题，记得的几个教训就是要保存好$HOME文件夹下的隐藏文件，还有就是尽量在升级之前把显卡驱动卸载了，在此记录一下自己升级后出现的问题和解决方法。
	
> 
> 
	
> 
> 
		 备份用户主目录下的隐藏配置文件 tar cvf home.tar.gz ./.* 
	
> 
> 
	
> 
> 
		1 开机进入桌面之后，窗口没有标题栏
	
> 
> 
	
> 
> 
		 这个现象有时候不升级系统时也会出现，没有研究过WHY！
	
> 
> 
	
> 
> 
		 解决方法：打开系统-首选项-启动应用程序中添加一个项目，命令为gnome-wm，即使用gnome-wm桌面管理器。还有一个办法就是在ubuntu-tweak的启动控制-回话控制-窗口管理器中将compiz-wm改为gnome-wm。
	
> 
> 





> 
	
> 
> 
		2 打开面板那里的位置中的例如主菜单时，提示没有为其注册相应的应用程序。
	
> 
> 
	
> 
> 
		 在桌面上右键一个文件夹，如果没有文件夹，新建一个，选择使用其他程序打开，然后在列表中选择用文件浏览器，或者输入命令nautilus都可以的，然后选择确定，问题解决
	
> 
> 





> 
	
> 
> 
		3 无线网卡驱动被正常加载，但是无法使用，网卡型号Intel Corporation PRO/Wireless 3945ABG，无线网卡控制开关不管用
	
> 
> 
	
> 
> 
		 参考资料：[http://forum.ubuntu.org.cn/viewtopic.php?f=116&t=296565](http://forum.ubuntu.org.cn/viewtopic.php?f=116&t=296565)
	
> 
> 
	
> 
> 
		 问题排除：cd /var/log;vi daemon.log 可以看到下边的话 NetworkManager[975]: <info> WiFi now disabled by radio killswitch
	
> 
> 
	
> 
> 
		 解决：sudo -i //切换到root用户
	
> 
> 
	
> 
> 
		 echo 1>/sys/class/rfkill/rfkill0/state
	
> 
> 
	
> 
> 
		 然后重启机器，无线网络打开
	
> 
> 
	
> 
> 
		 最根本的解决办法：sudo apt-get install rfkill
	
> 
> 
	
>     
>     <span style="color: rgb(0, 0, 0); font-size: 14px; font-style: italic; " class="Apple-style-span"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(51, 51, 51); ">4.</span><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(51, 51, 51); "><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(128, 0, 0); ">10.10 安装显卡驱动后开机关机启动logo</span><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(128, 0, 0); ">字体大,变为10.10的解决办法</span></span></span>
> 
> 





> 
	
>     
>     <span style="font-style: italic; " class="Apple-style-span"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; font-size: 14px; "><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">网址：<a style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(255, 17, 17); text-decoration: none; " href="http://forum.ubuntu.org.cn/viewtopic.php?f=49&t=265686">http://forum.ubuntu.org.cn/viewtopic.php?f=49&t=265686</a></span></span></span>
> 
> 





> 
	
>     
>     <span style="font-style: italic; " class="Apple-style-span"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; font-size: 14px; "><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">/etc/default/grub中 缺省是#GRUB_GFXMODE=640×480, 去掉#, 数字改为显卡支持的分辨率（我的没驱动时不支持宽屏分辨率，选择了1024x768x32，注意要加色深16或32，否则色深是4位的,很难看）。
>     /etc/grub.d/00_header中找到set gfxmode=${GRUB_GFXMODE}，后面加一行让plymouth和grub分辨率一样：</span></span></span>
> 
> 





> 
	
>     
>     <span style="font-style: italic; " class="Apple-style-span"><span style="font-family: 'lucida sans unicode', 'lucida grande', sans-serif; font-size: 14px; " class="Apple-style-span">代码: set gfxpayload=keep</span></span>
>     
>     <span style="font-style: italic; " class="Apple-style-span"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; font-size: 14px; "><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">保存后更新一下grub.cfg：</span></span></span>
>     
>     <span style="font-style: italic; " class="Apple-style-span"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; font-size: 14px; "><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">代码: sudo update-grub</span></span></span>
> 
> 






	 注：升级有风险！






	总结下：自己还是太菜了，或许尝试做LFS是对自己的一个提升！加油！ 




