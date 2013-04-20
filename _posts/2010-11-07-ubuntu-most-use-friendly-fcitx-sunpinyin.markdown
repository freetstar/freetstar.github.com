---
author: admin
comments: true
date: 2010-11-07 20:41:01
layout: post
slug: ubuntu-most-use-friendly-fcitx-sunpinyin
title: ubuntu下最好用的输入法fcitx-sunpinyin
wordpress_id: 1427
categories:
- 软件安装
---

	今天难得折腾一会儿输入法，对于系统美化方面的东西我比较模糊，神马字体渲染阿，输入法模糊音阿对我来说统统比较模糊。隐约记得是@Houge_Langley在大力推上推荐这款输入法。

	fcitx：

	Free Chiese Input Toy for X 是一个以[ GPL](http://www.gnu.org/copyleft/gpl.html)方式发布的、基于XIM的简体中文输入法(即原来的G五笔)，拼音（全拼和双拼），包括区位以及码表输入模块，是在Linux操作系统中使用的中文输入法（引自fcitx官网：[http://www.fcitx.org/main/](http://www.fcitx.org/main/)）

	sunpinyin：

	是建立在中文输入上的静态语言模型。支持多种输入平台和多款操作系统，比如说ibus，fcitx的XIM，Mac OS X。项目主页：[http://code.google.com/p/sunpinyin/](http://code.google.com/p/sunpinyin/)

	fcitx具体的安装方法：

	第一步：安装fcitx

	//如果系统以前装过fcitx，请先删除fcitx，然后找出配置文件删除

	删除配置文件：  

		sudo find ~ -name fcitx -ok rm -rf {} \;

		sudo add-apt-repository ppa:wengxt/fcitx-nightly

		sudo apt-get update

		sudo apt-get install  fcitx  

		第二步：移除其他输入法或者将fcitx定为首选输入法
    
    	移除ibus：sudo apt-get autoremove ibus
    移除scim：sudo apt-get autoremove scim

	或者切换系统首选输入法：

	方法1:系统-首选项-语言支持中修改开机启动的默认输入法

	方法2:用im-switch更改：im-switch -s fcitx -z default

	第三步：安装sun-pinyin 
    
    	sudo apt-get install fcitx-sunpinyin

	第四步：安装fcitx的Gtk配置界面 
    
    	sudo apt-get install fcitx-config

	第五步：给fcitx-sunpinyin添加词库 

	词库1

	下载hubert_star为sunpinyin制作的2套搜狗词库

	精简：[http://hslinuxextra.googlecode.com/files/sunpinyin-userdict.7z](http://hslinuxextra.googlecode.com/files/sunpinyin-userdict.7z)

	全套：[http://hslinuxextra.googlecode.com/f...rdict-small.7z](http://hslinuxextra.googlecode.com/f...rdict-small.7z)

	将解压出来的userdict文件放到~/.sunpinyin文件夹下，如果此文件夹不存在
    
    	mkdir -p /home/`whoami`/.sunpinyin

	词库2

	按照nenew的方法，进行添加。具体方法见下：

	[http://www.nenew.net/fcitx-sunpinyin.html](http://www.nenew.net/fcitx-sunpinyin.html)

	第六步：添加开机启动

	打开系统-应用程序-启动应用程序中添加fcitx的开机启动

	名称：fcitx（随便）

	命令：fcitx -d

	参考和感谢：

	nenew：[http://www.nenew.net/fcitx4-0beta1r463.html](http://www.nenew.net/fcitx4-0beta1r463.html)

	[http://www.nenew.net/fcitx-sunpinyin.html](http://www.nenew.net/fcitx-sunpinyin.html)

	huber_star:[http://www.linuxsir.org/bbs/thread372879.html](http://www.linuxsir.org/bbs/thread372879.html)

