---
comments: true
date: 2010-08-29 09:51:49
layout: post
slug: psensor-a-graghical-temperature-monitor
title: psensor  一款图形化的温度显示器
wordpress_id: 1198
categories:
- 软件安装
---


	 ![](http://www.ubuntugeek.com/wp-content/uploads/2010/08/psensor-last.png)






	Psensor 能够自动检测出大部分硬件的温度，并且温度变化会自动显示，窗口大小可随意改变






	设计初衷：简单易用，避免复杂的设置，而且对CPU和内存消耗少






	安装方法：（限于9.10/10.04 ）<!-- more -->






	 1 安装必要的包






	 sudo apt-get install lm-sensors make gcc libsensors4-dev libgtk2.0-dev libgconf2-dev






	 2 打开硬件温度检测






	 sudo sensors-detect






	 3 下载Psensor 源码






	[ here](http://wpitchoune.net/psensor/files/psensor-0.3.2-src.tar.gz)






	 4 正式安装






	 tar xvzf psensor-0.3.2-src.tar.gz






	 cd psensor-0.3.2






	 可选项：编辑Makefile文件，修改PSENSOR_DIR的安装路径






	 make clean all






	 sudo make install 






	 然后输入psensor即可






	 更多选项可以参考源码包中的README






	via{[here](http://www.ubuntugeek.com/psensor-a-graphical-temperature-monitor.html)}




