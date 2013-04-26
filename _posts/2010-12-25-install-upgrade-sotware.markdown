---
    author: admin
    comments: true
    date: 2010-12-25 11:22:56
    layout: post
    title: 小记:日常软件整理
    wordpress_id: 1545
    categories:
- ubuntu
- 软件安装
---

心血来潮 我把openoffice给卸载了,用源也将virtualbox升级到了4.0的正式版,同时开始尝试firefox4.0b8

一:卸载掉OO,装上LibreOffice

    sudo apt-get autoremove openoffice-common 先卸载掉再说
然后下载[libreoffice3.3.0-rc2](http://www.documentfoundation.org/download/)
也可以到这里下载[here](http://download.documentfoundation.org/libreoffice/testing/3.3.0-rc2/deb/x86/)
另外有语言包,可以自己选择下载
准备安装

    tar zxvf  LibO_3.3.0rc2_Linux_x86_install-deb_en-US.tar.gz
    ls
DEBS  readmes update
DEBS里是必要的deb包,readmes中是安装方法和安装语言包的一些介绍
开始安装.进入DEBS文件夹
    sudo dpkg -i *.deb
然后进入desktop-integration文件夹
再次运行
    sudo dpkg -i *.deb

二:安装virtualBox4.0

如果之前安装过
    sudo apt-get autoremove virtualbox- [这里tab一下,对应你安装的版本]
增加vb的10.10源,并安装

    echo "deb http://download.virtualbox.org/virtualbox/debian $(lsb_release -sc) contrib" | sudo tee -a /etc/apt/sources.list
    wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install virtualbox-4.0

对于usb2.0的支持,VirtualBox RDP和PXE对于intel的支持,需要安装这个扩展包,下载地址
[ http://download.virtualbox.org/virtualbox/4.0.0/Oracle_VM_VirtualBox_Extension_Pack-4.0.0-69151.vbox-extpack](http://download.virtualbox.org/virtualbox/4.0.0/Oracle_VM_VirtualBox_Extension_Pack-4.0.0-69151.vbox-extpack)

三:安装多个版本的firefox浏览器
怎么说ff也是浏览器界的大哥大姐了,试试最新的4.0.8吧//firefox4.0b9pre也有了,
下载地址:
[here](ftp://ftp.mozilla.org/pub/mozilla.org/firefox/releases/4.0b8/linux-i686/zh-CN/)
参照方法:天大的某位帅哥的[方法](http://forum.ubuntu.org.cn/viewtopic.php?f=73&t=294406&p=2168882#p2168882)
开始安装
    tar jxvf firefox-4.0b8.tar.bz2
    cp -r firefox/ /opt/
    sudo chown lgx.lgx /opt/firefox/
    mkdir profile4.0b8
/opt/firefox/firefox -profilemanager
然后创建配置文件,根据步骤提示选择新的配置文件名,并选择刚才创建的文件夹
这样就完成了大部分的工作

然后创建快捷方式,图标什马的自己选一个就好了,命令是关键
/opt/firefox/firefox -profile /opt/firefox/profile4.0b8
