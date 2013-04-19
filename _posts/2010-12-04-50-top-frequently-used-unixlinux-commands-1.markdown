---
author: admin
comments: true
date: 2010-12-04 11:26:39
layout: post
slug: 50-top-frequently-used-unixlinux-commands-1
title: 50个最常用的unix/linux命令
wordpress_id: 1507
categories:
- PROGRAM
---

             本文以例子的方式列出了在linux/unix中最常用的50个命令，同时，本文可能不会非常详细地介绍每个命令，只是给出一些基本介绍。   
1. tar 
创建一个tar包 
[code language="bash"]$ tar cvf archive_name.tar dirname/ [/code]
解压tar包 
[code language="bash"]$ tar xvf archive_name.tar [/code]
查看tar包中有哪些文件 
[code language="bash"]$ tar tvf archive_name.tar [/code]
更多的例子[ The Ultimate Tar Command Tutorial with 10 Practical Examples ](http://www.thegeekstuff.com/2010/04/unix-tar-command-examples/)
2. grep 
在文件中查找特定字符串（大小写敏感） 
[code language="bash"]$ grep -i "the" demo_file [/code]
打印匹配的行，同时输出其后的3行 
[code language="bash"]$ grep -A 3 -i "example" demo_text [/code]
递归的查找 
[code language="bash"]$ grep -r "ramesh" * 
更多的例子: <a href="http://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/">Get a Grip on the Grep! – 15 Practical Grep Command Examples </a>
3. find 
用名字来查找文件（大小写敏感） 
[code language=bash]# find -iname "MyCProgram.c" [/code]
对查找出来的文件执行命令 
[code language="bash"]$ find -iname "MyCProgram.c" -exec md5sum {} \; [/code]
查找$HOME文件下的的空文件 
[code language="bash"]# find ~ -empty [/code]
更多的例子：[ Mommy, I found it! — 15 Practical Linux Find Command Examples](http://www.thegeekstuff.com/2009/03/15-practical-linux-find-command-examples/) 
4. ssh 
登录到远程主机 
[code language="bash"]ssh -l jsmith remotehost.example.com [/code]
调试ssh客户端（显示更多的信息） 
[code language="bash"]ssh -v -l jsmith remotehost.example.com [/code]
显示ssh版本 
$ ssh -V 
[code language="bash"]OpenSSH_3.9p1, OpenSSL 0.9.7a Feb 19 2003 [/code]
更多的例子: [5 Basic Linux SSH Client Commands ](http://www.thegeekstuff.com/2008/05/5-basic-linux-ssh-client-commands/)
5. sed 
当你从嗯windows拷贝文件到unix时，你会发现在每行末尾有”\r\n”，本例子将dos的文件格式转换为unix文件格式 
[code language="bash"]$sed 's/.$//' filename [/code]
反向输出文件内容 
[code language="bash"]$ sed -n '1!G;h;$p' thegeekstuff.txt [/code]
为文件中的所有非空行添加行号 
[code language="bash"]$ sed '/./=' thegeekstuff.txt | sed 'N; s/\n/ /' [/code]
更多的例子:[ Advanced Sed Substitution Examples](http://www.thegeekstuff.com/2009/10/unix-sed-tutorial-advanced-sed-substitution-examples/) 
6. awk 
删除重复行 
[code language="bash"]$ awk '!($0 in array) { array[$0]; print }' temp [/code]
输出/etc/passwd中所有uid gid相同的行 
[code language="bash"]$awk -F ':' '$3==$4' passwd.txt [/code]
输出文件的某些域 
[code language="bash"]$ awk '{print $2,$5;}' employee.txt [/code]
更多的例子 [8 Powerful Awk Built-in Variables – FS, OFS, RS, ORS, NR, NF, FILENAME, FNR](http://www.thegeekstuff.com/2010/01/8-powerful-awk-built-in-variables-fs-ofs-rs-ors-nr-nf-filename-fnr/) 
7. vim 
编辑文件的143行 
[code language="bash"]$ vim +143 filename.txt [/code]
进入匹配到的第一行 
[code language="bash"]$ vim +/search-term filename.txt [/code]
以只读方式打开文件 
[code language="bash"]$ vim -R /etc/passwd [/code]
更多的例子:[ How To Record and Play in Vim Editor ](http://www.thegeekstuff.com/2009/01/vi-and-vim-macro-tutorial-how-to-record-and-play/)
8. diff 
比较的时候忽略空白行 
[code language="bash"]# diff -w name_list.txt name_list_new.txt 
2c2,3 
< John Doe --- > John M Doe 
> Jason Bourne [/code]
更多的例子 [Top 4 File Difference Tools on UNIX / Linux – Diff, Colordiff, Wdiff, Vimdiff ](http://www.thegeekstuff.com/2010/06/linux-file-diff-utilities/)
9. sort command examples 
以升序排列文件 
[code language="bash"]$ sort names.txt [/code]
以降序排列文件 
[code language="bash"]$ sort -r names.txt [/code]
以第三列排序文件 
[code language="bash"]$ sort -t: -k 3n /etc/passwd | more [/code]
10. export 
查看oracle的环境变量 
[code language="bash"]$ export | grep ORACLE 
declare -x ORACLE_BASE="/u01/app/oracle" 
declare -x ORACLE_HOME="/u01/app/oracle/product/10.2.0" 
declare -x ORACLE_SID="med" 
declare -x ORACLE_TERM="xterm" [/code]
export一个变量 
[code language="bash"]$ export ORACLE_HOME=/u01/app/oracle/product/10.2.0 [/code]
11. xargs 
将所有的图片拷贝的外置硬盘 
[code language="bash"]# ls *.jpg | xargs -n1 -i cp {} /external-hard-drive/directory [/code]
找到系统中所有的jpg图片，并且打包 
[code language="bash"]# find / -name *.jpg -type f -print | xargs tar -cvzf images.tar.gz [/code]
下载url-list.txt提到的所有URLS 
[code language="bash"]# cat url-list.txt | xargs wget –c [/code]
12. ls 
以易读的方式显示文件大小(例子 KB, MB etc.,) 
[code language="bash"]$ ls -lh 
-rw-r----- 1 ramesh team-dev 8.9M Jun 12 15:27 arch-linux.txt.gz [/code]
以最后修改时间给文件反向排序 
[code language="bash"]$ ls -ltr [/code]
显示文件的分类 
[code language="bash"]$ ls -F [/code]
更多的例子： [Unix LS Command: 15 Practical Examples ](http://www.thegeekstuff.com/2009/07/linux-ls-command-examples/)
13. pwd 
pwd用来显示工作目录 
14. cd 
[code language="bash"]Cd - 可以在两个最近使用的目录之间切换 
shopt -s cdspell 可以自动更改cd到某个目录时的拼写错误 [/code]
更多的例子：[ 6 Awesome Linux cd command Hacks ](http://www.thegeekstuff.com/2008/10/6-awesome-linux-cd-command-hacks-productivity-tip3-for-geeks/)
15. gzip 
创建一个.gz文档 
[code language="bash"]$ gzip test.txt [/code]
解压缩 
[code language="bash"]$ gzip -d test.txt.gz [/code]
显示压缩文件的压缩比率 
[code language="bash"]$ gzip -l *.gz 
         compressed        uncompressed  ratio uncompressed_name 
              23709               97975  75.8% asp-patch-rpms.txt [/code]
16. bzip2 
创建*.bz2 文档 
[code language="bash"]$ bzip2 test.txt [/code]
解压缩*.bz2 文档 
[code language="bash"]bzip2 -d test.txt.bz2 [/code]
更多的例子: [BZ is Eazy! bzip2, bzgrep, bzcmp, bzdiff, bzcat, bzless, bzmore examples ](http://www.thegeekstuff.com/2010/10/bzcommand-examples/)
17. unzip 
解压缩a *.zip 
[code language="bash"]$ unzip test.zip [/code]
查看*.zip文件，不解压 
[code language="bash"]$ unzip -l jasper.zip 
Archive:  jasper.zip 
  Length     Date   Time    Name 
 --------    ----   ----    ---- 
    40995  11-30-98 23:50   META-INF/MANIFEST.MF 
    32169  08-25-98 21:07   classes_ 
    15964  08-25-98 21:07   classes_names 
    10542  08-25-98 21:07   classes_ncomp [/code]
18. shutdown 
立刻关机 
[code language="bash"]# shutdown -h now [/code]
10分钟后关机 
[code language="bash"]# shutdown -h +10 [/code]
重启 
[code language="bash"]# shutdown -r now [/code]
在重启期间强制检查文件系统 
[code language="bash"]# shutdown -Fr now [/code]
19. ftp 
ftp和sftp都有类似的命令。链接远程主机，下载文件 
[code language="bash"]$ ftp IP/hostname 
ftp> mget *.html [/code]
在下载之前查看远程主机的文件的名 
[code language="bash"]ftp> mls *.html - 
/ftptest/features.html 
/ftptest/index.html 
/ftptest/othertools.html 
/ftptest/samplereport.html 
/ftptest/usage.html [/code]
更多的例子: [FTP and SFTP Beginners Guide with 10 Examples ](http://www.thegeekstuff.com/2010/06/ftp-sftp-tutorial/)
20. crontab 
查看特定用户的crontab列表 
[code language="bash"]# crontab -u john -l [/code]
设置cron任务每10分钟执行 
[code language="bash"]*/10 * * * * /home/ramesh/check-disk-space [/code]
更多的例子:[ Linux Crontab: 15 Awesome Cron Job Examples ](http://www.thegeekstuff.com/2009/06/15-practical-crontab-examples/)
21. service 
Service用来允许 system V 格式的初始化脚本 ，比如说，与其带着全路径运行 /etc/init.d/ 下的命令， 你可以使用service命令 
显示某个服务的状态 
[code language="bash"]# service ssh status [/code]
显示所有服务的状态 
[code language="bash"]service --status-all [/code]
重启某个服务 
[code language="bash"]# service ssh restart [/code]
22. ps 
ps 显示系统中进程的信息。ps有很多的参数，但主要的有下面的 
查看当前所有进程 
[code language="bash"]$ ps -ef | more [/code]
以树形结构查看 
[code language="bash"]$ ps -efH | more [/code]
23. free 
显示系统中空闲，已用，交换内存的信息 
常规的free命令输出。通常输出单位是字节 
[code language="bash"]$ free 
             total       used       free     shared    buffers     cached 
Mem:       3566408    1580220    1986188          0     203988     902960 
-/+ buffers/cache:     473272    3093136 
Swap:      4000176          0    4000176 [/code]
如果加参数-g，以GB单位显示，而-b以字节，-k 以千字节，-m以m单位显示 
[code language="bash"]$ free -g 
             total       used       free     shared    buffers     cached 
Mem:             3          1          1          0          0          0 
-/+ buffers/cache:          0          2 
Swap:            3          0          3 [/code]
如果你想查看所有的内存（包括swap）加-t选项 
[code language="bash"]ramesh@ramesh-laptop:~$ free -t 
             total       used       free     shared    buffers     cached 
Mem:       3566408    1592148    1974260          0     204260     912556 
-/+ buffers/cache:     475332    3091076 
Swap:      4000176          0    4000176 
Total:     7566584    1592148    5974436 [/code]
24. top 
top 显示系统中的cpu消耗量最大的进程 。要对输出以列排序的话，按“O”，得到下面的项目，你可以以下面的选项进行排序。 
[code language="bash"]Current Sort Field:  P  for window 1:Def 
Select sort field via field letter, type any other key to return 

  a: PID        = Process Id              v: nDRT       = Dirty Pages count 
  d: UID        = User Id                 y: WCHAN      = Sleeping in Function 
  e: USER       = User Name               z: Flags      = Task Flags 
  ........ [/code]
-u显示属于某个用户的进程 
[code language="bash"]$ top -u oracle [/code]
更多的例子 [Can You Top This? 15 Practical Linux Top Command Examples ](http://www.thegeekstuff.com/2010/01/15-practical-unix-linux-top-command-examples/)
25. df 
显示文件系统的磁盘使用情况。默认输出以字节为单位 
[code language="bash"]$ df -k 
Filesystem           1K-blocks      Used Available Use% Mounted on 
/dev/sda1             29530400   3233104  24797232  12% / 
/dev/sda2            120367992  50171596  64082060  44% /home [/code]
df -h 以GB位单位输出 
[code language="bash"]ramesh@ramesh-laptop:~$ df -h 
Filesystem            Size  Used Avail Use% Mounted on 
/dev/sda1              29G  3.1G   24G  12% / 
/dev/sda2             115G   48G   62G  44% /home [/code]
-T 选项显示文件系统类型 
[code language="bash"]ramesh@ramesh-laptop:~$ df -T 
Filesystem    Type   1K-blocks      Used Available Use% Mounted on 
/dev/sda1     ext4    29530400   3233120  24797216  12% / 
/dev/sda2     ext4   120367992  50171596  64082060  44% /home[/code]
