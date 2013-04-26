---
    author: admin
    comments: true
    date: 2013-04-24 13:55:31
    layout: post
    title: archlinux 更新intel集显模式

---

i5-2300 的cpu，自带GPU，更新Gnome-shell 3.8.1后进不去gdm,一番搜索以后发现是
Intel的GPU加速模式有问题，默认是uxa,需要更新至SNA,详见官方文档

[https://wiki.archlinux.org/index.php/Intel#Choose_acceleration_method](https://wiki.archlinux.org/index.php/Intel#Choose_acceleration_method)

具体方法:

创建

/etc/X11/xorg.conf.d/20-intel.conf 

添加以下内容:

    Section "Device"
    Identifier  "Intel Graphics"
    Driver      "intel"
    Option      "AccelMethod"  "sna"
    EndSection
