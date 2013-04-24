---
    author: admin
    comments: true
    date: 2010-10-27 15:49:20
    layout: post
    slug: redhat-as4u8-install-apache-tomcat
    title: Redhat AS4U8下apache和tomcat安装及整合小记
    wordpress_id: 1373
    categories:
- 服务器
---

准备工作：将所有需要的配置文件和软件copy到install目录

[lgx@oracle install]$

    pwd      #当前路径，安装包所在路径
    /usr/local/install

[lgx@oracle install]$

    ls         #列出安装软件包及其版本
    apache-tomcat-6.0.26.zip  httpd-2.2.15.tar.gz   jdk-6u20-linux-i586.bin
    mod_jk-1.2.28-httpd-2.2.X.so//注意整合模块与apache版本的匹配

### 一  建立user1用户  #以后用user1身份来启动tomcat

1  建立程序运行账号

    useradd  -d  /home/user1  -u 800  user1
    passwd  user1

    user1  属主目录 /home/user1   UID 800  GID800

2  改变/home/user1的属主

    chown  user1:user1  -R  /home/user1

### 二  安装apache服务器

1  切换到user1用户

    su – user1

2  安装文件解压

    tar  zxvf  httpd-2.2.15.tar.gz

3  进入解压后目录

[user1@oracle install]$cd httpd-2.2.15

4  编译安装

[user1@oracle httpd-2.2.15]$./configure –prefix=/home/user1/apache2.2.15 –enable-so  –enable-mods-shared=all

[user1@oracle httpd-2.2.15]$ make

[user1@oracle httpd-2.2.15]$ make install

### 三 安装JDK

1 进入/usr/local/install目录

[user1@oracle install]$ sh jdk-6u20-linux-i586.bin

一直点击回车，然后输入yes，再回车，等待安装完成，出现如下信息说明安装成功

Product and system data will be collected. If your configuration

    supports a browser, the Sun Product Registration form for

    the JDK will be presented. If you do not register, none of

    this information will be saved. You may also register your

JDK later by opening the register.html file (located in

    the JDK installation directory) in a browser.

For more information on what data Registration collects and

    how it is managed and used, see:

    http://java.sun.com/javase/registration/JDKRegistrationPrivacy.html

Press Enter to continue…..

2 移动jdk的目录到目标目录

[user1@oracle install]$ mv jdk 1.6.0_20/ /home/user1/jdk

3 设置user1用户的环境变量

[user1@oracle jdk]$ cd ~

[user1@oracle ~]$ vi .bash_profile

在.bash_profile文件中添加如下的变量信息

    export JAVA_HOME=/home/user1/jdk
    export CLASSPATH=$CLASSPATH:$JAVA_HOME/lib:$JAVA_HOME/jre/lib
    export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH:$HOMR/bin
    export JRE_HOME=/home/user1/jdk

4  测试一下

[user1@oracle bin]$ java -version

    java -version 1.6.0_20
    Java(TM) SE Runtime Environment (build 1.6.0_20-b02)
    Java HotSpot(TM) Client VM (build 16.3-b01, mixed mode, sharing)

出现上述信息说明，安装成功

### 四 安装tomcat

1进入6.0.266.0.26.zip

这时在/usr/local/install目录下会产生apache-tomcat-6.0.26目录

2 生成tomcat目录

[user1@oracle install]$ mv apache-tomcat-6.0.26 /home/user1/tomcat6

3 设置用户的变量

    vi .bash_profile
    export CATALINA_HOME=/home/user1/tomcat6
    export CATALINA_BASE=/home/user1/tomcat6

4

    source ～/.bash_profile

### 五 启动apache和tomcat

1 启动apache

切换到root，及apache目录中

[root@oracle bin]# ./apachectl -k start

2 以user1用户身份启动tomcat

    [user1@oracle bin]$ ./startup.sh
    Using CATALINA_BASE:   /home/user1/tomcat6
    Using CATALINA_HOME:  /home/user1/tomcat6
    Using CATALINA_TMPDIR: /home/user1/tomcat6/temp
    Using JRE_HOME:        /home/user1/jdk
    Using CLASSPATH:     /home/user1/tomcat6/bin/bootstrap.jar

3 打开浏览器测试一下是否成功

    apache 打开浏览器输入http://localhost,显示It works!!!则成功

Tomcat 打开浏览器输入http:/localhost:8080 显示大猫则成功

### 六 整合apache和tomcat

1 jk模块支持，进入install目录

Mv mod_jk-1.2.28-httpd-2.2.X.so /home/user1/apache2.2.15/modules/mod_jk-1.2.28.so

2 在apache的conf文件夹下建立workers.properties文件，内容如下

    worker.list=portal_worker
    worker.portal_worker.port=8009
    worker.portal_worker.host=localhost
    worker.portal_worker.type=ajp13
    worker.portal_worker.lbfactor=1
    worker.loadbalancer.type=lb
    worker.loadbalancer.balance_workers=portal_worker

3 编辑apache的httpd.conf文件

在加载模块处添加

    LoadModule jk_module modules/mod_jk-1.2.28.so

然后在文件末尾添加如下内容

    JkWorkersFile   conf/workers.properties
    JkShmFile       logs/mod_jk.shm
    JkLogFile       logs/mod_jk.log
    JkLogLevel      error
    JkMount /ProxoolAdmin.svl portal_worker
    JkMount /fckeditor/editor/filemanager/connectors/* portal_worker
    JkMount /CheckCode.svl portal_worker
    JkMount /*.do portal_worker
    JkMount /*.htm portal_worker
    JkMount /*.jsp portal_worker
    JkMount /*.jspa portal_worker
    JkMount /*.jspx portal_worker
    JkMount /*.php portal_worker
    JkMount /*.asp portal_worker

4 检查tomcat 的server.xml文件，在context修改网站目录，使其与apache的DocumentRoot一致

将context区域修改成<docBase="/home/user1/apache2.2.15/htdocs"

5 测试是否整合成功

在apache的htdocs目录下新建一个showtime.jsp文件

具体内容如下：

    <%@page language="java" import="java.util.*"%>

    Now Time is : <% out.println(new Date()); %>

打开浏览器输入：http://localhost:8080  大猫出现，ok，tomcat运行正常

打开浏览器输入：http://localhost/showtime.jsp出现时间，整合成功

六 ：本人新手，本文档也不是原文档，是自己总结的，可能会有错误，仅供参考
