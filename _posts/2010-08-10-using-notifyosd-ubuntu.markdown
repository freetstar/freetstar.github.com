---
author: admin
comments: true
date: 2010-08-10 12:12:45
layout: post
slug: using-notifyosd-ubuntu
title: ubuntu下用NotifyOSD来提醒你终端里的工作已完成
wordpress_id: 1091
categories:
- 软件安装
---


	如果你是命令行控的话，我觉得你会非常喜欢这个工具的。






	[![](http://ss10.sinaimg.cn/bmiddle/68785cf1h8d70538f1d39&690)](http://www.freetstar.com/wp-content/uploads/2010/08/notifyosd-terminal.png)






	当你在一个终端里进行一个非常耗时的工作任务时，你还可能同时在其他终端运行着其他的任务。这样，你可能要反复查看那个终端中的工作是否已经完成，还有时候你还会忘记在那个终端中有任务在运行，这都会导致你的工作效率降低。有了NotifyOSD，一切会方便很多






	使用步骤





> 
	
> 
> 
		1 编辑你的~/.bashrc文件
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 gedit ~/.bashrc或者 vi ~/.bashrc.将下列内容添加到文件的末尾
	
> 
> 
	
>     
>     <code> alias alert_helper='history|tail -n1|sed -e "s/^\s*[0-9]\+\s*//" -e "s/;\s*alert$//"'
>      alias alert='notify-send -i /usr/share/icons/gnome/32x32/apps/gnome-terminal.png "[$?] $(alert_helper)"'</code>
> 
> 
	
> 
> 
		 （本质用的notify-send 工具，这一步只是设置别名，提示图标等）
	
> 
> 





> 
	
> 
> 
		2 安装linotify-bin （ubuntu10.04默认安装）` `
	
> 
> 
	
> 
> 
		` sudo apt-get install libnotify-bin `
	
> 
> 





> 
	
> 
> 
		`3 source .bashrc 文件 `
	
> 
> 
	
> 
> 
		` source ~/.bashrc  

		`
	
> 
> 





> 
	
> 
> 
		`4 使用方法：在终端的命令之后输入";alert`"
	
> 
> 
	
> 
> 
		 e.g.
	
> 
> 
	
> 
> 
		 sleep 5;alert
	
> 
> 






	 






	注意：你可以在~/，bashrc文件中，改变提示图标等提示消息。具体设置可以看notify-send的man手册






	VIA{[Web Upd8](http://www.webupd8.org/2010/07/get-notified-when-job-you-run-in.html)}






	` `




