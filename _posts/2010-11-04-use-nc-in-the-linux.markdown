---
    author: admin
    comments: true
    date: 2010-11-04 14:14:48
    layout: post
    title: linux 下的nc使用
    wordpress_id: 1413
    categories:
- PROGRAM
---

nc是网络界的“瑞士军刀”

nc可以提供如下的网络功能:

1) 监听特定端口,这时候nc就可以作为一个服务器,但是我发现这样使用nc生成的服务器仅仅是一个echo服务器而已,没有其他更加强大的功能.

2) 连接特定端口,这时候nc就成为了一个客户端,同样的,也是一个简单的客户端,只能起echo的作用.

3) 扫描端口,这可以作为查询某个机器上是否开启了某个端口.

几个具体的使用例子

例子1：

使用nc打开linux下的特定端口

    nc -lp 23 & （即telnet）

    netstat -an|grep 23 （查看端口是否正常打开）

例子2：

使用nc进行文件传输，命令

    ssh root@www.freetstar.com "( nc -l 10003 > destination 2>/dev/null & )" && cat source | nc www.freetstar.com 10003

&&前边ssh登录到远程主机www.freetstar.com上，用nc命令打开本地的10003端口,成为后台进程

&&后边，在本地机器上打开source文件，并将其重定向到www.freetstar.com的10003号端口，也就是让远程www.freetstar.com主机10003号端口接收source文件

例子3：

使用nc扫描linux下的特定端口

    nc -v -z host.example.com 70-80

扫描端口(70到80)，可指定范围。-v输出详细信息。

例子4：

克隆硬盘或分区

类似于例子2，只需要由dd获得硬盘或分区的数据，然后传输即可。

克隆硬盘或分区的操作，不应在已经mount的的系统上进行。所以，需要使用安装光盘引导后，进入拯救模式（或使用Knoppix工 具光盘）启动系统后

    server1上执行：# nc -l -p 1234 | dd of=/dev/sda

    server1上执行1234号端口监听，将得到的文件保存到/dev/sda上

    server2上执行：# dd if=/dev/sda | nc server1 1234

例子5：

保存Web页面

    while true; do nc -l -p 80 -q 1 < somepage.html; done

例子6：

模拟HTTP Headers

    [root@hatest1 ~]# nc www.huanxiangwu.com 80

    GET / HTTP/1.1

    Host: ispconfig.org

    Referrer: mypage.com

    User-Agent: my-browser

在nc命令后，输入红色部分的内容，然后按两次回车，即可从对方获得HTTP Headers内容。

例子7：

聊天

    server1上监听1234端口[root@hatest2 tmp]# nc -lp 1234

    server2上向server1的1234端口发送消息[root@hatest1 ~]# nc server1 1234

这样，双方就可以相互交流了。使用Ctrl+D正常退出。

更多的使用，查看man手册

    nc example.host port 打开与example.host主机的port的一个TCP链接.如果链接失败,不显示任何错误信息,仅仅退出

    nc -p 31337 -w 5 example.host 42 打开与example。host主机的42号端口的一个TCP链接。用31337作为源端口,超时链接时间为5秒

    nc -u example.host 53 指定协议为udp协议

参考资料：

http://bloodiron888.blog.163.com/blog/static/164733271201062712226731/

http://www.cnblogs.com/faraway/archive/2008/08/30/1280070.html

http://delalt.blog.51cto.com/652303/135382
