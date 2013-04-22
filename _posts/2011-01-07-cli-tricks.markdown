---
author: admin
comments: true
date: 2011-01-07 22:42:34
layout: post
slug: cli-tricks
title: 一些积累的CLI Tricks
wordpress_id: 1558
categories:
- PROGRAM
---

删除文件中的空行
[code language="bash"]grep . oldfile >newfile
grep -v "^$" oldfile >newfile
[/code]

压缩字符串里的空格
[code language="bash"]tr -s " " " " strings[/code]

scp小用：
scp也可以在本地机器中当成cp用，如：
[code language="bash"]cp file1 file2[/code]
scp file1 file2
当然scp主要是用户网络传输的
[code language="bash"]scp tem.pdf username@remotemachine:[/code]
注意：“：”，同志们可以想象下没有冒号会怎么样

充分利用alias吧
比如说：cd3 cd4
[code language="bash"]alias cd3='cd ../..'
alias cd4='cd ../../..'[/code]

用组合键对付长命令行
[code language="bash"]ctrl+a 行首
ctrl+e 行尾
ctrl+u 光标前
ctrl+k 光标后
ESC+.调出上次你的命令所使用的参数
Ctrl+R 搜索[/code]

用fc命令将上次执行过的命令放到编辑器中执行
当然也可以用Ctrl+x和Ctrl+e来执行

正用着vim了却想起来某个命令没有执行怎么办
[code language="bash"]Solution1： 执行：！命令
Solution2： Ctrl+z先挂起来，回来运行玩了命令再玩你
[/code]
快速的给文件改后缀
[code language="bash"]rename html htm  *.html[/code]

