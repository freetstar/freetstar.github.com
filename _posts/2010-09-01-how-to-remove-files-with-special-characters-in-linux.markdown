---
author: admin
comments: true
date: 2010-09-01 20:11:13
layout: post
title: Linux下 rm 特殊符号前缀的文件
wordpress_id: 1212
categories:
- 问题解决
---

1 删除破折号"-"开头的文件

比如说当前文件夹下有-foo文件

可以使用下列命令

    rm -- -foo   

    rm ./-foo

    rm "-foo"

2  删除"-""/"等其他特殊符号前缀文件的最普遍方法

首先ls -il 查看文件的inode

然后运行，其中inode替换为相应文件的inode即可  

    find . -inum [inode] -exec rm -i {} \;

3 

还有个有意思的东东哦，你见过以"/"开头的文件么？

参考文章：

[http://johnny.chadda.se/article/how-to-remove-files-with-special-characters-in-linux/](http://johnny.chadda.se/article/how-to-remove-files-with-special-characters-in-linux/)

