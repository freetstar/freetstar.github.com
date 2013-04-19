---
author: admin
comments: true
date: 2010-06-22 19:46:53
layout: post
slug: burg-make-ur-ubuntu-bootloader
title: 用burg来美化你的ubuntu开机菜单
wordpress_id: 762
categories:
- 转载翻译
tags:
- burg
---


	还记得之前那个美化开机背景的日志吗？






	[http://www.freetstar.com/index.php/ubuntu-10-04-9-10grub2-splash-picure](http://www.freetstar.com/index.php/ubuntu-10-04-9-10grub2-splash-picure)






	现在我们burg用来美化的你开机启动菜单，下面我来一步步介绍她的使用方法





> 
	
> 
> 
		打开终端：输入以下命令  

		 sudo add-apt-repository ppa:bean123ch/burg   

		
	
> 
> 
	
> 
> 
		sudo apt-get update   

		
	
> 
> 
	
> 
> 
		sudo apt-get install burg burg-themes  

		  

		
	
> 
> 
	
> 
> 
		 
	
> 
> 






	  

	






	当出现下面图案时，直接回车即可






	[![](http://www.freetstar.com/wp-content/uploads/2010/06/Screenshot3-300x215.png)](http://www.freetstar.com/wp-content/uploads/2010/06/Screenshot3.png)






	在此画面时,选择grub所在硬盘即可






	[![](http://www.freetstar.com/wp-content/uploads/2010/06/Screenshot-1-300x214.png)](http://www.freetstar.com/wp-content/uploads/2010/06/Screenshot-1.png)






	  

	  

	  

	






	重启，你的开机菜单就会很丰富了  

	  

	  

	






	[![](http://www.freetstar.com/wp-content/uploads/2010/06/Selection_015.png)](http://www.freetstar.com/wp-content/uploads/2010/06/Selection_015.png)






	想看更多的吗？在开机的时候按"t"






	[![](http://www.freetstar.com/wp-content/uploads/2010/06/Selection_017.png)](http://www.freetstar.com/wp-content/uploads/2010/06/Selection_017.png)






	选择好主题，然后重启






	[![](http://www.freetstar.com/wp-content/uploads/2010/06/Selection_016.png)](http://www.freetstar.com/wp-content/uploads/2010/06/Selection_016.png)






	想预览一下吗？在终端输入






	burg-emu






	 






	Via{[Ubuntu Explorer](http://ubuntuexplore.blogspot.com/2010/06/ubuntu-how-to-beautify-your-bootloader.html)}






	 






	几个要注意的地方：






	1:可能会导致开机Logo变模糊






	2:不知道与[http://www.freetstar.com/index.php/ubuntu-10-04-9-10grub2-splash-picure](http://www.freetstar.com/index.php/ubuntu-10-04-9-10grub2-splash-picure)里的包是否会冲突






	3:毕竟是对Grub操作，做好grub重装的准备，不过基本上没有问题






	4:删除burg的时候，因为倚赖关系会提示删除Grub2,这一步选择否就是了






	 






	  

	




