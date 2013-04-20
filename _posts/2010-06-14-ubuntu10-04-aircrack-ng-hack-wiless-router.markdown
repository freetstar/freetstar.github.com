---
author: admin
comments: true
date: 2010-06-14 03:06:56
layout: post
slug: ubuntu10-04-aircrack-ng-hack-wiless-router
title: ubuntu10.04 下使用Aircrack-ng破解无线路由AP密码
wordpress_id: 617
categories:
- ubuntu
- 问题解决
---

	一:工具介绍

	 无线路由破解工具 Aircrack-ng ，官方网站_[http://www.aircrack-ng](http://www.aircrack-ng/)[ .org](http://www.aircrack-ng .org)_

> 
	
> 
> 
		 Aircrack-ng工具包有很多工具，工具主要有以下几个：
	
> 
> 
	
> 
> 
		 airmon-ng 处理网卡工作模式  

		 airodump-ng 抓包  

		 aircrack-ng 破解  

		 aireplay-ng 发包，干扰  
	
> 
> 

	 每个工具的具体参数选项就不一一介绍了,详情请参考原作者:[here](http://blog.csdn.net/MHY_MHY/archive/2008/11/07/3244543.aspx)

	 其他必须的linux命令

> 
	
> 
> 
		 ifconfig 查看网卡状态及参数
	
> 
> 
	
> 
> 
		 macchanger 伪造 MAC  

		 iwconfig 主要针对无线网卡的工具 (同 ifconfig)  

		 iwlist 获取无线网络的更详细信息
	
> 
> 

	二: 前期准备

	 安装工具包: 

	 sudo apt-get install aircrack-ng

	 确保自己的无线网卡已经打开

	 ifconfig 显示无线网卡的MAC地址,记下以便日后使用

	三:大致步骤描述

	 1. 修改无线网卡状态：先 down 掉

	 2. 伪造无线网卡的 MAC 地址：安全起见，减少被抓到的可能

	 3. 修改网卡工作模式：进入Monitor状态，会产生一个虚拟的网卡

	 4. 修改无线网卡状态： up

	 5. 查看网络状态，记录下 AP 的 MAC 和本机的 MAC ，确定攻击目标

	 6. 监听抓包：生成 .cap 或 .ivs

	 7. 干扰无线网络：截取无线数据包，发送垃圾数据包，用来获得更多的有效数据包

	 8. 破解 .cap 或 .ivs ，获得 WEP 密码，完成破解

	 改变MAC地址请参考:[here](http://www.path8.net/tn/archives/40)

	四:具体实践操作

	 1将无线网卡down掉

> 
	
> 
> 
		 sudo ifconfig wlan0 down 
	
> 
> 

	 2 鉴于是实验,也就是折腾,不打算很邪恶,就没有做三.2这一步,这样以来第一步没有多大必要

	 3启动无线 网卡 的监控模式

> 
	
> 
> 
		 sudo airmon-ng start wlan0 
	
> 
> 

	 4查看采用wep 加密的在线AP,ctrl+c退出,保留此终端

> 
	
> 
> 
		 sudo airodump-ng mon0 
	
> 
> 

	 5 打开另一个终端,输入以下命令.c后面的6为AP工作频道,替换为要破解的AP相应的工作频道即可.--bissid后面的AP's MAC 是要欲破解AP的MAC地址,也做相应替换,-w后的wep的是抓下来的数据包DATA 保存的文件名(可以随便取名)，然后回车开始抓包

> 
	
> 
> 
		 sudo airodump-ng -c 6 --bssid AP's MAC -w wep mon0 
	
> 
> 

	 6 再另开一个终端，输入以下命令.ESSID替换为要破解的AP相应的ESSID,AP's MAC也做相应的替换,My MAC是自己的无线网卡的地址.此步骤用来AP建立虚拟连接.

> 
	
> 
> 
		 sudo aireplay-ng -1 0 -e ESSID -a AP's MAC -h My MAC mon0
	
> 
> 

	 7 再打开一个终端,输入以下命令.在6步骤建立虚拟连接成功后,进行注入.同理AP's MAC和My MAC也应该做相应的替换.现在步骤3中数据包应该不断增长。

> 
	
> 
> 
		 sudo aireplay-ng -2 -F -p 0841 -c ff:ff:ff:ff:ff:ff -b AP's MAC -h My MAC mon0
	
> 
> 

	 8收集有5000个以上的DATA之后,另开一个终端 ,输入以下命令.进行解密(如果没算出来的话，继续等，Ubuntu aircrack-ng会在DATA每增加多5000个之后就自动再运行 ，直到算出密码为至)

> 
	
> 
> 
		 sudo aircrack-ng wep*.cap
	
> 
> 

	 9 如果没有出现意外，你应该会很高兴的看到KEY FOUND!破解出密码后在终端中输入 sudo airmon-ng stop mon0 关闭监控模式，不然无线网卡会一直向刚刚的AP进行注入的，用ctrl+c退出或者直接关闭终端都是不行的，除非重新启动电脑。

	 参考帖子: [http://hi.baidu.com/jasey_wang/blog/item/a48a4bb6b3322df931add1cc.html](http://hi.baidu.com/jasey_wang/blog/item/a48a4bb6b3322df931add1cc.html)

	 原帖:[http://blog.csdn.net/MHY_MHY/archive/2008/11/07/3244543.aspx](http://blog.csdn.net/MHY_MHY/archive/2008/11/07/3244543.aspx) 

	引用请注明作者和来源,鄙视抄袭冒充。本文原创（技术说明文档由本人参照英文原文翻译）,作者:MHY_MHY, email:mayc66@gmail.com,欢迎指出错误.最初发表在 [http://blog.csdn.net/mhy_mhy](http://blog.csdn.net/mhy_mhy) ,最后修改17:00 2008/11/6。

抄袭冒充。本文原创（技术说明文档由本人参照英文原文翻译）,作者:MHY_MHY, email:mayc66@gmail.com,欢迎指出错误.最初发表在 [http://blog.csdn.net/mhy_mhy](http://blog.csdn.net/mhy_mhy) ,最后修改17:00 2008/11/6。

