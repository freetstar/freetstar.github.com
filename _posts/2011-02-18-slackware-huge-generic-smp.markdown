---
author: admin
comments: true
date: 2011-02-18 10:30:36
layout: post
slug: slackware-huge-generic-smp
title: slackware下内核的huge，generic，smp模式等等
wordpress_id: 1604
categories:
- Opensource
---

** **

** **

现在用的是ubuntu+slackware的双系统，用ubuntu的grub2做引导器，运行sudo update-grub之后，系统能找到ubuntu和slackware，但每次开机菜单里有4个slackware引导项，只有 带huge的kernel才能进去，也就是第三个和第四个详细见ubuntu操作系统下/boot/grub/grub.cfg文件，我暂且把其中的slackware部分的发上来

menuentry "Slackware Linux (Slackware 13.1.0) (on /dev/sda2)" {

insmod part_msdos

insmod ext2

set root='(hd0,msdos9)'

search --no-floppy --fs-uuid --set dea45308-63fa-4014-83b6-dadd1c4802ea

linux /vmlinuz-generic-2.6.33.4 root=/dev/sda2

}

menuentry "Slackware Linux (Slackware 13.1.0) (on /dev/sda2)" {

insmod part_msdos

insmod ext2

set root='(hd0,msdos9)'

search --no-floppy --fs-uuid --set dea45308-63fa-4014-83b6-dadd1c4802ea

linux /vmlinuz-generic-smp-2.6.33.4-smp root=/dev/sda2

}

menuentry "Slackware Linux (Slackware 13.1.0) (on /dev/sda2)" {

insmod part_msdos

insmod ext2

set root='(hd0,msdos9)'

search --no-floppy --fs-uuid --set dea45308-63fa-4014-83b6-dadd1c4802ea

linux /vmlinuz-huge-2.6.33.4 root=/dev/sda2

}

menuentry "Slackware Linux (Slackware 13.1.0) (on /dev/sda2)" {

insmod part_msdos

insmod ext2

set root='(hd0,msdos9)'

search --no-floppy --fs-uuid --set dea45308-63fa-4014-83b6-dadd1c4802ea

linux /vmlinuz-huge-smp-2.6.33.4-smp root=/dev/sda2

}

由上可见，所有的配置选项里都没有initrd。可是有huge字样的kernel模式的都可以成功引导，没有则无法成功

这里就说到了slackware的内核模式了，详细见这里slackware12.0发行通告：[http://www.slackware.com/announce/12.0.php](http://www.slackware.com/announce/12.0.php)

这里我也稍微介绍一下 ：

slackware-generic版本

这种内核模式下，所有的驱动程序都被单独的编译成位一个模块，需要时加载。也就是说，用这样的vmlinuz-generic-2.6.33.4压缩内核来引导系统时，需要有initrd来辅助vmlinuz完成系统boot过程，关于vmlinuz和initrd的知识详见：[here](http://blogold.chinaunix.net/u2/63038/showart_500230.html)

注：在其他发行版，比如ubuntu中还有一说，generic一般表示是通用的内核版本,支持大部分的处理器

linux的smp技术

** **SMP的全称是"对称多处理"（Symmetrical Multi-Processing）技术，是指在一个计算机上汇集了一组处理器(多CPU),各CPU之间共享内存子系统以及总线结构。它是相对非对称多处理技术而言的、应用十分广泛的并行技术。在这种架构中，一台电脑不再由单个CPU组成，而同时由多个处理器运行操作系统的单一复本，并共享内存和一台计算机的其他资源。虽然同时使用多个CPU，但是从管理的角度来看，它们的表现就像一台单机一样。系统将任务队列对称地分布于多个CPU之上，从而极大地提高了整个系统的数据处理能力。所有的处理器都可以平等地访问内存、I/O和外部中断。在对称多处理系统中，系统资源被系统中所有CPU共享，工作负载能够均匀地分配到所有可用处理器之上。简单来说，就是将多个cpu当成一个来用，提高计算性能和I/O性能，是现代大部分计算机系统上软件

查看是否在是使用的smp的内核uname -a|grep --color=always -i "smp"，看是否有结果。一般较新的linux发行版都会在安装时检测是否有多个cpu或者多核，然后自动安装smp和普通的内核。ubuntu貌似默认就是smp，而slackware等其他发行版有其他smp和其他模式

自己编译smp的内核支持
 
 make menuconfnig
 
 选取 Processor type and features
 
 选取==>Support for suspend on SMP and hot-pluggable CPUs (EXPERIMENTAL)
 
 选取==>Symmetric multi-processing support #SMP 支持

slackware的huge版本

huge模式从字面上来看就是很大，huge本来是在linux系统安装时为了方便安装顺利进行，把所有的驱动都安装到kernel中了，当然也可以平常使用huge模式。这也就是上边为什么huge模式为什么不需initrd就可以引导系统了，他把磁盘驱动和文件系统驱动编译进内核里，这样他不需要依赖initrd就可以直接引导了，

说完了这些，为了使用第一个和第二个的generic内核模式， 我们就需要手动去创建initrd了。具体关于initrd的知识可以查看slackware下的/boot/README.initrd，下文我将尝试 创建initrd文件，然后修改ubuntu下的的grub.cfg配置文件，完整完成slackware的引导

肯定有不对的地方，往大家指出

学习资料：

[http://liubin.blog.51cto.com/282313/99100](http://liubin.blog.51cto.com/282313/99100)

[http://www.phy.duke.edu/~rgb/Beowulf/smp-faq/prive/mentre/smp-faq/smp-faq-3.html](http://www.phy.duke.edu/~rgb/Beowulf/smp-faq/prive/mentre/smp-faq/smp-faq-3.html)

[http://www.linuxsir.org/bbs/thread354056.html](http://www.linuxsir.org/bbs/thread354056.html)

[http://mirror.switch.ch/ftp/mirror/slackware/slackware-12.2/README.initrd](http://mirror.switch.ch/ftp/mirror/slackware/slackware-12.2/README.initrd)

[http://www.linuxforums.org/forum/slackware-linux/115663-add-slackware-grub.html](http://www.linuxforums.org/forum/slackware-linux/115663-add-slackware-grub.html)

[http://blogold.chinaunix.net/u2/63038/showart_500230.html](http://blogold.chinaunix.net/u2/63038/showart_500230.html)
