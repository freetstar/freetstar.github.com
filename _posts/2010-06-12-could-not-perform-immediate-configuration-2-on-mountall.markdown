---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

---
author: admin
comments: true
date: 2010-06-12 17:40:36
layout: post
slug: could-not-perform-immediate-configuration-2-on-mountall
title: Could not perform immediate configuration (2) on mountall 错误探究
wordpress_id: 591
categories:
- 问题解决
---

	 下午学姐找我说新装的ubuntu9.10什么软件也装不了,急急忙忙吃了中午饭,直奔教学楼而去

	 电脑环境:  

> 
	
> 
> 
		 PC环境是虚拟机,用sudo fdisk -l查看分区情况,分两个区,根挂载在/dev/sda1,swap分区挂载在/dev/sda5
	
> 
> 

	 错误提示情况:

> 
	
> 
> 
		 运行命令sudo apt-get install libboost-dev,提示有许多包要安装,其中就有mountall这个包,最后一句是E:Could not perform immediate configuration (2) on mountall  
	
> 
> 

	 探究和解决过程

> 
	
> 
> 
		 之前在CSDN里回过一个帖([here](http://topic.csdn.net/u/20100407/15/A2E683E6-9CC2-47BF-B765-36241A2A7E0B.html)),lz按我给的网址([here](http://nerdbynature.de/s9y/index.php?/archives/173-Internal-Error,-Could-not-perform-immediate-configuration-2-on-mountall.html))解决了...大概意思说的是swap分区无法挂载,需要将fstab里的swap分区给注释掉
	
> 
> 
	
> 
> 
		<!-- more -->
	
> 
> 
	
> 
> 
		 帖子里详细步骤(略有增删)
	
> 
> 
	
> 
> 
		 [code language="bash"] 
sudo chmod a+w /etc/fstab 
vi /etc/fstab //注释掉swap相应的行 
mountall 
dpkg --force-all -i /var/cache/atp/archives/mount_2.17.2-0ubuntu1_i386.deb 
sudo apt-get -f install 
[/code] 
	
> 
> 
	
> 
> 
		 按照上述方法安装,注释掉swap行之后,运行mountall命令,依然报错,具体错误信息没记下来= =!
	
> 
> 
	
> 
> 
		 继续进行后两步试试,依然报错
	
> 
> 

	 要是自己的电脑就好了,有时间倒腾,看看到底出啥错了,可以想许多办法... 后来直接蛮力得给学姐重做虚拟机,可惜对虚拟机不太熟悉,没装成~ ~

	 谈一下自己的对这个错误的认识和觉得一些可行的修复方法吧

> 
	
> 
> 
		 1:不要分swap分区- -!我承认我很邪恶
	
> 
> 
	
> 
> 
		 2:依然尝试注释掉swap分区,重复上述步骤,仔细研究报错的解决办法
	
> 
> 
	
> 
> 
		 3:sudo apt-get install libboost-dev时,系统提示安装的包中包含了mountall这个包,是不是只要安装包时包含mountall这个包,就是报题目的错?!
	
> 
> 
	
> 
> 
		 4:sudo apt-get install mountall --reinstall 重新安装下试试
	
> 
> 
	
> 
> 
		 5:系统中并没有损坏的包,所以不可能用网上一些同志用修复包的方法来解决问题...[here](http://forum.ubuntu.org.cn/viewtopic.php?f=48&t=271962),有可能是倚赖没装全吗?学姐的电脑倒是很多要升级的东西...
	
> 
> 
	
> 
> 
		 6:没有解决不掉的问题,相信自己,相信网络,相信群众的力量
	
> 
> 

