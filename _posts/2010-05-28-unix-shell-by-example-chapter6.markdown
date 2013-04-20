---
author: admin
comments: true
date: 2010-05-28 00:00:20
layout: post
slug: unix-shell-by-example-chapter6
title: unix shell范例精解第六章课后习题
wordpress_id: 96
categories:
- PROGRAM
tags:
- shell
- unix
---


	


		


			Mike Harrington:(510) 548-1278:250:100:175
		


		


			Christian Dobbins:(408) 538-2358:155:90:201
		


		


			Susan Dalsass:(206) 654-3279:250:60:50
		


		


			Archie McNichol:(206) 548-1348:250:100:175
		


		


			Jody Savage:(206) 548-1278:15:188:150
		


		


			Guy Quigley:(916) 343-6410:250:100:175
		


		


			Dan Savage:(406) 298-7744:450:300:275
		


		


			Nancy McNeil:(510) 548-5258:250:80:75
		


		


			John Goldenrod:(916) 348-4278:250:100:175
		


		


			Chet Main:(510) 548-5258:50:95:135
		


		


			Tom Savage:(408) 926-3456:250:168:200
		


		


			Elizabeth Stachelin:(916) 440-1763:175:75:300
		


	








	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额<!-- more -->注：以上内容被写进chapter6这个文档





##### 
	1.打印在第一个月捐款超过100美元的人的姓和名





##### 
        [sourcecode language="bash"]nawk -F[: ] $5 100{print $2,$1} chapter6[/sourcecode]





##### 
	2.打印在第一个月捐款少于60美元的人的姓名和电话号码





##### 
	[sourcecode language="bash"]nawk -F[: ] $5  60{print $1,$2,$4} chapter6[/sourcecode]





##### 
	3.打印第三个月捐款数额在90美元到150美元之间的人





##### 
	[sourcecode language="bash"]nawk -F[: ] $7 150  $7 90 {print $1,$2} chapter6[/sourcecode]





##### 
	4 打印这3个月的捐款总额超过800美元的人





##### 
	[sourcecode language="bash"]nawk -F[: ]$7+$6+$5  800 {print $1,$2} chapter6[/sourcecode]





##### 
	5 打印不在916区的人的姓





##### 
	[sourcecode language="bash"]nawk -F[: ]  !($3 ~ 916){print $2} chapter6[/sourcecode]





##### 
	6 打印月均捐款数额大于150美元的人的姓名和电话号码。





##### 
	[sourcecode language="bash"]nawk -F[: ]  ($5+$6+$7)/3  150 {print $1,$2}  chapter6[/sourcecode]





##### 
	7 打印每条记录，并在记录前加上其记录号





##### 
	[sourcecode language="bash"]nawk  {print NR,$0}  chapter6[/sourcecode]





##### 
	8 打印每个人的姓名和捐款数额





##### 
	[sourcecode language="bash"]nawk -F[: ]  {print $1,$2,$5+$6+$7}  chapter6[/sourcecode]




##### 
	9 把Elizabeth第二个月的捐款额加上10





##### 
	[sourcecode language="bash"]nawk -F[: ]  $1=="Elizabeth" {print $6+10} chapter6[/sourcecode]





##### 
	10 把Nancy McNeil的名字改成Louise McInnes






	

##### 
	[sourcecode language="bash"]nawk -F[: ] $1=="Nancy" {$1="Louise";$2="McInnes"; print $0} chapter6[/sourcecode]
	






