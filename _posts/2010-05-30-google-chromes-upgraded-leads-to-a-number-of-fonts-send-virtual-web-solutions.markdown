---
author: admin
comments: true
date: 2010-05-30 17:28:54
layout: post
slug: google-chromes-upgraded-leads-to-a-number-of-fonts-send-virtual-web-solutions
title: Google Chrome 升级之后字体发虚问题解决办法
wordpress_id: 183
categories:
- ubuntu
tags:
- chrome
- 字体发虚
---

	以[http://www.baidu.com/](http://www.baidu.com/) 和[http://www.cnbeta.com/](http://www.cnbeta.com/) 为试验品进行实验，同时每次实验后恢复初始状态。

> 
	实验1: 安装Webpage Decorator插件，地址： [https://chrome.google.com/extensions/detail/idmfdjpebmchkoghokmjmgbeejhfjncc?hl=zh-cn](https://chrome.google.com/extensions/detail/idmfdjpebmchkoghokmjmgbeejhfjncc?hl=zh-cn) 

> 
	安装好之后会在地址栏有图标提示[![](http://www.freetstar.com/wp-content/uploads/2010/05/Screenshot-1.png)](http://www.freetstar.com/wp-content/uploads/2010/05/Screenshot-1.png)，点击图标按钮可以调整网页的字体。 [http://www.baidu.com/](http://www.baidu.com/) 调整字体大小到16时字体发虚现象基本解决， [http://www.cnbeta.com/](http://www.cnbeta.com/) 调整字体大小到16时字体发虚现象基本解决.

> 
	总结：整体不错，但需要每次都对网页调整，而且比较麻烦，还给人感觉网页布局不是和谐- - ！

> 
	
> 
> 
		实验2:
	
> 
> 
	安装chrome stylist插件，地址： [https://chrome.google.com/extensions/detail/pabfempgigicdjjlccdgnbmeggkbjdhd?hl=zh-cn](https://chrome.google.com/extensions/detail/pabfempgigicdjjlccdgnbmeggkbjdhd?hl=zh-cn) 

> 
	安装好之后，打开插件的options，再打开style标签，点击LDR Simple，对All sites 挑上沟，把里面的字体改一下，保存重启或刷新。 我是把.item_title { font-size: 18px !important; }中的18px，改成 16px的 补充：发现上人人时左侧显示字体过大，故将LDR Simple中的.item{}的30px改成16px，刷新后显示正常 [http://www.baidu.com/](http://www.baidu.com/) 完美，字体不发虚 [http://www.cnbeta.com/](http://www.cnbeta.com/) 完美，字体不发虚，而且整体页面给人感觉很好

> 
	总结：比较完美的解决办法，强力推荐！！！

> 
	实验3: 

> 
	运行命令﻿ sudo gedit /etc/fonts/conf.d/66-wqy-zenhei-sharp.conf 把<test compare="more_eq" name="pixelsize"><double>12</double></test>中的12改为16 [http://www.baidu.com/](http://www.baidu.com/) 网页字体仍然发虚中 [http://www.cnbeta.com/](http://www.cnbeta.com/) 同上

> 
	总结：貌似不ok！

> 
	实验4: 打开Chrome的选项，高级选项，更改字体和语言设置： 将所有字体大小改成统一16（也可是其他） ﻿﻿ [http://www.baidu.com/](http://www.baidu.com/) 网页字体发虚情况明显减少 [http://www.cnbeta.com/](http://www.cnbeta.com/) 网页字体仍然发虚中 

> 
	总结：貌似不ok！

> 
	﻿实验5: 安装**Change Font Family Style Extension插件** 奇怪 ，这个插件怎么没有选项。。。直接使用，得出一下结论 [http://www.baidu.com/](http://www.baidu.com/) 网页字体发虚 [http://www.cnbeta.com/](http://www.cnbeta.com/) 网页字体仍然发虚 

> 
	总结：貌似不ok！

> 
	大总结：根据此帖 [http://bbs.chromi.org/thread-6197-1-1.html](http://bbs.chromi.org/thread-6197-1-1.html)来看，是chrome没办法对网页字体进行转换，导致字体发虚。个人观点，上边的几个实验或者是用插件进行强制转换，或者是来更改字体显示（^ ^不太懂，有矩阵，点阵之类的，我研究还不太深入），来实现字体转换的。有兴趣的ggmm们可以参照[http://bbs.chromi.org/thread-6197-1-1.html](http://bbs.chromi.org/thread-6197-1-1.html)此帖来解决字体发虚问题，本人还没亲自实验。 综上所述：推荐使用第二种方法！
	
  * 
		参考帖：
	
  * 
		[http://forum.ubuntu.org.cn/viewtopic.php?f=73&t=275305](http://forum.ubuntu.org.cn/viewtopic.php?f=73&t=275305) 看1楼
	
  * 
		[http://forum.ubuntu.org.cn/viewtopic.php?f=73&t=275594](http://forum.ubuntu.org.cn/viewtopic.php?f=73&t=275594) 看11楼加菲猫兄
	
  * 
		**[http://forum.ubuntu.org.cn/viewtopic.php?f=8&t=267006 ](http://forum.ubuntu.org.cn/viewtopic.php?f=8&t=267006 ) 看8楼**

	如果有其他方法，请留言，我会做进一步实验和总结

	如果有其他方法，请留言，我会做进一步实验和总结

