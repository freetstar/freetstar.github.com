---
    author: admin
    comments: true
    date: 2010-10-02 15:56:02
    layout: post
    title: 双linux系统折腾Grub记
    wordpress_id: 1307
    categories:
- 问题解决
---

    ubuntu10.04用的是Grub2,而我一直不太懂和熟悉Grub2的配置文件，心理对Grub有点阴影了。。

前几天刚刚把Fedora 13勉强装好，没办法，这几天迫于工作鸭梨和工作方便，老板点名说要我学Redhat，可哪里有免费的Redhat，没办法我就用centos了。于是中午兴致勃勃地把早已经下载好的镜像刻盘去了，顺便把Slackware13.1，Opensuse11.3的DVD镜像都刻盘了。。数数现在手里好像放着好多发行版。。。依次点个名吧：

Ubuntu 9.04到10.04，Opensue11.2和Opensuse11.3 ,Slaceware13.1， 红旗的桌面版SP3,Qomo1.0（感谢天大自由软件联盟给我这两张盘），Fedora 12和Fedora13，linuxmint8和linuxmint9,Centos5.5/很多都没有机会尝试。鉴于我的本本的配置，跑虚拟机是肯定很吃力。。上学期买的旧电脑也跑不起来，郁闷。

再扯回来，这次安装打算在Fedora的分区基础上格式化安装Centos，本来之前是只有Centos的镜像，也不打算刻盘的。希望用硬盘安装的方法来安装的，只需要修改下Grub配置即可。说明一下之前的fedora13分区情况

    /  /dev/sda2
    /boot  /dev/sda9
    /home  /dev/sda5
    swap  /dev/sda7  //swap分区和Ubuntu的swap分区共用，

我在ubuntu将Centos镜像的ioslinux文件解压至我的/home目录，然后然后修改/boot/grub/grub.cfg

增加了

    menuentry "Centos install"{

    recordfail

    insmod ext2

    set root='(hd0,7)' //我的ubuntu的home挂载在 /dev/sda7

    linux /ioslinux/vmlinuz****

    initrd /ioslinux/initrd***

}

保存之后重启，到了grub界面选择进入Centos install，提示无法找到内核文件.。然后没多想Grub配置方面的问题，想就此应该是硬盘失败了。于是乎就有了刻盘这个经过。。

然后下午可好盘之后，顺利地在Fedora13的分区基础上进行了Centos的安装，安装时没有选择安装Grub程序，重启后Grub界面没有Centos的选项。

我自信满满地说，这个难不倒我。不就是进去系统运行sudo update-grub2 嘛。。这个命令运行之后，确实发现了安装在/dev/sda2分区上的Centos，没有报错。可是重启以后Grub仍然不显示Centos。其间我还傻傻地用livecd和liveusb重装了好几次grub，仍然不行。（这时候上面硬盘安装时写进去的"Centos install"当然已经失效了）

没办法，只好重新自己好好整整grub.cfg这个配置文件了。

刚开始，添加 

    menuentry "Centos using"{

    insmod ext2

    set root='(hd0,2)'

    linux /boot/vmlinuz-2.6.18-194.el5 root=/dev/sda2

    initrd /boot/initrd-2.6.18-194.el5.img

}

重启之后，依然没办法进系统，显示无法挂载/dev等文件系统，我想应该还是root环境设置的问题吧，不知道怎么想的，就把/boot改成了(hd0,9)，也就是下面的配置文件

    menuentry "Centos using"{

    insmod ext2

    set root='(hd0,2)'

    linux (hd0,9)/vmlinuz-2.6.18-194.el5 root=/dev/sda2

    initrd (hd0,9)/initrd-2.6.18-194.el5.img

}

重启之后，顺利进入Centos的第一次系统配置界面。一切搞定！

Grub的配置文件真搞不懂。。。许多网上的朋友写的教程对我来说不可用，我想可能是因为他们没有将/boot单独分区进行挂载吧，而我的系统是将/boot独立出来的。

明天开始实习上班了，要学红帽下tomcat，nginx，samba，ftp等等。。希望一切顺利 

