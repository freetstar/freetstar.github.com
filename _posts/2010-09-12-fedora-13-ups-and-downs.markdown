---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

---
author: admin
comments: true
date: 2010-09-12 18:11:42
layout: post
slug: fedora-13-ups-and-downs
title: Fedora 13 历险记
wordpress_id: 1252
categories:
- 问题解决
---

	本文可能写得会有点杂乱无序，唠唠叨叨的，：）

	之前本本装的是ubuntu10.04和Fedora 12 ，前天想起来Fedora13的DVD盘早刻好了，一直没有升级到Fedora13.于是就升级了一下，结果出现各种问题

	一：Fedora 12升级到13

	开机把亲爱的DVD盘放进光驱，重启之后选择光盘，进入安装升级界面，提示系统已经安装了Fedora12,选择全新安装或升级安装，我选择升级至Fedora13，在Grub处选择第2个选项，具体不记得了，大概是对Grub不进行改动吧.....因为我要用Ubuntu的Grub做Boot loader。下一步之后，系统开始升级，大概有1400个包吧，等着吧，就去舍友电脑上玩植物打僵尸去了。。

	大约1小时候后？我回来了，系统升级完毕，弹出光盘，搞定！

	重启机器，等启动界面慢慢爬过之后，弹出一个对话框

	"can't open the theme:/usr/share/kde/apps/kdm/themes/Goddard"(大概是这句话，具体记不清出了)<!-- more -->

	然后开始google，拿我可爱的Nokia5320上UC浏览器google，好吧，都是提示更改开机登录管理器，选择gdm之类的，我忘了我装没装Gnome桌面。心想，没救了，突然灵光一现

	Ctrl+Alt+F2进入控制台，切换到刚才提到的文件夹中:

	/usr/share/kde/apps/kdm/themes/ 

	然后ls

	发现有Goddard这个文件夹，还有Oxygen，Oxygen-air其他的文件夹

	然后

	sudo rm -rf  Goddard/

	sudo cp -r Oxygen/ Goddard/

	哈哈，把Goddard用Oxygen代替了

	重启，O YEAH！

	顺利打开Kdm，输入亲爱的密码，第一次进入Fedora 13！

	升级部分到此完毕！

	二 Fedora 13配置记

	在fedora12时已经将用户lgx配置到sudoers中，具体方法见_[http://pengjiayou.com/](http://pengjiayou.com/)_的Fedora12 配置手册，以后就可以象ubuntu一样，直接运行sudo来获得管理员权限了。

	在配置过程中遇到很多问题，可能说的无序

	比如机器在内存占用不大的情况突然死机，只有鼠标能够移动，连虚拟控制台都进不去。。。

	听我慢慢道来吧：

	打开终端

	sudo yum update  （我以为和ubuntu差不多，都是更新软件包信息，打开另一个终端，yum --help看了一下，原来yum的update直接就升级安装各种包了。。冏）

	经过计算，总共要下载1.2G的包包，好吧，我等了一下午，当install过程一步步进展顺利时，fedora再次无语的死机，无奈，强制关机重启

	重启之后，登录界面打不开了，停留在可爱的fedora标志下的蓝色背景中。

	好吧，Alt+F2进入控制台，登录进去之后

	sudo shutdown -r now 

	然后在开机界面选择Grub时，按下"e"键，把传递给内核的参数rhgb删除了，之后进入Fedora文本界面启动过程，提示一切服务加载正常，在atd之后停留，kdm进程没有被加载。。

	估计是安装过程被打断，导致qt安装出现问题，因为kdm是依赖qt的，所以kdm也无法加载，无奈之余，再次进入登录控制台，

	运行

	sudo yum update 

	提示有错误产生，要运行yum-compliction-trasaction 

	好吧，我运行之后提示python-devel与python冲突，yum info python python-devel发现居然安装了两个python，status都是installed，估计这样导致出错了

	于是

	sudo yum-complication-transaction --skip-broken

	一切完好。。。

	然后运行

	sudo yum update 

	报错：qtX11 和qt冲突。。。

	更无奈之中，只好

	sudo yum remove qt 

	结果你懂得，一大堆东西要依赖qt的，kdm被删除了，amrok被删除了，就连konsole也没了。。还有很多很多。。。

	为了把python冲突也给解决掉，我又很暴力的

	sudo yum remove python 

	之后sudo yum update 运行正常，不过系统在yum-complication-transaction处停留了很久，应该是全面检测包信息吧，无论如何，最后那些包还是安装上了

	然后重新安装qt，

	sudo yum install qt

	最后安装kdm

	sudo yum install kdm 

	重启，Fedora 13正宗的登录界面出现了，输入密码，又一次进入桌面

	不出所料，konsole无法打开，许多软件因为依赖关系被删除了，悲剧阿！

	没办法，一步步来吧。。

	打开xterm，输入

	sudo yum install kdelibs 

	然后konsole可以了，这是头等大事阿

	然后很邪恶的去安装显卡驱动了，参考帖

	_[http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/](http://lishaohui.qd.blog.163.com/blog/static/48658916201042883056152/)_

	不过此帖子没有给出判断内核模式的方法，我的内核模式是PAE，一般：uname -a 即可，

	安装好重启之后，到了fedora的蓝色背景那里后无法出现kdm，进入控制台：）好像第好n次了吧

	查看系统的log日志文件

	vi /var/log/Xorg.0.log

	提示nvidia.ko又问题，应该是内核无法加载吧

	无奈手机继续google

	_[http://www.linuxidc.com/Linux/2010-07/27312.htm](http://www.linuxidc.com/Linux/2010-07/27312.htm)_

	根据上帖，在Grub界面对Fedora内核参数后添加rdblacklist nouveau了 （这个后来我子啊ubuntu的/boot/grub/grub.cfg中手动添加了）

	重启，搞定。。就是多了Nvidia的logo

	修改/etc/X11/Xorg.conf

	添加"Option" "NoLogo" "True"就可以了

	三：开始正式使用中

	其实用Fedora用几个原因把，作为Linux界大哥红帽的桌面版，Fedora集成了很多先进的技术，同时Fedora貌似也是很多Linux开发人员的得力助手，具有完备的开发环境，同时自己也可以体验下rpm系的linux发行版

	这几天在看Redhat 服务器管理与应用，暂且拿Fedora来体验下吧。

	最近也把Shellscript看得差不多了，打算开始好好掌握Linux c/C++。

	其实自己也比较乱，以linux为核心工作又很多发展方向，linux应用软件开发，linux网络工程师，系统管理员，嵌入式开发。现在自己是到处看，四处望。

	路漫漫其修远兮，吾将上下而求索

