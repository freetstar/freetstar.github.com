---
author: admin
comments: true
date: 2010-07-18 13:25:52
layout: post
title: Ubuntu10.04 从源中安装Robocup2D的rcssserver rcsslogplayer
wordpress_id: 991
categories:
- ubuntu
- 问题解决
---

添加软件源：

    deb http://ppa.launchpad.net/gnurubuntu/rubuntu/ubuntu lucid main  

    deb-src http://ppa.launchpad.net/gnurubuntu/rubuntu/ubuntu lucid main  

然后运行

    sudo apt-get update  

    sudo apt-get install rcssserver rcsslogplayer

这是之前的那篇文章ubuntu10.04配置比赛环境的文章[http://www.freetstar.com/ubuntu10-04-robocup2d-platform](http://www.freetstar.com/ubuntu10-04-robocup2d-platform)

本人没有亲自尝试此方法，故rcssserver和rcsslogplayer的版本不祥。。。其实一直觉得亲自从源代码编译安装软件是最好的

