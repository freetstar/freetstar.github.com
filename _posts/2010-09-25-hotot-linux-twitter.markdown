---
author: admin
comments: true
date: 2010-09-25 00:31:54
layout: post
title: '[转载]Hotot：Linux 下最新潮的 Twitter 客户端'
wordpress_id: 1304
categories:
- 软件安装
---

==============================================================

嘿，大家好，从今以后，我打算从今以后做[WOW！Ubuntu](http://wowubuntu.com/)的义务撰稿人，在[WOW！Ubuntu](http://wowubuntu.com/)发表一些关于UBUNTU/LINUX文章和其他类型的文章，我的博客就用来写我自己的一些瞎折腾的东西了，比如编程，生活，工作等。希望大家多踩踩[WOW！Ubuntu](http://wowubuntu.com/)！

==============================================================

虽然每天都有Linux下的twitter客户端象雨后春笋一样出现，但是Hotot绝对是目前Linux下新生的最新潮的Twitter客户端。

尽管是特别为Linux桌面设计的，但是给人的感觉更像是iphone或者Andorid的应用软件。她有光滑的动画过渡，具体其他twitter客户端的性能，反应敏捷-貌似这一切应该归功于软件底层是python吧。

[![](http://wowubuntu.com/wp-content/uploads/2010/09/Hotot_007-500x454.png)](http://wowubuntu.com/wp-content/uploads/2010/09/Hotot_007-500x454.png)

关于扩展：目前Hotot支持图像上传和全球定位，同时我们也期待有更多的第三方扩展出现。Hotot的良好的框架为第三方插件的出现提供了良好的条件

指示器小程序：同时在面板上有指示器小程序。包含了"展示"和"退出"这2个常用的选项。具体如图

[![](http://wowubuntu.com/wp-content/uploads/2010/09/Selection_0081.png)](http://wowubuntu.com/wp-content/uploads/2010/09/Selection_0081.png)

特点：和其他客户端一样，同样具有

* 回复
* 收信/发信
* 收藏/查看收藏
* 编辑资料
* 搜索
* 转推
* fo和unfo，block功能

项目主页： [http://www.hotot.org/](http://www.hotot.org/)

# 下载：

目前Hotot仍在Alpha阶段，官方网站没有给出正式的下载。您可以去Google Code上下载：[GoogleCode page](http://code.google.com/p/hotot/):

[hotot-win7_hg~20100921.12.7z](http://code.google.com/p/hotot/downloads/detail?name=hotot-win7_hg~20100921.12.7z)

# 安装：在压缩包中有ubutnu下的安装方法。

终端运行命令：

    sudo apt-get install python-webkit python-notify python-keybinder

解压缩之前下载的包，进入文件夹，运行

    ./install.ubuntu

提示输入密码时输入密码，就是这么简单

或者你可以制作deb包然后安装，运行命令

    dpkg-buildpackage -rfakeroot && sudo dpkg -i ../*.deb

其他Linux发行版安装方法情参见：[http://code.google.com/p/hotot/wiki/Installation_HOWTO](http://code.google.com/p/hotot/wiki/Installation_HOWTO)

<span style="font-size:16px;">备注：</span>

<span style="font-size:16px;">1 Hotot支持两种API：twip gtap使用方法：<a style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; text-decoration: none; color: rgb(204, 102, 0); border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; " href="http://code.google.com/p/hotot/wiki/HowToUseAPIProxy">http://code.google.com/p/hotot/wiki/HowToUseAPIProxy</a></span>

<span style="font-size:16px;">2 Hotot支持的代理：socks和http，使用方法：<a style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; text-decoration: none; color: rgb(204, 102, 0); border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; " href="http://code.google.com/p/hotot/wiki/HowToUseProxy">http://code.google.com/p/hotot/wiki/HowToUseProxy</a></span>

<span style="font-size:16px;">
强力推荐！</span>

来源：<a style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; text-decoration: none; color: rgb(204, 102, 0); border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; " href="http://wowubuntu.com/hotot.html">OMG! Ubuntu&&WOW！UBUNTU 

</a>
