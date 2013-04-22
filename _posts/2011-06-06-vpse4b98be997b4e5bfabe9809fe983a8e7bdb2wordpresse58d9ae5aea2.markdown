---
author: admin
comments: true
date: 2011-06-06 23:11:01
layout: post
slug: vps%e4%b9%8b%e9%97%b4%e5%bf%ab%e9%80%9f%e9%83%a8%e7%bd%b2wordpress%e5%8d%9a%e5%ae%a2
title: vps之间快速部署Wordpress博客
wordpress_id: 1722
categories:
- linux前沿
---

环境:需要将VPS-A上的wordpress镜像至VPS-B,保持一切不变.因为VPS-A使用域名www.freetstar.com 访问wordpress博客,VPS-B要求使用IP访问镜像出来的wordpress博客

VPS-A和VPS-B都采用LAMP环境,本文假设LAMP环境均已假设成功(其实VPS-A为我目前博客所在VPS,VPS-B为准备转移至的VPS)

VPS-A的IP为:﻿﻿184.82.33.230

VPS-B的IP为:202.99.96.12

两个VPS的web路径结构,mysql数据库路径结构一致,web都为/var/www,数据库都为/var/lib/mysql

 第一步:备份VPS-A上的wordpress文件和数据库  

 tar vzvf 06-05-wp.tar.gz /var/www
 
 ##/var/www为wordpress存放的目录
 
 mysqldump -uroot --add-drop-table  -p mysql > bak.mysql
 
 ##VPS-A上wordpress的数据库为mysql,将其导出,注意选项.还可以利用phpmyadmin来导出到本地,具体方法:[here](http://codex.wordpress.org/Backing_Up_Your_Database)
 
 然后scp 06-05-wp.tar.gz bak.mysql root@VPS-B:/var/www,将wordpress的文件和数据库文件拷贝至VPS-B之中

第二步:

 **说明:在第一步中可以看到,我VPS-A上数据库使用的是mysql,当初装wordpress时不懂事,直接使用的mysql-server自带的mysql数据库,冏**
 
 首先在VPS-B上安装wordpress, 非常要注意的是在**1**:wp-config.php里,指定的数据库名为mysql,用户名和密码最好和VPS-A上的一致 **2**:
 
 VPS-B上的wordpress版本必须和VPS-A上的wordpress版本一致.
 
 然后将06-05-wp.tar.gz解压出来覆盖当前的wordpress目录

第三步:

 将VPS-B上的mysql数据库删除之后再重建一个mysql数据库
 
 mysql>drop database mysql;
 
 mysql>show databases;   //查看是否删除成功
 
 mysql>create database mysql;
 
 退出mysql命令行,处理bak.sql,将数据库中的www.freetstar.com都替换为202.99.96.12,即用ip来进行访问,不使用域名
 
 sed -i 's#www.freetstar.com#202.99.96.12#g' bak.sql
 
 然后导入数据到mysql数据库中
 
 mysql -uroot -p mysql <bak.sql

第四步:

已经完成了全部的工作,测试一下

总结一下思路:

 **首先两个VPS环境LAMP环境最好一致,然后在目的VPS上安装好和源VPS一致的wordpress版本,然后用源VPS的wordpress文件覆盖目的VPS的wordpress路径,至于数据库,如果目的**
 
 **VPS的目的数据库不为空,最好删除了再将源VPS的数据库文件导入**

注意事项和一些问题:

1 之前VPS-B使用nginx做web服务时,未成功,提示500 server 错误,error.log提示redirect错误,应该是重定向问题,自己还搞不定,晚上请教下高手.

所以暂时使用lamp环境实验下自己这样做迁移的思路,结果很ok,可以使用ip访问

2  两个VPS之间mysql和php的版本最好不要差太多了,否则容易引起错误
