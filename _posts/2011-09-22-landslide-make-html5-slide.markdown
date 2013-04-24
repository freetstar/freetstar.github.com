---
    author: admin
    comments: true
    date: 2011-09-22 20:08:38
    layout: post
    slug: landslide-make-html5-slide
    title: 用landslide创建html5 slide
    wordpress_id: 1794
    categories:
- Opensource
---

[Landslide](https://github.com/adamzap/landslide)是一款用python写的制作Html5 slide的软件。

Landslide通过源代码来产生Html文件。

举个例子，制作一个介绍python流程控制的slide，这里是Rst源码

Python
======

--------------

If
==

* Please don't use ()
* Never forget the ``:`` at the end of the line

Check this code:

.. sourcecode:: python

    x, y = 1, 2
    if x > y:
    print 'x is greater'

--------------

For
===

* ``for`` iterates over a sequence
* Never forget the ``:`` at the end of the line

Check this code:

.. sourcecode:: python

    numbers = [1, 2, 3, 4, 5,]
    for number in numbers:
    print number

--------------

While
=====

* ``while`` is like ``if``, but executes while the codition is ``True``
* please don't use ()
* never forget the ``:`` at the end of the line

Check this code:

.. sourcecode:: python

    from random import randint

    args = (1, 10,)
    x = randint(*args)
    while x != 6:
    x = randint(*args)

--------------

Thank you!
==========

首先要安装landslide，利用python得easy_install工具即可方便安装

    sudo easy_install landslide

保存上边的RST代码为python.rst，运行

    landslide python.rst即可产生html文件，效果图

[![](http://www.freetstar.com/wp-content/uploads/2011/09/1316693142881-uploadscreenshot-dot-com-1024x250.png)](http://www.freetstar.com/wp-content/uploads/2011/09/1316693142881-uploadscreenshot-dot-com.png)

原文：[here](http://f.souza.cc/2011/09/creating-html-5-slide-presentations-using-landslide/)

好玩，下次的slide就用它做了，顺便学学css和rst。。。
