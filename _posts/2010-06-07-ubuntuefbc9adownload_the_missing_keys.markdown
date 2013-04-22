---
author: admin
comments: true
date: 2010-06-07 01:58:29
layout: post
slug: ubuntu%ef%bc%9adownload_the_missing_keys
title: ubuntu：下载丢失的GPG 密钥
wordpress_id: 293
categories:
- ubuntu
- 问题解决
---

本教程旨在于讲授如何在软件源中下载和增加gpg认证密钥。教程是很简单和容易

从以下链接下载和安装：

    ubuntu 10.04 [Launchpad-getkeys](http://www.4shared.com/file/t2dU9g7Q/launchpad-getkeys_01lucid3_all.html)

    ubuntu 9.10  [Launchpad-getkeys](http://www.4shared.com/file/chXMssjG/launchpad-getkeys_01karmic_all.html) 

运行以下命令 

    sudo launchpad-getkeys

现在所有丢失的认证密钥都已经安装好了。你可以到系统-系统管理-软件源-身份认证中查看

翻译：[FreeTstar](http://www.freetstar.tcom)

via{[Ubuntu Explorer](http://ubuntuexplore.blogspot.com/2010/05/ubuntu-how-to-download-missing-gpg-key.html)}

 安装一些软件或者进行更新的时候，会提示无法从服务器获得pgp认证密钥，可以通过以上方法解决，也可以换一个源试下

 一种解决思路：{[ubuntu中文论坛](http://forum.ubuntu.org.cn/viewtopic.php?f=77&t=182819)}2l的解决办法

   gpg --keyserver subkeys.pgp.net --recv ********  

   导入密匙：  

   gpg --export --armor ******** | sudo apt-key add -  

   注： * 号是指密匙的后八位

