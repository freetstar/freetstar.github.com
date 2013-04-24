---
    author: admin
    comments: true
    date: 2011-02-03 21:20:07
    layout: post
    slug: install-the-debiandeb-package-on-the-ubuntu
    title: 误将debian的deb包在ubuntu安装之后的解决办法
    wordpress_id: 1595
    categories:
- 问题解决
---

有时候不小心将debian的deb包安装在了ubuntu下,导致报错,报错如下:The package XXX needs to be reinstalled, but I can’t find an archive for it.此处XXX对应相应的包名

此时只要在终端下运行这个命令即可

    dpkg --remove --force-remove-reinstreq XXX

其中XXX对应你的包名
