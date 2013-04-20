---
author: admin
comments: true
date: 2010-05-28 18:06:08
layout: post
slug: ubuntu10-04-robocup2d-platform
title: ' Ubuntu10.04    Robocup2D平台比赛安装'
wordpress_id: 114
categories:
- ubuntu
tags:
- ubuntu Robocup 2D 配置
---

经过robocup2009年中国比赛，agent2d在64位机器上跑起来没有问题。64位机最好装64bit的操作系统，32位的跑32bit也不会出现问题。

系统配置参考前边9.10的文档资料

（1）系统准备

[code language="bash"]sudo apt-get install nautilus-gksu[/code]

把“管理员打开选项”添加到右键菜单中

[code language="bash"]sudo apt-get install nautilus-open-terminal [/code]

把终端添加到右键菜单中

[code language="bash"]sudo apt-get install rar unrar p7zip[/code]

安装解压缩程序

以便安装进行下来的安装，这几个程序需要注销后才能生效

(2) 比赛平台的安装

下载包server monitor logger

网址：[http://sourceforge.net/projects/sserver/](http://sourceforge.net/projects/sserver/)

网址内有各种版本的包，应根据实际情况进行选择，同时每个版本的发行日志应该下载阅读。同时还有其他的工具，如观看录像工具。<!-- more -->

（3）前期安装（注：10.04和9.10在一些软件包上可能有所改动，请注意10.04和9.10所安装软件包的不同之处）

在终端中输入以下命令

[code language="bash"]sudo apt-get install build-essential //编译器安装
sudo apt-get install xorg-dev  //xorg图形界面
sudo apt-get install flex bison //词法分析器生成器 语法分析器
sudo apt-get install libboost-dev libboost-all-dev//安装boost库 10.04增加了libboost-all-dev
sudo apt-get install libqt4-dev libqt4-gui qt4-dev-tools qt4-doc qt4-designer qt4-qtconfig //qt4的应用程序
sudo apt-get install libglpng libglpng-dev//ubuntu10.04默认没有装这个
sudo apt-get install libglib2.0-dev //ubuntu10.04默认也没装glibc库
           [/code]

（4）前期准备完毕后

解压相应的rcssserver rcssmonitor文件夹，在文件夹右键单击在终端中打开。依次输入下面命令

[code language="bash"]sudo ./configure //配置库等一系列东西
sudo make
sudo make install //必须root装
sudo ldconfig //修改软件数据库 缓存
[/code]

注：在make的过程中可能提示/usr/bin/ld 错误。是因为/usr/lib下的共享库文件无法使用造成的，利用find .  -name “strings” 大概查找需要的文件，然后做个软链接sudo ln -s example1.so.1 example1.so.

比如说make时提示找不到laudio之类的词语,那就是laudio的库无法使用,此时,切换到/usr/lib文件夹下 ,用命令find . -name "libaudio*"  (在所有文件名中查找包含libaudio的) 然后做软链接sudo ln -s libaudio.so.2 libaudio.so

具体的：

切换到/usr/lib文件夹下

[code language="bash"]
sudo ln -s libgthread-2.0.so.0 libgthread-2.0.so
sudo ln -s libgobject-2.0.so.0 libgobject-2.0.so
sudo ln -s libaudio.so.2 libaudio.so
[/code]

还有就是在安装soccerwindows的时候在./configure 的时候加选项--disable-qt3（现在都是qt4了）

对于有的rcssmonitor跑起来后没有队员的情况，可以卸载掉网络管理器，我个人认为这两者有冲突。

(5)另一种安装方法

进入系统/系统管理/软件源，在软件源对话框中切换到第三方软件页面，点击添加：

[code language="bash"]deb http://ppa.launchpad.net/gnurubuntu/rubuntu/ubuntu lucid main
deb-src http://ppa.launchpad.net/gnurubuntu/rubuntu/ubuntu lucid main
[/code]

安装Server：

[code language="bash"]sudo apt-get update
sudo apt-get install rcssserver rcsslogplayer
[/code]
参考网址：

[https://launchpad.net/~rm1232002/+archive/rcss+lucid](https://launchpad.net/~rm1232002/+archive/rcss+lucid)

根据作者的描述来看，在10.04上作者还没有完成打包。哈哈，等我闲下来自己打个包，^ ^

PS：有的安装步骤需要权限，请加sudo

情况可能有所变化，但万变不离其宗。。。

比赛平台的配置与安装的ubuntu操作系统有关，有的库和软件装时本身已安装。建议用DVD安装ubuntu。或者安装完毕后以DVD作为一个更新的数据源。为了方便系统重装和实现离线升级，把第一次在/var/cache/apt/archives的deb包找到并复制保存，待以后使用
