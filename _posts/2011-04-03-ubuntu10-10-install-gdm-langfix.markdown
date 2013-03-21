---
comments: true
date: 2011-04-03 14:14:36
layout: post
slug: ubuntu10-10-install-gdm-langfix
title: ubuntu10.10更新后local报错
wordpress_id: 1658
categories:
- 问题解决
---

在4月1号左右更新的系统，更新完之后gnome-terminal直接乱码。当时是





在install的最后阶段，报类似下面的错误





> perl: warning: Please check that your locale settings: LC_ALL = (unset), LC__FASTMSG = "true", LC_MESSAGES = "", LANG = "zh_CN" are supported and installed





用locale命令查看时发现报下面的错误





然后各种LC_*混乱，直接就悲剧了





> locale: Cannot set LC_CTYPE to default locale: No such file or directory  

locale: Cannot set LC_MESSAGES to default locale: No such file or directory  

locale: Cannot set LC_ALL to default locale: No such file or directory





当时想是不是locale设置出问题了，参照了半天这个帖子也没成功：[http://www.linuxdiyf.com/bbs/thread-74373-1-1.html](http://www.linuxdiyf.com/bbs/thread-74373-1-1.html)





最后在ubuntu中文论坛上看到了有类似的帖子：[http://forum.ubuntu.org.cn/viewtopic.php?f=8&t=323600](http://forum.ubuntu.org.cn/viewtopic.php?f=8&t=323600)





其中lz提示了一个解决办法：[http://forum.ubuntu.org.cn/viewtopic.php?f=8&t=323798&p=2257250#p2257250](http://forum.ubuntu.org.cn/viewtopic.php?f=8&t=323798&p=2257250#p2257250)





很多人有问题，看来这是gdm的一个bug





ubuntu10.10 32位用户可以下载这个包：[http://ubuntu.srt.cn/ubuntu/pool/main/g/gdm/gdm_2.30.5-0ubuntu4.1+langfixes~maverick1_i386.deb](http://ubuntu.srt.cn/ubuntu/pool/main/g/gdm/gdm_2.30.5-0ubuntu4.1+langfixes~maverick1_i386.deb)





ubuntu10.04 32位用户可以下载这个包：[http://ubuntu.srt.cn/ubuntu/pool/main/g/gdm/gdm_2.30.2.is.2.30.0-0ubuntu5.1+langfixes~lucid1_i386.deb](http://ubuntu.srt.cn/ubuntu/pool/main/g/gdm/gdm_2.30.2.is.2.30.0-0ubuntu5.1+langfixes~lucid1_i386.deb)





地址：[http://ubuntu.srt.cn/ubuntu/pool/main/g/gdm/](http://ubuntu.srt.cn/ubuntu/pool/main/g/gdm/)





安装之后退出登录再登入即可恢复正常
