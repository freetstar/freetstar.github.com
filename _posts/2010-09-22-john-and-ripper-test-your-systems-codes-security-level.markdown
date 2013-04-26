---
author: admin
comments: true
date: 2010-09-22 08:26:17
layout: post
title: John the Ripper ---检测系统密码的安全性
wordpress_id: 1294
categories:
- 软件安装
---

介绍：

是一个专业的密码破解工具，它可以工作在Unix ,DosWinNT/Win95等平台上，这个工具的主要目的在于检测Unix平台密码的强度(相对于Windows平台，大家可以做用LC4这个软件),当然现在已经被一些非法分子在使用  

它经过了Linux x86 Linux x86/Alpha/SPARC, FreeBSD x86, OpenBSD x86, Solaris 2.x SPARC and x86, Digital UNIX, AIX, HP-UX, and IRIX平台的测试。  

其Dos版本和Win32版本采用了DJGPP与Cygnus Developer's Kit来实现(一种跨平台库)。

安装方法：

1 下载Linux平台源代码：[here](http://www.openwall.com/john/g/john-1.7.6.tar.gz)

2 解压tar zxvf filename.tar.gz，之后进入src文件内

3 输入make，查看支持的Linux系统架构

4 选择好之后，  

    make clean system //system为你选择的架构

5 然后进入run文件夹，应该会有john这位大哥在那里等待你了

使用方法：

进入run文件夹后运行
    sudo ./unshadow /etc/passwd /etc/shadow >passwdtest

然后./john passwdtest来揭秘密码，一般1分钟到1个小时内能解出来的密码是脆弱的

如果时间太长，可以Ctrl+c自己终止，也可以在原来终止的部分恢复，更多内容参数内容请参见

[http://hi.baidu.com/wjs_hd2009/blog/item/799a211e5c866301314e156d.html](http://hi.baidu.com/wjs_hd2009/blog/item/799a211e5c866301314e156d.html)

补充：  

破解字典是关键，要想使用更多的字典，请购买[http://www.openwall.com/wordlists/](http://www.openwall.com/wordlists/)

官网地址为：[http://www.openwall.com/john/](http://www.openwall.com/john/)

Youtube教程：[http://www.youtube.com/watch?v=4ZpzZsGCG9I&feature=fvw](http://www.youtube.com/watch?v=4ZpzZsGCG9I&feature=fvw)

参考资料：[http://linux.chinaunix.net/bbs/viewthread.php?tid=45977](http://linux.chinaunix.net/bbs/viewthread.php?tid=45977)

