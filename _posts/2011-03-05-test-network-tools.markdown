---
    author: admin
    comments: true
    date: 2011-03-05 10:31:50
    layout: post
    title: 测试两台server之间的网络情况
    wordpress_id: 1590
    categories:
- 软件安装
---

通常我们想要测试两台服务器之间的网络链接状况时,我们可能使用ftp,scp等协议传输一个文件来估计网络情况,但是由于会涉及到硬盘的转速和CPU的计算能力,所以并不能真正完全的表现出网络状况

下面介绍5个用来测试网络状况的命令

一:IPERF

**基本介绍**

** **

    iperf是NLANR/DAST开发的,用来测试TCP/UDP带宽情况,此命令有一些参数和udp字符.Iperf可以显示网络带宽,延迟抖动,数据亏损

下面介绍测试网络链接情况的几个标准:

* 延迟(响应时间或者RTT):可以用ping来测试 
* 抖动(时延变化):可以通过Iperf 的UDP测试 
* 数据包丢失:可以通过Iperf UDP测试
* 带宽情况可以用TCP测试

    TCP和UDP不同之处在于:TCP会检测每一个包是否都被正确的传送到了目的地,而UDP不会检测数据包,这也使得UDP比TCP更快

    Iperf利用TCP和UDP不同特点来提供网络链接情况

使用方法:

需要有一台server有Iperf允许在某个监听端口上,需要另外一台client机来发送数据消息

例子:

![](http://www.linuxaria.com/wp-content/uploads/2011/01/iperf_labo.gif)

安装:

    sudo apt-get install iperf

基本使用方法:

    server端:

<span style="color: #666666; font-style: italic;">#iperf -s</span>

<span style="color: #666666; font-style: italic;"> </span>
<span style="color: #660033;">------------------------------------------------------------</span>
    Server listening on TCP port <span style="color: #000000;">5001</span>
    TCP window <span style="color: #c20cb9; font-weight: bold;">size</span>: <span style="color: #000000;">8.00</span> KByte <span style="color: #7a0874; font-weight: bold;">(</span>default<span style="color: #7a0874; font-weight: bold;">)</span>
<span style="color: #660033;">------------------------------------------------------------</span>
<span style="color: #7a0874; font-weight: bold;">[</span><span style="color: #000000;">852</span><span style="color: #7a0874; font-weight: bold;">]</span> <span style="color: #7a0874; font-weight: bold;">local</span> 10.1.1.1 port <span style="color: #000000;">5001</span> connected with 10.6.2.5 port <span style="color: #000000;">54355</span>
<span style="color: #7a0874; font-weight: bold;">[</span> ID<span style="color: #7a0874; font-weight: bold;">]</span>   Interval          Transfer        Bandwidth
<span style="color: #7a0874; font-weight: bold;">[</span><span style="color: #000000;">852</span><span style="color: #7a0874; font-weight: bold;">]</span>   <span style="color: #000000;">0.0</span>-<span style="color: #000000;">10.1</span> sec   <span style="color: #000000;">1.15</span> MBytes   <span style="color: #000000;">956</span> Kbits<span style="color: #000000; font-weight: bold;">/</span>sec
<span style="color: #660033;">------------------------------------------------------------</span>
    Client connecting to 10.6.2.5, TCP port <span style="color: #000000;">5001</span>
    TCP window <span style="color: #c20cb9; font-weight: bold;">size</span>: <span style="color: #000000;">8.00</span> KByte <span style="color: #7a0874; font-weight: bold;">(</span>default<span style="color: #7a0874; font-weight: bold;">)</span>
<span style="color: #660033;">------------------------------------------------------------</span>
<span style="color: #7a0874; font-weight: bold;">[</span><span style="color: #000000;">824</span><span style="color: #7a0874; font-weight: bold;">]</span> <span style="color: #7a0874; font-weight: bold;">local</span> 10.1.1.1 port <span style="color: #000000;">1646</span> connected with 10.6.2.5 port <span style="color: #000000;">5001</span>
<span style="color: #7a0874; font-weight: bold;">[</span> ID<span style="color: #7a0874; font-weight: bold;">]</span>   Interval          Transfer        Bandwidth
<span style="color: #7a0874; font-weight: bold;">[</span><span style="color: #000000;">824</span><span style="color: #7a0874; font-weight: bold;">]</span>   <span style="color: #000000;">0.0</span>-<span style="color: #000000;">10.0</span> sec   <span style="color: #000000;">73.3</span> MBytes   <span style="color: #000000;">61.4</span> Mbits<span style="color: #000000; font-weight: bold;">/</span>sec

    client端:

<span style="font-family: Tahoma, Verdana, Arial; line-height: normal; white-space: normal;">

<span style="color: #666666; font-style: italic;">#iperf -c 10.1.1.1 -d</span>

<span style="color: #666666; font-style: italic;"> </span>
<span style="color: #660033;">------------------------------------------------------------</span>
    Server listening on TCP port <span style="color: #000000;">5001</span>
    TCP window <span style="color: #c20cb9; font-weight: bold;">size</span>: <span style="color: #000000;">85.3</span> KByte <span style="color: #7a0874; font-weight: bold;">(</span>default<span style="color: #7a0874; font-weight: bold;">)</span>
<span style="color: #660033;">------------------------------------------------------------</span>
<span style="color: #660033;">------------------------------------------------------------</span>
    Client connecting to 10.1.1.1, TCP port <span style="color: #000000;">5001</span>
    TCP window <span style="color: #c20cb9; font-weight: bold;">size</span>: <span style="color: #000000;">16.0</span> KByte <span style="color: #7a0874; font-weight: bold;">(</span>default<span style="color: #7a0874; font-weight: bold;">)</span>
<span style="color: #660033;">------------------------------------------------------------</span>
<span style="color: #7a0874; font-weight: bold;">[</span> <span style="color: #000000;">5</span><span style="color: #7a0874; font-weight: bold;">]</span> <span style="color: #7a0874; font-weight: bold;">local</span> 10.6.2.5 port <span style="color: #000000;">60270</span> connected with 10.1.1.1 port <span style="color: #000000;">5001</span>
<span style="color: #7a0874; font-weight: bold;">[</span> <span style="color: #000000;">4</span><span style="color: #7a0874; font-weight: bold;">]</span> <span style="color: #7a0874; font-weight: bold;">local</span> 10.6.2.5 port <span style="color: #000000;">5001</span> connected with 10.1.1.1 port <span style="color: #000000;">2643</span>
<span style="color: #7a0874; font-weight: bold;">[</span> <span style="color: #000000;">4</span><span style="color: #7a0874; font-weight: bold;">]</span> <span style="color: #000000;">0.0</span>-<span style="color: #000000;">10.0</span> sec <span style="color: #000000;">76.3</span> MBytes <span style="color: #000000;">63.9</span> Mbits<span style="color: #000000; font-weight: bold;">/</span>sec
<span style="color: #7a0874; font-weight: bold;">[</span> <span style="color: #000000;">5</span><span style="color: #7a0874; font-weight: bold;">]</span> <span style="color: #000000;">0.0</span>-<span style="color: #000000;">10.1</span> sec <span style="color: #000000;">1.55</span> MBytes <span style="color: #000000;">1.29</span> Mbits<span style="color: #000000; font-weight: bold;">/</span>sec

    iperf也能在windows上使用，iperf的主页及更多的参数说明:<a href="http://openmaniak.com/iperf.php">http://openmaniak.com/iperf.php</a>

<span style="color: #ff0000;"><span style="font-size: medium;">二:NETCAT</span></span>

<span style="color: #ff0000;">
</span>

<span style="font-family: monospace;"><span style="line-height: 15px;">基本介绍:
    netcat被称为功能丰富的网络调试和勘探工具.许多linux发行版都自带这一工具
基本使用方法:
一台server机,一台client机
    server端:
    nc -v -v -l -n  2222 >/dev/null
    listening on [any] 2222 ...
    client端:
    time yes|nc -v -v -n 10.1.1.1 2222 >/dev/null
大概10s之后,在client端用Ctrl+C来停止,观察输出
    Client端:
    sent 87478272, rcvd 0

    real 0m9.993s
    user 0m2.075s
    sys 0m0.939s
    Server端:(单位字节)
    sent 0, rcvd 87478392
然后用87478392乘以8,再除以10s即可,得出网速70m/s</span></span>

<span style="font-family: Tahoma, Verdana, Arial; line-height: normal; white-space: normal; color: #110000;">

<span style="font-family: Tahoma, Verdana, Arial; line-height: normal; white-space: normal;">

<span style="font-family: Tahoma, Verdana, Arial; line-height: normal; white-space: normal;">

<span style="font-family: Tahoma, Verdana, Arial; line-height: normal; white-space: normal;">

<span style="color: #000000;">参考:</span><a href="http://deice.daug.net/netcat_speed.html">http://deice.daug.net/netcat_speed.html</a>

<span style="font-size: medium;"><span style="color: #ff0000;">三：Bandwitdth Test Controller（BWCTL）</span></span>

基本介绍：

    BWCTL是个命令行的程序，可以做为daemon运行。可以测试TCP和UDP的性能。

    BWCTL在两个终点上运行，当两个终端都提出测试的请求时，BWCTL开始运行，得出测试数据，分享给两个终端

基本使用方法：

参考官方主页：<a href="http://www.internet2.edu/performance/bwctl/manpages.html">http://www.internet2.edu/performance/bwctl/manpages.html</a>

<span style="color: #ff0000;"><span style="font-size: medium;">四：nuttcp</span></span>

基本介绍：

类似于iperf的工具，可以用来测试tcp和udp

安装：

    sudo apt-get install nuttcp

基本使用方法：

1：

    server端：

    nuttcp -S

    client端：

    nuttcp serverip

2：

还可以测试任意两个站点的网络链接情况

    nuttcp host1 host2

注：man nuttcp获得更多的参数

参考：<a href="http://www.wcisd.hpc.mil/nuttcp/Nuttcp-HOWTO.html">http://www.wcisd.hpc.mil/nuttcp/Nuttcp-HOWTO.html</a>

<span style="color: #ff0000;"><span style="font-size: medium;">五：thrulay</span></span>

<span style="font-family: Tahoma, Verdana, Arial; line-height: normal; white-space: normal;">基本介绍：</span>

<span style="font-family: Tahoma, Verdana, Arial; line-height: normal; white-space: normal;">检测网络的负载情况，延时等其他网络性能，对于tcp和udp都有很好的检测，有易读的输出结果</span>

<span style="font-family: Tahoma, Verdana, Arial; line-height: normal; white-space: normal;">参考：</span><a href="http://e2epi.internet2.edu/thrulay/thrulayd.man.html">http://e2epi.internet2.edu/thrulay/thrulayd.man.html</a>

个人觉得thrulay，iperf需要好好研究下

 

