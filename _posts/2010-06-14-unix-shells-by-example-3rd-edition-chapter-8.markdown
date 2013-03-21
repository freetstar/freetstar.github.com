---
comments: true
date: 2010-06-14 13:56:23
layout: post
slug: unix-shells-by-example-3rd-edition-chapter-8
title: unix shells by example 3rd edition chapter 8
wordpress_id: 609
categories:
- 生活
---

## 
	习题1:启动






	 1,Q:哪个进程把登录提示符打印到屏幕上






	 A:getty<!-- more -->






	 2,Q:哪个进程为HOME,LOGNAME和PATH赋值?  






	 A:/bin/login






	 3.Q:怎么才能知道自己在运行哪个shell?






	 A:echo $0






	 4,Q:在哪里(哪个文件指定你的登录shell)?






	 A:/etc/passwd文件中,相应用户的的最后一项






	 5,Q:解释/etc/profile和.profile这两个文件之间的区别.shell先执行哪一个?






	 A:前者是一个系统级的初始化文件,后者是用户定义的初始化文件.先执行前者.






	 6,Q:编辑你的.profile文件,完成一下功能.a)欢迎用户;b)如果路径不包含你的主目录,将其加入;c)用stty命令来食指退格键的擦除功能;d)键入:.profile.dot命令的功能是什么?






	 A:a)增加echo "Hi";b)怎加~;c)stty erase ^h;d)dot命令用来初始化文件,当前shell中执行这个脚本






	  

	





## 
	习题2:shell的元子符






	1.创建一个名为wildcards的目录,cd到该目录然后在命令行键入:






	 touch ab abc a1 a2 a3 all a12 ba ba.1 ba.2 filex filey Abc ABC ABc2 abc






	2.写出能实现下列功能的命令,并测试你所写的命令






	 a)列出所有名字以a开头的文件.  -------------------ls a*






	 b)列出所有名字以至少一个数字结尾的文件.-----------------ls *[0-9]






	 c)列出所有名字以a或者A开头的文件----------------ls [Aa]*






	 d)列出所有名字以句号跟一个数字结尾的文件----------ls *.[1-9]






	 e)列出所有名字中包含两个字母a的文件---------------ls *a*a*






	 f)列出所有名字由3个字母组成,且3个字母都是大写的文件---------------ls [A-Z][A-Z][A-Z]






	 g)列出所有名字以10,11或12结尾的文件--------------ls *[1][0-2]






	 h)列出所有名字以x或y结尾的文件-------------ls *[xy] 






	 i)列出所有名字以数字,大写字母或者小写字母结尾的文件--------------ls *[0-9a-zA-Z]






	 j)列出所有名字不是以a,b或者B开头的文件--------------ls [!abB]*






	 k)删除名字为两个字符,并以a或者A开头的文件------------rm [aA]?






	  

	






	附上自己写的小脚本一段.






	  

	






	


		  

		[code language="bash"] 
#!/bin/sh 
#This is a script to alarm me that it is time to have a nive sleep 
#It will play music by alarm me and shut down the screen 
#hope it will work! 
set `date +%-H%M` 
if [ $1 -gt 0200 ] 
then 
{ echo Baby,its time to have a nice sleep\n;
   xset dpms force off ; 
  mplayer /home/lgx/音乐/westlife/Season\ In\ The\ Sun.mp3;
 }
 fi 
exit [/code]
	


	


		  

		
	


	


		这几天晚上睡得比较完,恰好正在学习脚本,于是写个小脚本提醒自己吧.
	


	


		到了晚上两点之后,关闭screen,放点音乐.
	


	


		初写脚本,定有很多考虑不周的地方,大家多提意见.
	






