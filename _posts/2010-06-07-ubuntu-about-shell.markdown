---
author: admin
comments: true
date: 2010-06-07 23:25:53
layout: post
slug: ubuntu-about-shell
title: ubuntu 关于shell的那些事
wordpress_id: 300
categories:
- ubuntu
---

**1 用终端上IRC**

    sudo apt-get install irssi 
    irssi -c irc.ubuntu.com -p 8000 -n hiall 
    /j #ubuntu-cn

2 在终端里跑小火车

    sudo apt-get install sl

3 释放可爱的小鱼

    Alt+F2

    free the fish

4  古怪的日

     ddate

5 跑晕你不偿

     yes > /dev/null 

6 安装女朋友（纯属恶搞;))

     sudo apt-get install girlfriend
    正在读取软件包列表... 完成   
    正在分析软件包的依赖关系树... 完成  
    有一些软件包无法被安装。  
    下列的信息可能会对解决问题有所帮助：  
    下列的软件包有不能满足的依赖关系：  
    girlfriend: 依赖: house但是它将不会被安装  
    girlfriend: 依赖: car但是它将不会被安装  
    house,car: 依赖: money但是它将不会被安装   
    E: 无法安装的软件包

7 每天的财富

     sudo apt-get install fortune

8 打印月份

     cal 6 2010

9 水汪汪的大眼镜

    xeyes

10 天翻地覆  把文件行反过来输出

    tac  filename

11 老牛

    aptitude moo

12 强大的CTRL组合键（^ 代表CTRL）

    ^c，终止当前命令 
    ^z  ,停止当前的命令。用fg放到前台或者用bg放到后台
    ^d，退出
    ^w，删除当前行的一个单词
    ^u , 删除当前行的所有单词
    ^r, 得出最近使用的命令
    ^a, 移动到命令行最前

13 重复执行

> ！！重复执行上一次执行过的命令 

14 文件带行号输出

> nl filename

15 关掉显示器

> 桌面单击右键，创建启动器

命令部分填 xset dpms force off

16 删除回收站垃圾

> rm -rf ~/.Trash/*

17 嘿嘿，搞坏你的硬盘

> dd if=/dev/random of=/dev/sda

17 改变标题栏按钮的位置

> gconftool-2 --set /apps/metacity/general/button_layout --type string "maximize,minimize,close:menu"

未完待续，不断更新中。。。

