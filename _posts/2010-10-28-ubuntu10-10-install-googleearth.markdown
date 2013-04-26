---
author: admin
comments: true
date: 2010-10-28 22:48:46
layout: post
title: ubuntu10.10下安装googleearth
wordpress_id: 1376
categories:
- 转载翻译
---

注:若操作系统是64位的用户,运行命令安装依赖sudo apt-get install ia32-libs lib32nss-mdns

第一步:从ubuntu的官方源中安装googleearth-package这个包

    sudo apt-get install googleearth-package

第二步:运行

    make-googleearth-package --force

来产生deb包(可能比较耗时)

第三步:安装

    sudo dpkg -i googleearth_5.2.1.1588+0.5.7-1_i386.deb 

第四步:打开googleearth

依次打开应用程序-互联网-Google Earth

via{[here](http://ubuntuguide.net/how-to-install-google-earth-in-ubuntu-10-10-maverick)}

