---
    author: admin
    comments: true
    date: 2010-09-13 21:13:29
    layout: post
    title: 将man手册转成pdf文件
    wordpress_id: 1268
    categories:
- 问题解决
---

manpage，linux users和developers的瑞士军刀阿

今天在Happyaron大哥的blog上看到了一篇将man手册转换成pdf格式文件的日志，方法与大家共享

命令

man -t bash |ps2pdf - bash.pdf

解释：

    man -t  将man手册转换成groff格式，输出到标准输出

    ps2pdf -bash.pdf  将标准输入的文件转换成bash.pdf文件

用管道链接两个命令。一切就是这么简单

再举例，如果您想将man本身输出成pdf格式文件

man -t man|ps2pdf - man.pdf

参考：[http://blogs.gnome.org/happyaron/2010/09/13/convert-man-page-to-pdf/](http://blogs.gnome.org/happyaron/2010/09/13/convert-man-page-to-pdf/)

