---
    author: admin
    comments: true
    date: 2012-11-28 13:55:31
    layout: post
    slug: archlinux-fix
    title: archlinux修复记
    wordpress_id: 1949
    categories:
- linux前沿
---

    archlinux3个月没有更新，刚来学校就sudo pacman -Syu，结果果真遇到glibc的冲突，没有强制--force安装，根据[wiki](https://www.archlinuxcn.org/lib-%E7%9B%AE%E5%BD%95%E6%94%B9%E4%B8%BA%E6%8C%87%E5%90%91-usrlib-%E7%9A%84%E8%BD%AF%E9%93%BE%E6%8E%A5/#more-203)走了一遍，还是悲催的失败了，可能是各种包更新依赖关系坏掉了。开机无法进系统，提示glibc出问题了。

    遂想到使用chroot处理这种问题，开始将ubuntu镜像使用unetbootin烧制到了u盘中，无法使用，google后发现u盘需要格式化为FAT32格式（蛋疼中。。。），成功启动到ubuntu使用界面，打开gnome-terminal，开始遵循archwiki的[chroot](https://wiki.archlinux.org/index.php/Chroot)进行操作，提示

    chroot: cannot execute /bin/sh: Exec format error 

看wiki中提到最好使用同样架构的linux，因为archlinux用的是64位架构，遂下载64位架构的ubuntu镜像，重新烧制，引导，重新chroot成功。

   chroot方法简记：

1 寻找要挂载的根分区，lsblk /dev/sda,

2 创建临时目录，挂载根分区（以及其他必须的分区）mkdir /mnt/arch ;mount /dev/sda5 /mnt/arch

3 挂载临时文件系统

# cd /mnt/arch
# mount -t proc proc proc/
# mount -t sysfs sys sys/
# mount -o bind /dev dev/
# mount -t devpts pts dev/pts/

4 正式开启chroot环境

    chroot .

5 开始修复系统

    chroot真是个不错的东东

PS:解决glibc强制--force后遗症的办法之一：[hehe](http://forum.ubuntu.org.cn/viewtopic.php?f=155&t=380980)

