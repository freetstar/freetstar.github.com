---
comments: true
date: 2010-12-08 21:50:53
layout: post
slug: 50-top-frequently-used-unixlinux-commands-2
title: 50个最常用的unix/linux命令
wordpress_id: 1524
categories:
- PROGRAM
---

26. kill 
 kill 用来终止一个进程。首先，用ps -ef查找进程ID，然后用kill -9来杀掉这个进程。你还可以运用killall，pkill，xkill来杀掉一个unix进程
[code language="bash"]$ ps -ef | grep vim
ramesh    7243  7222  9 22:43 pts/2    00:00:00 vim[/code]
[code language="bash"]$ kill -9 7243[/code]
更多的例子: [4 Ways to Kill a Process – kill, killall, pkill, xkill](http://www.thegeekstuff.com/2009/12/4-ways-to-kill-a-process-kill-killall-pkill-xkill/)
27. rm 
在删除文件前提示
[code language="bash"]$ rm -i filename.txt[/code]
可以在文件名参数中使用通配符
交互删除所有的file开头的文件
[code language="bash"]$ rm -i file*[/code]
删除example文件夹本身以及其下文件夹
[code language="bash"]$ rm -r example[/code]
28. cp 
将file1复制至file2,同时保存文件的修改时间和权限
[code language="bash"]$ cp -p file1 file2[/code]
将file1复制至file2,如果file2存在提示是否覆盖
[code language="bash"]$ cp -i file1 file2[/code]
29. mv 
将 file1 重命名为 file2. 如果file2存在，则提示是否覆盖
[code language="bash"]$ mv -i file1 file2[/code]
mv -f 和mv -i相反，强制覆盖
mv -v 则显示详细信息。通常在使用shell的通配符时非常有用
[code language="bash"]$ mv -v file1 file2[/code]
30. cat 
可以同时显示许多文件。file1之后输出file2的内容
[code language="bash"]$ cat file1 file2[/code]
cat -n 选项会在每个输出行上加上行号
[code language="bash"]$ cat -n /etc/logrotate.conf
    1   /var/log/btmp {
    2       missingok
    3       monthly
    4       create 0660 root utmp
    5       rotate 1
    6   }[/code]
31. mount 
在挂载之前，先创建一个目录
[code language="bash"]# mkdir /u01
# mount /dev/sdb1 /u01[/code]
写到fstab中以实现自动挂载 
[code language="bash"]/dev/sdb1 /u01 ext2 defaults 0 2[/code]
32. chmod 
chmod 用来改变文件和文件夹的权限
给于文件所属主和属组所有权限
[code language="bash"]$ chmod ug+rwx file.txt[/code]
删除文件所属组的一切权限
[code language="bash"]$ chmod g-rwx file.txt[/code]
将文件权限递归的赋予子目录下的所有文件
[code language="bash"]$ chmod -R ug+rwx file.txt[/code]
更多的例子: [7 Chmod Command Examples for Beginners](http://www.thegeekstuff.com/2010/06/chmod-command-examples/)
33. chown 
chown 用来改变文件的属主和属组
将文件的属主变为oracle，属组变为db
[code language="bash"]$ chown oracle:dba dbora.sh[/code]
-R用来递归
[code language="bash"]$ chown -R oracle:dba /home/oracle[/code]
34. passwd 
用来修改配置用户的密码
[code language="bash"]$ passwd[/code]
root用户可以用passwd来修改其他用户的密码
[code language="bash"]# passwd USERNAME[/code]
移除某个用户的密码,一旦密码被移除,用户可以无密码登录
[code language="bash"]# passwd -d USERNAME[/code]
35. mkdir 
在主目录下创建一个temp目录
[code language="bash"]$ mkdir ~/temp[/code]
创建一个多层的目录.如果相应的目录不存在,则创建.
[code language="bash"]$ mkdir -p dir1/dir2/dir3/dir4/[/code]
36. ifconfig 
查看和编辑网络链接.
查看所有网络链接情况
[code language="bash"]$ ifconfig -a[/code]
激活和停止某个网卡
[code language="bash"]$ ifconfig eth0 up[/code]
$ ifconfig eth0 down
更多的例子: [Ifconfig: 7 Examples To Configure Network Interface](http://www.thegeekstuff.com/2009/03/ifconfig-7-examples-to-configure-network-interface/)
37. uname 
Uname 列出系统的重要信息,,比如:— 内核名,主机名,内核版本 ,cpu类型等等
以ubuntu系统为例
[code language="bash"]$ uname -a
Linux john-laptop 2.6.32-24-generic #41-Ubuntu SMP Thu Aug 19 01:12:52 UTC 2010 i686 GNU/Linux[/code]
38. whereis 
查找某个unix所在的地方(例如ls命令在哪里)
[code language="bash"]$ whereis ls
ls: /bin/ls /usr/share/man/man1/ls.1.gz /usr/share/man/man1p/ls.1p.gz[/code]
你可以使用-B参数来替代whereis默认寻找的路径.在/tmp下寻找可执行文件lsmk并显示出来
[code language="bash"]$ whereis -u -B /tmp -f lsmk
lsmk: /tmp/lsmk[/code]
39. whatis 
Whatis 显示一行有关某个命令的描述
[code language="bash"]$ whatis ls
ls              (1)  - list directory contents
[/code]
[code language="bash"]$ whatis ifconfig
ifconfig (8)         - configure a network interface[/code]
40. locate c
用locate命令快速的查找某个文件,或者许多文件.用updatedb命令创建locate寻找时使用的数据库
下列例子显示系统中包含单词crontab的文件
[code language="bash"]$ locate crontab
/etc/anacrontab
/etc/crontab
/usr/bin/crontab
/usr/share/doc/cron/examples/crontab2english.pl.gz
/usr/share/man/man1/crontab.1.gz
/usr/share/man/man5/anacrontab.5.gz
/usr/share/man/man5/crontab.5.gz
/usr/share/vim/vim72/syntax/crontab.vim[/code]
41. man 
显示特定命令的man手册
[code language="bash"]$ man crontab[/code]
当一个命令的man手册有许多部分时,你可以指定读取特定部分]
[code language="bash"]$ man SECTION-NUMBER commandname[/code]
man手册的8个部分
1、Standard commands （标准命令）
2、System calls （系统调用）
3、Library functions （库函数）
4、Special devices （设备说明）
5、File formats （文件格式）
6、Games and toys （游戏和娱乐）
7、Miscellaneous （杂项）
8、Administrative Commands （管理员命令）
比如说, 输入whatis crontab,会发现有2部分,1和5,查看5部分的man手册 
[code language="bash"]$ whatis crontab
crontab (1)          - maintain crontab files for individual users (V3)
crontab (5)          - tables for driving cron
$ man 5 crontab[/code]
42. tail 
输出一个文件的最后10行
[code language="bash"]$ tail filename.txt[/code]
显示filename.txt的最后N行
[code language="bash"]$ tail -n N filename.txt[/code]
查看文件的实时状态tail -f. 此命令通常用来查看持续增长的log文件, 可用Ctrl-C中断
[code language="bash"]$ tail -f log-file[/code]
更多的例子: [3 Methods To View tail -f output of Multiple Log Files in One Terminal](http://www.thegeekstuff.com/2009/09/multitail-to-view-tail-f-output-of-multiple-log-files-in-one-terminal/)
43. less 
less 在查看大型日志文件时非常有效, 他不需要在完全打开文件的情况下查看文件内容
[code language="bash"]$ less huge-log-file.log[/code]
当使用less命令打开文件时,下边这两个快捷键非常有用
[code language="bash"]CTRL+F – forward one window[/code]
CTRL+B – backward one window
更多的例子[ Unix Less Command: 10 Tips for Effective Navigation](http://www.thegeekstuff.com/2010/02/unix-less-command-10-tips-for-effective-navigation/)
44. su 
切换到另外一个用户,超级用户可以切换到任意用户而不输入密码
[code language="bash"]$ su - USERNAME[/code]
仅仅以另外一个用户执行一次特定命令,以下例子中,john以raj的身份执行ls命令.执行之后马上回复john用户身份
[code language="bash"][john@dev-server]$ su - raj -c 'ls'[/code]

[john@dev-server]$
登录某个特定用户,同时指定使用某个shell
[code language="bash"]$ su -s 'SHELLNAME' USERNAME[/code]
45. mysql 
mysql 可能是linux系统上最广泛使用的开源数据库了,尽管你在自己的服务器上没有使用mysql数据库,但是你实际上可能是一个mysql的终端用户,使用mysql命令链接远程数据库
链接远程数据库,通常会提示输入密码
[code language="bash"]$ mysql -u root -p -h 192.168.1.2[/code]
链接本地mysql数据库
[code language="bash"]$ mysql -u root -p[/code]
如果你想指定mysql的root密码,在-p之后输入,记住!不要留任何空白,紧跟着输入
46. yum 
安装apache服务器
[code language="bash"]$ yum install httpd[/code]
升级apache服务器
[code language="bash"]$ yum update httpd[/code]
写在apache服务器.
[code language="bash"]$ yum remove httpd[/code]
47. rpm 
安装apache
[code language="bash"]# rpm -ivh httpd-2.2.3-22.0.1.el5.i386.rpm[/code]
升级apache
[code language="bash"]# rpm -uvh httpd-2.2.3-22.0.1.el5.i386.rpm[/code]
移除apache
[code language="bash"]# rpm -ev httpd[/code]
更多的例子: [RPM Command: 15 Examples to Install, Uninstall, Upgrade, Query RPM Packages](http://www.thegeekstuff.com/2010/07/rpm-command-examples/)
48. ping 
Ping远程主机,ping5次
[code language="bash"]$ ping -c 5 gmail.com[/code]
更多的例子:[ Ping Tutorial: 15 Effective Ping Command Examples](http://www.thegeekstuff.com/2009/11/ping-tutorial-13-effective-ping-command-examples/)
49. date 
设置系统时间
[code language="bash"]# date -s "01/31/2010 23:59:53"[/code]
一旦你改变了系统时间,你需要将系统时间和硬件时间同步更新
[code language="bash"]# hwclock –systohc
# hwclock --systohc –utc[/code]
50. wget 
快捷有效地下载软件,音乐,视频的wget命令
[code language="bash"]$ wget http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-3.2.1.tar.gz[/code]
下载,但是起另外一个名字
[code language="bash"]$ wget -O taglist.zip http://www.vim.org/scripts/download_script.php?src_id=7701[/code]
更多额例子 [The Ultimate Wget Download Guide With 15 Awesome Examples](http://www.thegeekstuff.com/2009/09/the-ultimate-wget-download-guide-with-15-awesome-examples/)
