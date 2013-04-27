---
author: admin
comments: true
date: 2010-07-04 02:19:30
layout: post
title: 浅谈ubuntu10.04 server Apache2.0 性能优化
wordpress_id: 876

---

近来VPS的Apache耗MEM耗得可怕,于是想到优化下Apache2

Apace2.0 中最影响性能优化的最核心特性是:MPM(Multi-Processing Modules)

要想让Apache的性能最佳,第一步要做的,就是要选择合适的MPM

下面简单介绍Apache2的3个MPM

    event模式

比较适合那些需要有大量持续链接(KeepAlive traffic)的情况.KeepAlive的好处是,可以在同一个TCP链接中响应多次请求;这种方式,可以使一个包含大量图片的HTML文档加速50%.在配置文件中设置KeepAlive为On,即可启用KeepAlive

    prefork模式（默认）  

这个多路处理模块(MPM)实现了一个非线程型的、预派生的web服务器，它兼容Apache 1.3。它适合于没有线程安全库，需要避免线程兼容性问题的系统。它的特点:虽然不是很快,但是很稳定.它能够隔离每个请求,所以,如果某个请求出现故障,不会影响其他的请求.prefork由一个主进程在那里负责,事先派生出一些子进程,这样一旦有访问需求,客户机就不必再等待服务器产生子进程所花的时间.这个MPM具有很强的自我调节能力，只需要很少的配置指令调整。最重要的是将MaxClients设置为一个足够大的数值以处理潜在的请求高峰，同时又不能太大，以致需要使用的内存超出物理内存的大小。

StartServers 5 

//apache服务启动时就启动5个进程 

MinSpareServers 5 

//开启后需要备用的最小进程数 

MaxSpareServers 10 

//服务开启后需要备用的最大进程数 

MaxClients 150 

//允许用户的最大并发数 

MaxRequestsPerChild 0 

//子进程可以处理的最大访问数,0表示可以处理无穷多个 

    worker模式  

使网络服务器支持混合的多线程多进程。.速度比prefork快得多.由于使用线程来处理请求，所以可以处理海量请求，而系统资源的开销小于基于进程的MPM。但是，它也使用了多进程，每个进程又有多个线程，以获得基于进程的MPM的稳定性.和prefork类似的是,他也是由一个单独的控制进程来负责子进程的建立,并事先派生出一些子进程在那里等候,这样客户可以不必等待服务器建立对应的子进程,而马上就可以得到响应和处理.这种worker的MPM工作方式将是未来Apache2的发展趋势.他的两个重要参数是:ThreadsPerChild和MAxClients.前者控制每个子进程运行建立的进程数,后者用来控制允许建立的总线程数.

Worker 由主控制进程生成"StartServers"个子进程，每个子进程中包含固定的ThreadsPerChild线程数，各个线程独立地处理请求。同样，为了不在请求到来时再生成线程，MinSpareThreads和MaxSpareThreads设置了最少和最多的空闲线程数；而MaxClients 设置了同时连入的clients最大总数。如果现有子进程中的线程总数不能满足负载，控制进程将派生新的子进程。MinSpareThreads和 MaxSpareThreads的最大缺省值分别是75和250。这两个参数对Apache的性能影响并不大，可以按照实际情况相应调节。 ThreadsPerChild是worker MPM中与性能相关最密切的指令。ThreadsPerChild的最大缺省值是64，如果负载较大，64也是不够的。这时要显式使用 ThreadLimit指令，它的最大缺省值是20000。Worker模式下所能同时处理的请求总数是由子进程总数乘以ThreadsPerChild 值决定的，应该大于等于MaxClients。如果负载很大，现有的子进程数不能满足时，控制进程会派生新的子进程。默认最大的子进程总数是16，加大时也需要显式声明ServerLimit（最大值是20000）。需要注意的是，如果显式声明了ServerLimit，那么它乘以 ThreadsPerChild的值必须大于等于MaxClients，而且MaxClients必须是ThreadsPerChild的整数倍，否则 Apache将会自动调节到一个相应值。

StartServers 2   

//服务器启动时创建的子进程的数量   

MaxClients 150   

//允许同时伺服的最大接入请求数量,是serverlimint和ThreadsPerChild的乘积   

MinSpareThreads 25   

//允许空闲线程的最小数量   

MaxSpareThreads 75   

//允许空闲线程的最大数量   

ThreadsPerChild 25  

//每个子进程建立的线程数量  

MaxRequestsPerChild /  

/设置每个子进程在生存期间允许伺服的最大请求数量,若为0,表示子进程永远不会结束  

这3种模式做何选择呢?

对我来说,只是一个blog站点而已,不会有太多的访问量,并且希望能够优化系统资源的使用,把apache吃了的mem多要回来点,于是我选择worker的MPM.worker模式消耗资源相对较少,具体优点可以参考以下文章

[http://httpd.apache.org/docs/2.0/misc/perf-tuning.html#compiletime](http://httpd.apache.org/docs/2.0/misc/perf-tuning.html#compiletime)

安装worker模式的MPM

必要知识 1

查看Apache当前的MPM模式

/usr/bin/apache2 -V

找到语句 "-D APACHE_MPM_DIR="server/mpm/prefork" ,由此可见使用的是prefork模式的MPM

必要知识 2

单纯地通过apt-get install apache2-mpm-worker来安装worker模式是可不行的,会删除php5,重新安装php5时会将prefork模式装回

<一> 通过以下方式安装的LAMP包

    sudo apt-get install apache2 libapache2-mod-php5 php5-mysql mysql-server

此方式是安装的MPM模式是prefork

卸载此MPM方法

    sudo apt-get autoremove apache2-mpm-prefork --purge

因为依赖关系,libapache2-mod-php5也会被卸载掉

下面开始Worker安装

第一步:安装apache2-mpm-worker和apache的fastcgi模块libapache-mod-fcid

    sudo apt-get install apache2-mpm-worker libapache2-mod-fcgid

第二步:激活 Fastcgi模块

    sudo a2enmod fcgid

第三步:安装php5

    sudo apt-get install php5-cgi php5-cli

第四步:将下列设置增加到/etc/apache2/httpd.conf或者增加到/etc/apache2/conf.d下的某一个文件中,可以为/etc/apache2/conf.d/00-myconf ("00-" 将保证自己在 /etc/apache2/conf.d 文件夹中是第一个被读取, 这是必须)

    cd /etc/apache/conf.d 

    vi 00-myconf 将下列内容添加并保存退出 

AddHandler fcgid-script .php 

FCGIWrapper /usr/lib/cgi-bin/php5 .php 

Options +ExecCGI 

# If you have Aliases provide php support for them (Here we provide php support for scripts in /usr/share's subdirectories) 

Alias /aptitude /usr/share/doc/aptitude/html/en 

Alias /apt /usr/share/doc/apt-doc 

AddHandler fcgid-script .php 

FCGIWrapper /usr/lib/cgi-bin/php5 .php 

Options ExecCGI FollowSymlinks Indexes

5 . 对于/etc/apache2/sites-available下的虚拟主机配置文件,增加**ExecCGI** 在<Directoy /path-to-site> 块 (添加到你的块中).

    cat /etc/apache2/sites-availabe/default

其中有这样的一段话

AllowOverride All 

Order Allow,Deny 

    allow from all 

添加Options +ExecCGI, 添加后如下 

Options +ExecCGI 

AllowOverride All 

Order Allow,Deny 

    allow from all

6 激活你的站点 

    sudo a2ensite default

7 重启apache服务 

    sudo /etc/init.d/apache2 restart

<二>用这种方式安装的Apache2

    sudo apt-get install apache2

此模式默认安装的worker模式的mpm,所需要做的工作大部分同上,具体不再做阐述了, 

实际总结:采用worker模式后,apache吃mem的现象得到了很大的缓解.系统总mem使用降到了300m左右 

参考资料: 

Hiweed的<Ubuntu Server 最佳方案> 

[http://www.6curl.com/post/21/](http://www.6curl.com/post/21/) 

[http://67054.blog.51cto.com/57054/70439/](http://67054.blog.51cto.com/57054/70439/) 

[http://www.netroby.com/article-823.html](http://www.netroby.com/article-823.html) 

[http://ubuntuforums.org/showthread.php?t=1038416](http://ubuntuforums.org/showthread.php?t=1038416) 

