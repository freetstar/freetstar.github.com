---
comments: true
date: 2010-10-07 19:20:19
layout: post
slug: introduce-2-linux-cli-tricks-books-and-books-aboutlinux-cli
title: 介绍几个Linux CLI tricks和2本命令行技巧书
wordpress_id: 1317
categories:
- PROGRAM
---


	 接触了Linux以后，越发发现linux CLI的强大和有趣，Linux下常用命令的高效，也比较关注命令行的一些东西，读了点O'REILLY一些有名的著作






	《sed & awk》 《bash》 等，讲得大多都比较系统，清晰。而最近也读了点篇幅较小，但是关于CLI的比较有趣的文章，首先介绍几个"聪明"的命令






	1 用TELNET看《星球大战》






	 telnet [towel.blinkenlights.nl<!-- more -->](http://towel.blinkenlights.nl)






	没什么好解释的，就是ASCII艺术之一。如果你有ipv6连接，还能看到彩色版的。牛吧？






	2 查看ASCII码表






	 man 7 ascii






	 很多人初学编程都会接触到ascii码的概念，有时候为了查某个符号的ascii值，可能还得






	翻箱倒柜找出当年的课本？Linux Manpage里面其实包含了很多类似的实用资料，上述命






	令就能很详细的方式解释ascii编码，当然这里还有在线版。






	3 远程传送麦克风语音






	 dd if=/dev/dsp | ssh username@host dd of=/dev/dsp






	 没错就是实现一个喊话器的功能。






	/dev/dsp是Linux下声卡的文件映射（Digital Signal Proccessor），从其中读数据就是录






	音，往里面写数据就是播放，相当简单！






	其中username和host分别填用户名和主机名






	PS：cat /dev/urandom | aplay  //我感觉此方法可以用来夏季驱蚊，不信，你试试^_^






	4 抓取LINUX桌面的视频






	 ffmpeg -f x11grab -s wxga -r 25 -i :0.0 -sameq /tmp/out.mpg






	我们在一些视频网站上看到别人的3D桌面怎么怎么酷的视频，通常就是这么来的，






	ffmpeg可以直接解码X11的图形，并转换到相应输出格式。






	5 使用cd和alias命令快速返回上级目录






	$alias cd1="cd .."  

	$alias cd2="cd ../.."  

	$alias cd3="cd ../../.."  

	$alias cd4="cd ../../../.."  

	$alias cd5="cd ../../../../.."






	6 用"cd -"来在最近访问的2个目录之间切换






	如下:  

	$ cd /tmp/very/long/directory/structure/that/is/too/deep  

	$ cd /tmp/subdir1/subdir2/subdir3  

	$ cd -  

	$ pwd  

	/tmp/very/long/directory/structure/that/is/too/deep






	大家看了几个之后，是不是感到命令行的强大了。






	这些东西都不是出自我手，前4个命令是来自[WOW！Ubuntu](http://wowubuntu.com/linux-shell-pdf.html)两位大哥的辛勤工作，外文的翻译和整理，同时提供了pdf下载，地址：[51CTO](http://down.51cto.com/data/127587) / [UUShare](http://www.uushare.com/user/rikulu/file/3499500)






	后两个来自亲爱的[Jasey_Wang](http://jaseywang.info/2010/09/16/linux-101-hacks%E7%AC%94%E8%AE%B0%E4%B8%80/)同学对于《Linux 101 Hacks》的读后感，《Linux 101 Hacks》下载：[英文原版](http://db.tt/MIjb25x)/[中文版](http://db.tt/XxPblfU)






	其实文章比较水，目的主要是推广下这两本好书吧。




