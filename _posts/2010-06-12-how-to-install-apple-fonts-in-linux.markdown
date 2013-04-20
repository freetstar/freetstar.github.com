---
author: admin
comments: true
date: 2010-06-12 14:53:54
layout: post
slug: how-to-install-apple-fonts-in-linux
title: linux 中安装Mac OSX的字体
wordpress_id: 570
categories:
- 转载翻译
tags:
- font
---

			` ``这些MAC OSX字体包括了:AppleGaramond, Aquabase, Lithgrl, Lucida Grande and Lucida MAC`

			`你可以从这里下载[HERE](http://code.google.com/p/ubuntu-debs/downloads/detail?name=macfonts.tar.gz&can=2&q=),或者运行下面命令来下载和安装这些字体  

			`

			[code language="bash"] 
cd wget http://ubuntu-debs.googlecode.com/files/macfonts.tar.gz 
tar zxvf macfonts.tar.gz 
sudo cp -r macfonts/ /usr/share/fonts 
sudo fc-cache -f -v [/code]

			`下面是一些字体截屏`

			` ![](http://lh6.ggpht.com/_1QSDkzYY2vc/TBJ9hIGHWxI/AAAAAAAABPQ/1GqbDINLA-0/s288/AppleGaramond.ttf_001.png) `

			` ![](http://lh3.ggpht.com/_1QSDkzYY2vc/TBJ9hSE_I5I/AAAAAAAABPU/ldsQcHZMpfE/s288/Lucida%20Grande.ttf_002.png)`

			`  

			`

			`翻译:[FreeTstar](http://www.freetstar.com)`

			`VIA{[http://www.webupd8.org/2010/06/how-to-install-apple-mac-osx-fonts-in.html](http://www.webupd8.org/2010/06/how-to-install-apple-mac-osx-fonts-in.html)}`

sx-fonts-in.html](http://www.webupd8.org/2010/06/how-to-install-apple-mac-osx-fonts-in.html)}`

