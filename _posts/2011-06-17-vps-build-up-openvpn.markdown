---
    author: admin
    comments: true
    date: 2011-06-17 01:05:47
    layout: post
    slug: vps-build-up-openvpn
    title: VPS搭建OpenVPN教程
    wordpress_id: 1733
    categories:
- 服务器
---

此文用于技术实验,请勿用于"非法"目的,留言时谢谢"配合",

我尽量在文章中详细解释每一步,自己对网络的知识也是通过G##F##W##建立起来的,有的地方不对,望指正,如果有更多的网络知识疑问,call[@Jasey_Wang](http://jaseywang.info/)(网络信息安全党) [＠ihipop](http://ihipop.info/)(VPN老手)

实验环境:

    VPN server:米国VPS(网通链接速度比较快),OS:ubuntu server 10.10

    VPN Client:本机,国内的一个PC,OS:ubuntu desktop 10.10

整体思路:

在服务器端安装和配置好openvpn,生成服务器端和客户端的证书和认证密钥,同时配置好服务器端的网络情况,设置允许数据包转发,将客户端的证书下方到客户端电脑上,同时客户端电脑安装openvpn,修改必要的配置文件,去链接远程的vpn服务器

**第一步:布置VPN server端**

1)更新VPS 自身软件至最新

#apt-get update
#apt-get upgrade --upgrade

2)安装Openvpn及其依赖udev

#apt-get install openvpn udev

    OpenVPN提供了"easy-rsa"这套加密方面的工具,openvpn安装好之后,easy-rsa在/usr/share/doc/openvpn/examples/easy-rsa/文件夹中,为了使OpenVPN正常工作,需要把easy-rsa复制到/etc/openvpn中.运行下列命令:

#cp -R /usr/share/doc/openvpn/examples/easy-rsa/ /etc/openvpn

接下来我们大部分的配置工作都在/etc/openvpn/easy-rsa/2.0/中进行,因为大部分OpenVPN配置都在这个文件夹中

3)配置必要的公钥配置文件,修改一些变量值来方便以后配置公钥和运行脚本

#vim /etc/openvpn/easy-rsa/2.0/vars
    export KEY_PROVINCE="CA"
    export KEY_CITY="﻿SanFrancisco"
    export KEY_ORG="freetstar"
    export KEY_EMAIL="lgxwqq@gmail.com"

    export KEY_COUNTRY="US"﻿

##比较关键的是KEY_EMAIL这个变量,最好写成自己的邮箱

4)初始化公钥基础设施,也就是依次运行下面这些脚本

    cd /etc/openvpn/easy-rsa/2.0/
. /etc/openvpn/easy-rsa/2.0/vars       //初始化一些变量信息
. /etc/openvpn/easy-rsa/2.0/clean-all  //用来清除以前产生的证书和密钥等
. /etc/openvpn/easy-rsa/2.0/build-ca   //生成新的ca

每一步回车即可

5)产生私钥,为OpenVPN server创建私钥

. /etc/openvpn/easy-rsa/2.0/build-key-server server

    challenge password和company names这两项回车即可,接下来几项可能用y来回答,注意问题提示

6)为Client即freetstar创建证书,这里freetstar应该替换为你的对应ID,

. /etc/openvpn/easy-rsa/2.0/build-key freetstar

7)创建Diffie Hellman参数,此参数用来管理OpenVPN密钥交流和认证

. /etc/openvpn/easy-rsa/2.0/build-dh

8)将创建好的ca.crt和freetstar.crt,freetstar.key拷贝至Client端

    scp ca.crt freetstar.crt freetstar.key freetstar@﻿﻿60.25.201.209:

#注,60.*是我Client本机的公网ip地址,推荐用scp这些加密的工具进行传输,因为安全性要高

9)将必要的证书和密钥拷贝至/etc/openvpn文件下,这样OpenVPN才能识别必要的证书和密钥

    cd /etc/openvpn/easy-rsa/2.0/keys
    cp ca.crt ca.key dh1024.pem server.crt server.key /etc/openvpn

10)配置/etc/openvpn/server.conf文件,这个配置文件本身不存在,需要从模板中获取,同时修改必要的server.conf配置文件

    cd /usr/share/doc/openvpn/examples/sample-config-files gunzip -d server.conf.gz cp server.conf /etc/openvpn/ vim /etc/openvpn/server.conf   push "redirect-gateway def1"  //找到此行并修改,让client使用OpenVPN server作为默认网关 11)将client.conf配置文件拷贝至Client端

    cd /usr/share/doc/openvpn/examples/sample-config-files
    scp client.conf freetstar@﻿﻿60.25.201.209:

12)配置Server端的网络,设置永久打开路由转发功能

#vim /etc/sysctl.conf

    net.ipv4.ip_forward=1

目前先暂时打开路由转发

    echo 1 > /proc/sys/net/ipv4/ip_forward

配置Iptables

    iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
    iptables -A FORWARD -s 10.8.0.0/24 -j ACCEPT
    iptables -A FORWARD -j REJECT
    iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE  //设置数据转发,10.8.0.0/24是虚拟网卡网段 eth0是实际网卡

    VPS采用了xen虚拟,故是eth0,如果vps采用了openvz虚拟化,此处应该修改为venet0

运行

    iptabels-save //保存iptables规则
<span style="font-family: Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif; line-height: 19px; white-space: normal;">13)安装<tt>dnsmasq,所有client的dns请求也通过VPN</tt></span>

#apt-get install dnsmasq
#vim /etc/openvpn/server.conf
修改为push "dhcp-option DNS 10.8.0.1"

14)测试,正常情况下应该出现tun0这个虚拟网卡

#/etc/init.d/openvpn start

#ifconfig

    tun0      Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00

    inet addr:10.8.0.1  P-t-P:10.8.0.2  Mask:255.255.255.255

    UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1500  Metric:1

    RX packets:2762 errors:0 dropped:0 overruns:0 frame:0

    TX packets:2920 errors:0 dropped:0 overruns:0 carrier:0

    collisions:0 txqueuelen:100

    RX bytes:520504 (520.5 KB)  TX bytes:1035346 (1.0 MB)

**第二步:配置Client端**

1)安装openvpn

    sudo apt-get install openvpn

2)将之前下载到client端的文件,拷贝至/etc/openvpn文件中

    sudo cp ca.crt freetstar.crt freetstar.key client.conf /etc/openvpn

3)编辑client.conf,配置远程VPN的ip地址,本地证书和公钥

    sudo vim /etc/openvpn/client.conf
    remote remoteIP 1194  //注,remoteIP改成OpenVPN Server的ip,也就是VPS的IP地址
    ca ca.crt
    cert freetstar.crt   
    key freetstar.key  

4)开启OpenVPN客户端

    sudo /etc/init.d/openvpn start

5)通过[http://formyip.com/](http://formyip.com/)检测自己的ip地址是否已经变更为OpenVPN server IP地址

6)尽情享受吧

备注

1:首先需要VPS支持搭建OpenVPN,一般是通过tun来获取支持的

2:肯定会在配置过程中出现各种问题, 可以参考p哥的解决办法,非常详尽

3:以debug模式来调试vpn

<span style="color: #222222; font-family: monospace; line-height: 21px; white-space: pre;">openvpn <span style="background-image: initial; background-attachment: initial; background-origin: initial; background-clip: initial; background-color: transparent; vertical-align: baseline; color: #000000; font-weight: bold; background-position: initial initial; background-repeat: initial initial; padding: 0px; margin: 0px; border: 0px initial initial;">/</span>etc<span style="background-image: initial; background-attachment: initial; background-origin: initial; background-clip: initial; background-color: transparent; vertical-align: baseline; color: #000000; font-weight: bold; background-position: initial initial; background-repeat: initial initial; padding: 0px; margin: 0px; border: 0px initial initial;">/</span>openvpn<span style="background-image: initial; background-attachment: initial; background-origin: initial; background-clip: initial; background-color: transparent; vertical-align: baseline; color: #000000; font-weight: bold; background-position: initial initial; background-repeat: initial initial; padding: 0px; margin: 0px; border: 0px initial initial;">/</span>server.conf</span>

参考文档:

[http://library.linode.com/networking/openvpn/ubuntu-10.04-lucid#sph_id2](http://library.linode.com/networking/openvpn/ubuntu-10.04-lucid#sph_id2)

[https://www.deleak.com/blog/2010/06/04/openvpn-on-vps/](https://www.deleak.com/blog/2010/06/04/openvpn-on-vps/)

[http://pityonline.info/?p=1054](http://pityonline.info/?p=1054)
