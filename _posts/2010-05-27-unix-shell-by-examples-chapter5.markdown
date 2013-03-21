---
comments: true
date: 2010-05-27 01:14:20
layout: post
slug: unix-shell-by-examples-chapter5
title: ' unix shell范例精解第五章课后习题'
wordpress_id: 69
categories:
- PROGRAM
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








上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额<!-- more -->

注：以上内容被写进chapter5这个文档


###### 1 打印所有的电话号码：




###### [sourcecode language="bash"]nawk -F[: ] '{print $4}' chapter5[/sourcecode]


###### 2 打印Dan的电话号码：




###### [sourcecode language="bash"]nawk -F[: ] '{/^Dan/print $4}' chapter5[/sourcecode]


###### 3 打印Susan的姓名和电话号码：




###### [sourcecode language="bash"]nawk -F[: ] '/^Susan/{print $1, $2,$4}' chapter5[/sourcecode]


###### 4 打印所有以D开头的姓：




###### [sourcecode language="bash"]nawk -F[: ] '$2 ~ /^D/{print $2}' chapter5[/sourcecode]




###### 5 打印所有以C或E开头的名：




######  [sourcecode language="bash"]nawk -F[: ] '$1 ~ /^[C|E]/{print $1}' chapter5[/sourcecode]


###### 6 打印所有只有4个字母的姓：




###### [sourcecode language="bash"]nawk  -F[: ] '$2 ~ /^[A-Z][a-z][a-z][a-z]$/{print $2}' chapter5[/sourcecode]


###### 7 打印所有916区的人的姓：




###### [sourcecode language="bash"]nawk  -F[:  ] '$3 ~ /916/{print $1 , $2}' chapter5[/sourcecode]


###### 8  打印Mike的竞选捐款数额。打印时每个值都要要以美元符号开头，例如，$250,$100,$175




###### [sourcecode language="bash"]nawk  -F:  '$1 ~ /^Mike/{print "$"$3,"$"$4,"$"$5}' chapter5[/sourcecode]


###### 9 先打印姓，然后打印一个逗号，再打印名：




###### [sourcecode language="bash"]nawk -F[:  ] '{print$2 "," $1}' chapter5[/sourcecode]


### 




###### 10 写一个名为facts的awk的脚本，完成以下操作：打印McNeil（Savages）的全名和电话号码;打印Chet的捐款数额;打印所有第一个月捐款250美元的人




###### 原文中没有Savages，故以McNeil代替


[sourcecode language="bash"]
(1)cat   facts.sc
#This is a comment
#This is really my frist wak script!If u got a better way,please contact me.
$5 ~ /250/{print "--the 250$-- " $1,$2}
$2 ~ /McNeil/{print "\t\t    McNeil's info\n\t\t "$1,$2,$4}
$1 ~ /Chet/{print "\t\t     Chet  ""$"$5+$6+$7}
(2)nawk -F[: ] -f facts.sc chapter5
[/sourcecode]
感觉第十个问题解决得不够漂亮，由于nawk是对每一行单独处理的，导致输出的时候每想要的结果都是一行行自己列出来的，不整齐，待解决（可以尝试用sed）。


