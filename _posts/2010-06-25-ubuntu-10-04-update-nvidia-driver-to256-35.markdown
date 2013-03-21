---
comments: true
date: 2010-06-25 02:37:57
layout: post
slug: ubuntu-10-04-update-nvidia-driver-to256-35
title: ubuntu 10.04 Nvidia显卡驱动升级到256.35记
wordpress_id: 779
categories:
- ubuntu
- 软件安装
---


	


		NVIDIA 256系列Linux驱动首款正式版出炉
	


	


		[http://www.enet.com.cn/article/2010/0624/A20100624674525.shtml](http://www.enet.com.cn/article/2010/0624/A20100624674525.shtml)
	


	


		NVIDIA 256系列Linux驱动发布重点，产品支持列表，其他信息[  

		http://www.nvidia.cn/object/linux-display-ia32-256.35-driver-cn.html](http://www.nvidia.cn/object/linux-display-ia32-256.35-driver-cn.html)  

		总体而言，对市面上大众型的显卡对是支持的
	


	


		NVIDIA 256系列Linux驱动32位下载  

		
	


	


		[http://www.nvidia.cn/object/linux-display-ia32-256.35-driver-cn.html](http://www.nvidia.cn/object/linux-display-ia32-256.35-driver-cn.html)
	


	


		NVIDIA 256系列Linux驱动64位下载  

		[http://www.nvidia.cn/object/linux-display-amd64-256.35-driver-cn.html](http://www.nvidia.cn/object/linux-display-amd64-256.35-driver-cn.html)
	


	


		  

		
	


	


		[  

		](http://www.nvidia.cn/object/linux-display-amd64-256.35-driver-cn.html)本本情况：显卡8400M GS ,缓存64mb，CPU T2330，主频1.6G  

		
	


	


		驱动情况：之前使用的是Nvidia 195系列驱动<!-- more -->  

		安装方法：  

		1.添加源
	


	


		 ubuntu 10.04和Maverick用户 
	


	


		[code langague="bash"] sudo add-apt-repository ppa:ubuntu-x-swat/x-updates[/code]
	


	


		 ubuntu Karmic, Jaunty, Intrepid and Hardy 用户
	


	


		[code langague="bash"] 
sudo sh -c "echo 'deb http://ppa.launchpad.net/nvidia-vdpau/ppa/ubuntu UBUNTU_VERSION main' >> /etc/apt/sources.list"
sudo sh -c "echo 'deb-src http://ppa.launchpad.net/nvidia-vdpau/ppa/ubuntu UBUNTU_VERSION main' >> /etc/apt/sources.list"
[/code]  

		其中UBUNTU_VERSION替代为相应的ubuntu版本即可  

		
	


	


		2 更新软件源并安装驱动
	


	


		 ubuntu 10.04和Maverick用户  

		[code langague="bash"] sudo apt-get update sudo apt-get install nvidia-current nvidia-current-modaliases nvidia-settings [/code]  

		ubuntu Karmic, Jaunty, Intrepid and Hardy 用户  

		[code langague="bash"] sudo apt-get install nvidia-glx-256 nvidia-256-modaliases nvidia-settings [/code]
	


	


		3 安装完毕后nvidia-xserver提示版本还是195,重启后提示版本为256.35
	


	


		 [![](http://www.freetstar.com/wp-content/uploads/2010/06/Screenshot4.png)](http://www.freetstar.com/wp-content/uploads/2010/06/Screenshot4.png)
	


	


		 
	


	


		PS：如果想恢复原来驱动的话，可以删除此源，重新安装驱动即可
	






