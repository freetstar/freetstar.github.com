---
author: admin
comments: true
date: 2011-02-28 13:37:17
layout: post
title: 升级至wordpress3.1出错后退回来
wordpress_id: 1621
categories:
- 问题解决
---

2月24号在家手动升级了一下wordpress，打算升级到3.1.0，提示升级出错，

[Thu Feb 24 06:38:13 2011] [warn] [client 123.73.94.175] mod_fcgid: stderr: PHP Warning:  copy(/var/www/wp-includes/images/smilies/icon_twisted.gif): failed to open stream: Permission denied in /var/www/wp-admin/includes/class-wp-filesystem-direct.php on line 200, referer: http://www.freetstar.com/wp-admin/update-core.php

在24号晚上maplebeats在fb说我博客出问题了，一直没咋在意，以为vps抽风了，直到25号晚上坐车回天津在车上有朋友提醒访问时页面空白，在学校收拾和休息了一天后开始弄。第一步查日志

    vi /var/log/apache2/error.log

查到

[Thu Feb 24 06:38:13 2011] [warn] [client 123.73.94.175] mod_fcgid: stderr: PHP Warning:  copy(/var/www/wp-includes/images/smilies/icon_twisted.gif): failed to open stream: Permission denied in /var/www/wp-admin/includes/class-wp-filesystem-direct.php on line 200, referer: http://www.freetstar.com/wp-admin/update-core.php  

[Thu Feb 24 06:38:20 2011] [warn] [client 218.213.130.167] mod_fcgid: stderr: PHP Fatal error:  require(): Failed opening required '/var/www/wp-includes/class-wp.php' (include_path='.:/usr/share/php:/usr/share/pear') in /var/www/wp-settings.php on line 68

然后date查看server的时间，又去看了下监控宝报错的时间，查了一下时间差，发现确实在server的06点报php报错时不能访问，于是判断为php方面的错误，然后自己根据提示touch class-wp.php，然后又报

[Sun Feb 27 04:50:55 2011] [warn] [client 69.63.180.248] mod_fcgid:  stderr: PHP Fatal error:  Call to undefined method  stdClass::get_results() in /var/www/wp-includes/functions.php on line  432

觉得奇怪，然后在本地下载wordpress3.0.5和wordpress3.1的源码包，发现确实目录和文件存在不一样，3.1新增几个文件。然后逐一删除/var/www/下的一些php文件，也就时wordpress升级不成功导致新增的3.1的php文件，然后在服务器上下载3.0.5的源码包，tar解压缩，将其cp过去//////也就是恢复3.0.5的目录结构和php文件，但保留自己的插件配置等几个目录

然后查看日志信息，再没有报错，博客终于回来了，一定要做好备份啊！

