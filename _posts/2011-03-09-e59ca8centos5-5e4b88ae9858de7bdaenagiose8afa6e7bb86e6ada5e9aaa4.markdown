---
author: admin
comments: true
date: 2011-03-09 20:50:09
layout: post
slug: '%e5%9c%a8centos5-5%e4%b8%8a%e9%85%8d%e7%bd%aenagios%e8%af%a6%e7%bb%86%e6%ad%a5%e9%aa%a4'
title: 在centos5.5上配置nagios详细步骤
wordpress_id: 1627
categories:
- 服务器
---

本文环境
 
 cat /etc/issue 操作系统为Centos release 5.5(Final)
 
 uname -a       位数为64位
 
 本文假设安装配置时用户是root

第一步：安装必要的环境
	
  * yum install httpd php5        //apache和php5
	
  * yum install gcc glibc glibc-common //gcc 编译器
	
  * yum install gd dg-devel      //GD开发库
	
  * yum install mysql-devel.x86_64 //安装64位的mysql工具包

第二步：配置必要的用户
	
  * useradd -m nagios     //增加nagios用户
	
  * passwd  nagios        //设置nagios用户的密码，恩，你应该懂的
	
  * groupadd nagcmd       //新增一个nagcmd用户组，以允许外部命令能够通web界面提交
	
  * usermod -a -G nagcmd nagios
	
  * usermod -a -G nagcmd apache //把apache运行用户加到nagcmd,这里是apache,当然你可以用其他名字，比如说nobody

第三步：下载必要的包包
	
  * #pwd
	
  * /root
	
  * mkdir ~/downloads
	
  * cd downloads
	
  * wget http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-3.2.3.tar.gz
	
  * wget http://prdownloads.sourceforge.net/sourceforge/nagiosplug/nagios-plugins-1.4.15.tar.gz

第四步：编译安装
	
  * tar zxvf nagios-3.2.3.tar.gz
	
  * cd nagios-3.2.3
	
  * ./configure --prefix=/usr/local/nagios --with-command-group=nagcmd
	
  * //注，我当时没有选择--prefix=/usr/local/nagios 这个选项，默认就是安装这个在这个路径的，谁知到第一次装完/usr/local/nagiso下缺少了bin和sbin文件夹，后来加上来就好了../configure --help明明说默认安装在/usr/local/nagios下的
	
  * make all
	
  * make install
	
  * make install-init
	
  * make install-config
	
  * make install-commandmode //这么多make,nagios别听着是难够死，其实还是比较贴心的

第五步：修改一个邮件通知的地方
	
  * vi /usr/local/nagios/etc/objects/contacts.cfg
	
  * 在第一个define块那里，把邮箱换成自己的邮件，这个比较好找，不多说了，比如说换成我的lgxwqq[@]gmail.com

第六步：配置nagios的对应的apache配置文件
	
  * make install-webconf //将会在apache的ServerRoot下的conf.d文件下生成nagios.conf文件，网上有很多手动添加的例子，其实不用。当然如果你用的是nginx之类的，可能需要手动添加
	
  * htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin //配置登录http://ServerIP/nagios/时要输入的密码，即nagiosadmin是登录名,密码就是你刚才输入的
	
  * 重启web服务
	
  * service httpd restart
	
  * 当然，这只是单纯的用用户名和口令去验证，并不非常安全，如果你有兴趣的话可以阅读：[here](http://nagios.sourceforge.net/docs/3_0/cgisecurity.html)，进行进一步的配置

第七步：编译安装插件
	
  * #pwd
	
  * /root
	
  * cd ~/downloads
	
  * tar zxvf nagios-plugins-1.4.15.tar.gz
	
  * cd nagiso-plugins
	
  * ./configure --with-nagios-user=nagios --with-nagios--group=nagios
	
  * make
	
  * make install //注意这里要确保mysql-devel安装，否则无法产生这个check_mysql插件

第八步：开启nagios
	
  * chkconfig --add nagios
	
  * chkconfig nagios on
	
  * 测试nagios的配置文件是否有误
	
  * /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
	
  * 提示
	
  * Total Warnings: 0
	
  * Total Errors:   0
	
  * 则表明无误，这一步测试配置文件的步骤也是我们每次修改完配置文件要做的事情
	
  * service nagios start

第九步：停止selinux或者配置selinux
	
  * 暂且设置SELinux为被动模式
	
  * setenforce 0
	
  * 或者永久停止SELinux
	
  * vi /etc/selinux/config
	
  * 设置为SELINUX=disabled
	
  * 或者选择不停止SELinux.这样配置CGIS
	
  * chcon -R -t httpd_sys_content_t /usr/local/nagios/sbin/
	
  * chcon -R -t httpd_sys_content_t /usr/local/nagios/share/

第十步：测试登录
	
  * http://ServerIP/nagios/
	
  * 提示用户名和密码，即第六步的东西
	
  * 成功后的界面
	
  * 

![](http://i.imgur.com/BQwea.png)

这样nagios的基本已经配置完毕，发觉网上有的文章比较老，还是推荐阅读官方的安装手册

[http://nagios.sourceforge.net/docs/3_0/quickstart-fedora.html](http://nagios.sourceforge.net/docs/3_0/quickstart-fedora.html)

