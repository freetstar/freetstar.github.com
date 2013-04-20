---
author: admin
comments: true
date: 2010-05-28 17:52:11
layout: post
slug: ubuntu-9-10-simulation-platform
title: ubuntu 9.10 Robocup仿真组比赛环境安装配置
wordpress_id: 111
categories:
- ubuntu
tags:
- 9.10 Robocup
- ubuntu
---

	 比赛平台要求操作系统为ubuntu9.10-64bit。。64位机最好装64bit的操作系统，基本上跑32bit也不会出现问题。 首先给电脑陪好基本的网络环境，给机器选择好源(此部分参照上海的jandy的blog[http://ubuntuabc.com/123/](http://ubuntuabc.com/123/)此blog中有关于ubuntu系统配置的一些文档）。配置好系统之后，开始比赛平台的正式安装。 

	 比赛平台的安装 

	 （1）系统准备 

	 sudo apt-get install nautilus-gksu 把"管理员打开选项"添加到右键菜单中 

	 sudo apt-get install nautilus-open-terminal 把终端添加到右键菜单中 

	 sudo apt-get install rar unrar p7zip 安装解压缩程序 以上步骤是为了下边的安装的方便。这几个程序需要注销后才能生效 

	 (2)准备 下载包server monitor logger 网址：[http://sourceforge.net/projects/sserver/](http://sourceforge.net/projects/sserver/) 网址内有各种版本的包，应根据实际情况进行选择，同时每个版本的发行日志应该下载阅读。同时还有其他的工具，如观看录像工具。

	 （3）前期安装 

	 在终端中输入以下命令

	 sudo apt-get install build-essential //基本的编译器GCC等 

	 sudo apt-get install xorg-dev //xorg图形界面

	 sudo apt-get install flex bison //词法分析器生成器 语法分析器 

	 sudo apt-get install libboost-dev //安装boost库 

	 sudo apt-get install libqt4-dev libqt4-debug libqt4-gui libqt4-sql qt4-dev-tools qt4-doc qt4-designer qt4-qtconfig //qt4的应用程序 

	 sudo apt-get install X11-dev 

	 可能libqt4-sql，libqt4-debug都不能用。只要在上述命令中删除即可 

	 （4）前期准备完毕后

	 解压相应的rcssserver rcssmonitor文件夹，在文件夹右键单击在终端中打开。

	 依次输入下面命令 

	 sudo ./configure //配置库等一系列东西 

	 sudo make  sudo make install //必须在root下装 

	 sudo /sbin/ldconfig //修改软件数据库 缓存 

	 安装后测试：终端输入rcssserver 和rcssmonitor 

	 当rcssmonitor看不到球员的时候需要卸载网络管理器  sudo apt-get autoremove network-manager --purge (个人猜测可能是软件冲突的原因，或者网络端口冲突) 

	 (5)另一种安装方法（未尝试使用过） 大概方法是： 进入系统/系统管理/软件源，在软件源对话框中切换到第三方软件页面，点击添加：

	 deb http://ppa.launchpad.net/gnurubuntu/rubuntu/ubuntu karmic main 

	 deb-src http://ppa.launchpad.net/gnurubuntu/rubuntu/ubuntu karmic main

	 安装Server：  sudo apt-get update sudo apt-get install rcssserver rcsslogplayer 

	 具体网址见： [https://launchpad.net/~rm1232002/+archive/rcss+lucid](https://launchpad.net/~rm1232002/+archive/rcss+lucid) PS：有的安装步骤需要权限，请加sudo 情况可能有所变化，但万变不离其宗。。。

	 比赛平台的配置与安装的ubuntu操作系统有关，有的库和软件装时本身已安装。建议用DVD安装ubuntu。或者安装完毕后以DVD作为一个更新的数据源。为了方便系统重装和实现离线升级，把第一次在/var/cache/apt/archives的deb包找到并复制保存，待以后使用

�据源。为了方便系统重装和实现离线升级，把第一次在/var/cache/apt/archives的deb包找到并复制保存，待以后使用

