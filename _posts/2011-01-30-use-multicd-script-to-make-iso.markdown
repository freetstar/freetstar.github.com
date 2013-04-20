---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
---
author: admin
comments: true
date: 2011-01-30 15:28:55
layout: post
slug: use-multicd-script-to-make-iso
title: 用MultiCD和UNetbootin制作支持多Linux发行版启动的u盘
wordpress_id: 1579
categories:
- ubuntu
- 软件安装
---

本以为原来手机上挂的u盘丢了,就又去买了一个u盘,谁知道后来又找到了,为了充分利用和实现自己以前想制作多启动u盘想法,下面利用multicd和UNetbootin来制作多启动u盘

首先介绍下MultiCD,

官方主页:[http://multicd.tuxfamily.org/](http://multicd.tuxfamily.org/)

功能介绍:简单来说就是可以把多个linux发行版的iso镜像合并成一个iso镜像,支持的linux发行版有ubuntu,archlinux,suse,slax,fedora等等等等等等.....当然,还能够支持一些windows的iso文件.支持的发行版:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros)

使用方法:

第一步:下载必要的镜像

到这里下载slax:[http://www.slax.org/get_slax.php](http://www.slax.org/get_slax.php)

到这里下载ubuntu:[http://www.ubuntu.com.cn/desktop/get-ubuntu/download/](http://www.ubuntu.com.cn/desktop/get-ubuntu/download/)

到这里下载tiny core linux:[http://www.tinycorelinux.com/](http://www.tinycorelinux.com/)

到这里下载:sysrescue:[http://www.sysresccd.org/](http://www.sysresccd.org/)

到这里下载puppy:[http://puppylinux.org/main/Download%20Latest%20Release.htm](http://puppylinux.org/main/Download%20Latest%20Release.htm)

到这里下载archlinux:[http://www.archlinux.org/download/](http://www.archlinux.org/download/)

到这里下载Gparted:[http://sourceforge.net/projects/gparted/files/gparted-live-stable/](http://sourceforge.net/projects/gparted/files/gparted-live-stable/)

到这里下载Clonezila:[http://clonezilla.org/downloads.php](http://clonezilla.org/downloads.php)<!-- more -->

![](http://i.imgur.com/IW00Z.png)

第二步:开始正式安装

1创建一个文件夹

mkdir ~/multicd

2 进入文件夹,并下载multicd脚本

cd ~/muitlcd

wget  ftp://downloads.tuxfamily.org/multicd/multicd-6.3.sh

3 将第一步下载的镜像拷贝到multicd文件夹中,并进行改名,改名规则:[http://multicd.tuxfamily.org/#SupportedDistros](http://multicd.tuxfamily.org/#SupportedDistros).比如说puppy必须改名为_puppy.iso_

刚开始我没怎么改名也能够成功,有兴趣研究下这个脚本吧,里边貌似有主动帮你改名的代码

4 赋予刚才下载脚本执行权限

chmod +x multicd-6.3.sh

sudo ./multicd-6.3.sh 这是一些[参数](http://multicd.tuxfamily.org/#Arguments)

会生成一个大iso文件(我的一直报tiny core错误,然后就把这个镜像给排除了)

5 用vb等虚拟机试试这个iso文件起作用不,一切顺利的话再利用UNetbootin来将这个iso做到u盘上

![](http://i.imgur.com/fvArN.png)

6 可以开机试试了
