---
author: admin
comments: true
date: 2011-05-22 16:45:48
layout: post
slug: windows7-pygtk-gtk
title: Windows7 64位下搭建PyGTK开发环境
wordpress_id: 1715
categories:
- PROGRAM
---

毕业设计用PyGTK实现的，理论上是可以跨平台的，但是其中用到的一些模块可能无法在Win下用（或许折腾折腾这些模块可以搞到win平台的，好吧，我没那么蛋疼）

Win7上搭建GTK和PyGTK开发环境的详细步骤：

一：环境说明

Windows 7 x86_64  没有安装Python

二：下载必要的包

python-2.6.5.msi  下载地址：[http://www.python.org/ftp/python/2.6.5/python-2.6.5.msi](http://www.python.org/ftp/python/2.6.5/python-2.6.5.msi)

﻿注：是32位的，不是64位的，因为接下来的其他安装包只能在32位Python上运行，我之前装64位Python时一直无法成功配置开发环境

pycairo-1.8.6.win32-py2.6.exe 下载地址：[http://ftp.gnome.org/pub/GNOME/binaries/win32/pycairo/1.8/pycairo-1.8.6.win32-py2.6.exe](http://ftp.gnome.org/pub/GNOME/binaries/win32/pycairo/1.8/pycairo-1.8.6.win32-py2.6.exe)

pygobject-2.20.0.win32-py2.6.exe 下载地址：[http://ftp.gnome.org/pub/GNOME/binaries/win32/pygobject/2.20/pygobject-2.20.0.win32-py2.6.exe](http://ftp.gnome.org/pub/GNOME/binaries/win32/pygobject/2.20/pygobject-2.20.0.win32-py2.6.exe)

pygtk-2.16.0+glade.win32-py2.6.exe 下载地址：[http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.16/pygtk-2.16.0+glade.win32-py2.6.exe](http://ftp.gnome.org/pub/GNOME/binaries/win32/pygtk/2.16/pygtk-2.16.0+glade.win32-py2.6.exe)

注意：如果使用的是Python2.6.5则下载的pycairo,pygobject,pygtk则都对应应该为py2.6的

gtk+-bundle_2.16.6-20100912_win32.zip 下载地址：[http://ftp.gnome.org/pub/gnome/binaries/win32/gtk+/2.16/gtk+-bundle_2.16.6-20100912_win32.zip](http://ftp.gnome.org/pub/gnome/binaries/win32/gtk+/2.16/gtk+-bundle_2.16.6-20100912_win32.zip)

注：都是用win32的，虽然宿主环境是64位win7

三：安装python2.6.5，这个不需要多废话，一步步的安装即可

然后编辑win7的环境变量，顺序依次是：Control Panel=>System=>Advanced System Setting=>Advanced>Environment Variables=>System  vaiables=>Path，将C:\Python26添加到环境变量中去

四：安装pycairo 安装pygobject 安装pygtk-2.16.0+glade.win32-py2.6.exe

可能出现的情况是：在安装时，系统提示找不到python2.6.5，这都是注册表的错，解决办法

参考本文：[http://weblogs.asp.net/bsimser/archive/2009/12/21/installing-pygtk-on-windows-x64.aspx](http://weblogs.asp.net/bsimser/archive/2009/12/21/installing-pygtk-on-windows-x64.aspx)

我简单说一下

> 问题产生的原因：
> 
> 

> 
> Python注册表的路径是：HKEY_LOCAL_MACHINE\SOFTWARE\Python
> 
> 

> 
> 而安装程序会去：HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node下寻找python
> 
> 

> 
> 修改问题的办法：
> 
> 

> 
> HKEY_LOCAL_MACHINE\SOFTWARE\Python把这个注册表output出来，然后用文本编辑器编辑一下，把output出来的注册表文本每一行的HKEY_LOCAL_MACHINE\SOFTWARE\Python在
> 
> 

> 
> SOFTWARE和Python中间加上Wow6432Node，然后保存好修改，退出。双击修改过的注册表，系统会提示你导入，导入后即可，然后到HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node
> 
> 

> 
> 找下Python是否出现，ok，搞定！

七：安装gtk+-bundle_2.16.6-20100912_win32.zip

解压到C盘gtk文件夹，gtk文件夹是我自己创建的（当然你也可以放到任何位置），然后编辑win7的环境变量，顺序依次是：Control Panel=>System=>Advanced System Setting=>Advanced>Environment Variables=>System  vaiables=>Path，将C:\gtk\bin添加到环境变量中去，非常建议写到最前边！ 

八：测试

输入gtk-demo测试gtk是否安装成功，打开python的gui IDE查看python的版本信息等等

> #!/usr/bin/env python  

import pygtk  

import gtk  

class Base:  

 def __init__(self):  

 self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)  

 self.window.set_default_size(200, 200)  

 self.window.connect('destroy', gtk.main_quit)  

 self.window.show()  

 def main(self):  

 gtk.main()  

if __name__==”__main__”:
> 
> 

> 
> base=Base()  

 base.main()

当然，你完全可以简单的在Python控制台输入import pygtk  import gtk等来测试python是否能找到这些包，找不到的话会报错的

折腾了一下午加一晚上才搞定这基本的开发环境，而且很多模块win下没有现成的，很蛋疼，需要自己移植;期间也遇到很多问题，如果你也遇到了请留言

上个小图：

![](http://ww3.sinaimg.cn/bmiddle/68785cf1tw1dhemnebz84j.jpg)

��题，如果你也遇到了请留言

上个小图：

![](http://ww3.sinaimg.cn/bmiddle/68785cf1tw1dhemnebz84j.jpg)

