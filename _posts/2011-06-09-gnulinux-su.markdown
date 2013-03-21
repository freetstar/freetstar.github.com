---
comments: true
date: 2011-06-09 14:11:39
layout: post
slug: gnulinux-su
title: GNU/Linux中的su
wordpress_id: 1724
categories:
- linux前沿
---

su是switch user的缩写,为了从某个用户环境中切换到另一个用户环境中,比如说su - root是切换到root用户,并且使用root用户的环境变量,而su root是切换到root用户,但使用的是当前用户的环境变量,再多的就不再赘述.





su的存在方便了用户,但是也有安全隐患,su的滥用可能导致安全隐患.





  






本文主要体验利用PAM来限制su的行为





  






测试环境:ubuntu10.10





查看当前用户的情况





在Ubuntu系统中,默认安装时第一个用户被添加到admin组,我安装ubuntu时的用户是freetstar,用id命令查看freetstar所在的用户组





> ┌┌(freetstar@freetstar-lap)┌(3657/pts/1)┌(01:02pm:06/09/11)
> 
> 


> 
> ┌-└┌(%:~)┌- id
> 
> 


> 
> uid=1000(freetstar) gid=1000(freetstar) groups=1000(freetstar),4(adm),20(dialout),24(cdrom),29(audio),30(dip),46(plugdev),110(netdev),111(lpadmin),119(admin),122(sambashare),125(libvirtd)
> 
> 






<!-- more -->





第一步:测试正常情况下的su操作





> ┌┌(freetstar@freetstar-lap)┌(3671/pts/8)┌(01:23pm:06/09/11)┌-
> 
> 


> 
> └┌(%:/var/log)┌-** sudo passwd root**
> 
> 


> 
> Enter new UNIX password:
> 
> 


> 
> Retype new UNIX password:
> 
> 


> 
> passwd: password updated successfully
> 
> 


> 
> **#说明,首先利用sudo给root用户设置密码**
> 
> 


> 
> ┌┌(freetstar@freetstar-lap)┌(3673/pts/8)┌(01:28pm:06/09/11)┌-
> 
> 


> 
> └┌(%:/var/log)┌- **su - root**
> 
> 


> 
> Password:
> 
> 


> 
> ┌┌(root@freetstar-lap)┌(23/pts/8)┌(01:28pm:06/09/11)┌-
> 
> 


> 
> └┌(#:~)┌-
> 
> 


> 
> **#su到root用户**
> 
> 

> 
> 

> 
> ┌(freetstar@freetstar-lap)┌(3674/pts/8)┌(01:31pm:06/09/11)┌-
> 
> 

> 
> └┌(%:/var/log)┌-** sudo tail -f auth.log**
> 
> 

> 
> ......
> 
> 

> 
> 

> 
> 

> 
> Jun  9 13:30:15 freetstar-lap su[15097]: Successful su for root by freetstar
> 
> 

> 
> Jun  9 13:30:15 freetstar-lap su[15097]: + /dev/pts/7 freetstar:root
> 
> 

> 
> Jun  9 13:30:15 freetstar-lap su[15097]: pam_unix(su:session): session opened for user root by freetstar(uid=1000)
> 
> 

> 
> 

> 
> **#查看auth信息,显示freetstar这个用户su到root用户成功**
> 
> 





第二步:修改认证模块,只是注释掉这两个认证模块




> 

> 
> 

> 
> **sudo vim /etc/pam.d/su**
> 
> 

> 
> 

> 
> # auth       required   pam_wheel.so
> 
> 

> 
> # auth       sufficient pam_wheel.so trust
> 
> 

> 
> **第一行表示需要是wheel用户组的用户才可以执行su操作**
> 
> 

> 
> **第二行表示su时不需要提供密码**
> 
> 

> 
> 

> 
> 






保存退出,尝试登录root用户,





> ┌┌(freetstar@freetstar-lap)┌(3662/pts/7)┌(01:39pm:06/09/11)┌-
> 
> 


> 
> └┌(%:~/Downloads)┌- **su  - root**
> 
> 


> 
> Password:
> 
> 


> 
> su: Permission denied
> 
> 


> 
> **#提示被拒**
> 
> 


> 
> ┌┌(freetstar@freetstar-lap)┌(3675/pts/8)┌(01:38pm:06/09/11)┌-
> 
> 


> 
> └┌(%:/var/log)┌-** sudo tail -f auth.log **
> 
> 


> 
> ......
> 
> 


> 
> Jun  9 13:39:28 freetstar-lap su[15097]: pam_unix(su:session): session closed for user root
> 
> 


> 
> Jun  9 13:39:32 freetstar-lap su[15407]: pam_authenticate: Permission denied
> 
> 


> 
> Jun  9 13:39:32 freetstar-lap su[15407]: FAILED su for root by freetstar
> 
> 


> 
> Jun  9 13:39:32 freetstar-lap su[15407]: - /dev/pts/7 freetstar:root
> 
> 


> 
> **#提示失败**





第三步:设置"wheel组"





Wheel本来的意义是让只有在Wheel组中的用户才有权限去执行su命令,但在现在的Linux发行版中,几乎没有了Wheel这样一个组





  






基本上只有BSD发行版才默认启用Wheel组.关于Linux中的wheel,看Richard大神怎么说的:[here](http://www.gnu.org/software/coreutils/manual/html_node/su-invocation.html)





在这里不用太麻烦地去添加wheel组,再usermod的将当前用户添加到wheel组中.我们只





需要重新修改认证模块的配置文件





  






> 

> 
> **sudo vim /etc/pam.d/su**
> 
> 

> 
> 

> 
> auth       required   pam_wheel.so group=admin
> 
> 

> 
> 

> 
> auth       sufficient pam_wheel.so trust
> 
> 

> 
> **#将默认的wheel组改成admin组,admin组即Ubuntu下的管理组**
> 
> 






  






重新尝试su





  






> ┌┌(freetstar@freetstar-lap)┌(3687/pts/7)┌(01:50pm:06/09/11)┌-
> 
> 


> 
> └┌(%:~/Downloads)┌- su  - root
> 
> 


> 
> Password:
> 
> 


> 
> ┌┌(root@freetstar-lap)┌(23/pts/7)┌(01:56pm:06/09/11)┌-
> 
> 


> 
> └┌(#:~)┌-
> 
> 


> 
> **#成功了**
> 
> 






  






auth.log就不再贴了,基本上和第一步的日志一样





这里有一个小问题:root用户默认不再admin组里,所以为了让root用户也可以无障碍su,需要将root用户添加到admin组中





  






Tips:





1 任何使用su成功与否的信息都会在日志中有记录





2 谨慎修改,修改不当会造成无法开机进入系统





  






欢迎疑问,求疑问





  






  






  

