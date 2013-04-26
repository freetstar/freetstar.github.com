---
author: admin
comments: true
date: 2010-08-16 16:52:19
layout: post
title: 小记：Linux下设置ssh免认证登录服务器
wordpress_id: 1142
categories:
- ubuntu
- 软件安装
---

    ssh免认证登录，可以省去输入密码的交互过程，方便实现自动执行一些无需职守程

特以设置本PC登录远程VPS为例

方法如下：

第一步：客户机

//生成密钥对，-t 指明生成密钥类型为rsa ,-P表示设置私钥的密码，设为空，-f设置密钥存放的文件路径

    ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa

//将公钥拷贝到目标服务器上 username是用户，remote-hostname是服务器

    scp ~/.ssh/id_rsa.pub username@remote-hostname:~/temp 

第二步：目标服务器

//新建目录 

    mkdir -p ~/.ssh  

//改变权限

    chmod 700 .ssh  

//相当于重命名公钥位authorized_keys

    cat temp >> ~/.ssh/authorized_keys

//改变权限  

    chmod 600 ~/.ssh/authorized_keys 

//删除临时文件

    rm -rf temp 

注意权限一定要设置

第三步:测试

    ssh username@romote-hostname

