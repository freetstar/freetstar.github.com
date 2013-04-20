---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
---
author: admin
comments: true
date: 2011-01-08 17:13:10
layout: post
slug: redhat4-8-setting-bond0
title: Redhat4.8配置bond0小记
wordpress_id: 1560
categories:
- 服务器
---

武清机房1日游
先上几张小图...
![](http://i.imgur.com/PQlA3.jpg)
![](http://i.imgur.com/4HPBX.jpg)
最后系统装完搞定之后,大哥吩咐做bond0,结果被乙方公司派来搞服务器的哥们儿不会做,立马上手坐,之前只稍微看过一点文档,
打开手机,uc,接着问google大哥,于是有了这篇小记:

bond0的原理:
将两块以及更多的网卡虚拟成有一个网卡,形成一个ip对外提供服务.有利于负载均衡,
bond0的制作:
以Redhat4.8为例子
第一步:首先确认系统支持
[code language="bash"]modprobe bond[tab]看一下是否有对应的模块[/code]
第二步:<!-- more -->
制作bond0,以root身份
[code language="bash"]cd /etc/sysconfig/network-scripts/[/code]
生成bond0的配置文件
[code language="bash"]vi ifcfg-bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.XX.XX //写成自己要的,下边的自己也对应着改
NETMASK=255.255.255.0
GATEWAY=192.168.XX.XX
USERCTL=no[/code]
修改对应网卡的配置文件,比如说你打算使用eth0和eth1做bond
[code language="bash"]vi ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=none
MASTER=bond0
USERCTL=no[/code]
然后
[code language="bash"]cp ifcfg-eth0 ifcfg-eth1
sed -i 's/eth0/eth1/g' ifcfg-eth1[/code]
第三步:
修改系统配置
[code language="bash"]vi /etc/modprobe.conf
alias bond0 bonding
options bond0 millmon=100 mode=1
//mode 1主备工作 mode 0 同时工作[/code]
加入启动项
[code language="bash"]vi /etc/rc.d/rc.local
ifenslave bond0 eth0 eht1[/code]
第四步:
重启网络服务
[code language="bash"]service network restart
ifconfig //检查bond0是否出现,也可以ping下自己[/code]
更多的资料:[here](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/bonding.txt)
