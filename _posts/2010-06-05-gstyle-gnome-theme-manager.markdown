---
    author: admin
    comments: true
    date: 2010-06-05 14:33:19
    layout: post
    slug: gstyle-gnome-theme-manager
    title: Gstyle -一个全新的gnome 主题管理器
    wordpress_id: 258
    categories:
- ubuntu
---

    gstyle是一个强大的gnome主题管理器.此软件关注一个主窗口内每一个可能的主题类型.从gnome-look,deviantart, customize.org等网站下载的主题包可以通过此软件轻松安装,或者可以直接从gstyle里下载安装

**在ubuntu10.04/9.10中安装gstyle**

打开终端运行下列命令

    sudo apt-add-repository ppa:s-lagui  

    sudo apt-get update  

    sudo apt-get install gstyle

翻译:[FreeTstar](http://www.freetstar.com)

    via{[UbuntuGeek](http://www.ubuntugeek.com/gstyle-a-new-full-gnome-theme-manager.html)}

作者整理:

在终端中输入gstyle,提示报错

    glib.GError: 类型不匹配: 键 /desktop/gnome/interface/menus_have_icons 需要"string",实际为"bool"

解决方法:  运行gconf-editor

打开/desktop/gnome/interfaces , 新建一个键,名称为"menus_have_icons ",类型为"字符串",值随便来一个,然后确定(原键无法修改类型,故创建一个新键来覆盖原来的键)

终端再次输入gstyle

    glib.GError: 类型不匹配: 键 /desktop/gnome/interface/buttons_have_icons 需要"string",实际为"bool"

同样采取上述方法即可

目前可以安装内置有27个主题,秀下本人安装的mac主题.

[![](/media/images/2010-06-05-gstyle-gnome-theme-manager/Screenshot1.png)](/media/images/2010-06-05-gstyle-gnome-theme-manager/Screenshot1.png)

