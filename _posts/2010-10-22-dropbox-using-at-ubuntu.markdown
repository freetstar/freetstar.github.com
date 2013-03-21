---
comments: true
date: 2010-10-22 20:45:01
layout: post
slug: dropbox-using-at-ubuntu
title: Dropbox在ubuntu下的安装和使用实战
wordpress_id: 1351
categories:
- 软件安装
---


	Dropbox 介绍：






	 Dropbox 是一个优秀的云端储存同步服务。Dropbox 可跨平台同步，目前的客户端已支持 Linux，Windows，Mac OS 及部分 Mobile 系统，如 Android，iPhone，BlackBerry等，安装十分方便。它还提供 Web 访问及操作，它是你电脑的一部分……如果你只有一台电脑，可以用它来当作网盘储存数据，也可以把文件或目录共享给其他人；如果你有多台电脑，可以同步每台电脑上需要共享的数据，而不必拿 U 盘或移动硬盘导来导去。只需要把需要同步的文件或目录放入 Dropbox 中，便可随时随地使用这些数据。






	Dropbox在"中国"的安装方法：<!-- more -->






	 由于各种"原因"，我们无法正常的安装和使用。。。JUST FUCK G#F#W#！我推荐你拥有1枚ssh账号，你懂得！在这里我们利用ssh来安装Dropbox。这里使用Proxychains工具来安装Dropbox，ProxyChains工具的使用方法：[here](http://wiki.wowubuntu.com/blog/ubuntu_ssh_tunneling)






	 32位： proxychains wget https://www.dropbox.com/download?dl=packages/nautilus-dropbox_0.6.3_i386.deb






	 64位： proxychains wget https://www.dropbox.com/download?dl=packages/nautilus-dropbox_0.6.3_amd64.deb






	 下载到deb包之后，安装。然后运行






	 proxychains dropbox start -i  

	






	 然后安装成功后，可以设置proxy，方便你的proxy使用






	 更详细的安装见：[WOW！ubuntu](http://wowubuntu.com/ubuntu_dropbox.html)[ ](http://wowubuntu.com/ubuntu_dropbox.html)






	Dropbox的使用技巧：






	 一。同步Dropbox之外的文件夹






	 由于在ubuntu下dropbox默认只同步Dropbox文件夹内的数据，要想直接同步其他文件夹的的数据，可以使用以下方法：






	 ln -s /path/to/folder/name_desired_folder/ ~/Dropbox/desired-folder //即做软链接






	 或者在Dropbox内新建目录，而在其他文件夹中放指定的目录中






	






	 二。利用Dropbox在PC和VPS之间同步数据






	 //登录到vps






	 ssh freetstar@www.freetstar.com






	 //切换至主目录






	 cd  






	 //下载32位安装包






	 wget -O dropbox.tar.gz http://www.dropbox.com/download/?plat=lnx.x86






	 //解压






	 tar -xvzf dropbox.tar.gz  

	






	 //运行






	 ~/.dropbox-dist/dropboxd






	 接下来提示






	 This client is not linked to any account...






	 Please visit https://www.dropbox.com/cli_link?host_id=7d44a557aa58f285f2da0x67334d02c1 to link this machine.






	 Host_id会随机器变化.打开上边的链接,然后再查看event,会发现www.freetstar.com已经被添加






	






	 同时,目录下会生成Dropbox文件夹,运行~/.dropbox-dist/dropbox &来进行同步






	 注明:dropboxd调用dropbox来运行






	 更详细的安装方法:[http://wiki.dropbox.com/TipsAndTricks/TextBasedLinuxInstall](http://wiki.dropbox.com/TipsAndTricks/TextBasedLinuxInstall)






	 [http://wiki.dropbox.com/TipsAndTricks/UbuntuServerInstall](http://wiki.dropbox.com/TipsAndTricks/UbuntuServerInstall)






	 还有更多的Tricks:[http://wiki.dropbox.com/TipsAndTricks](http://wiki.dropbox.com/TipsAndTricks)






	






	






	Dropbox使用邀请：






	 Dropbox默认有2G的免费空间，每邀请1位新增用户，双方获得250M的空间。免费上限为10G。我的邀请链接是：[http://www.dropbox.com/referrals/NTExMTc0MDUzOQ](http://www.dropbox.com/referrals/NTExMTc0MDUzOQ)






	 






	参考文章：[http://www.maizidi.com/dropbox-sync-other-folders/](http://www.maizidi.com/dropbox-sync-other-folders/)






	 [http://wowubuntu.com/vps-dropbox.html](http://wowubuntu.com/vps-dropbox.html)//其实是p哥写的日志,我就不再外链了






	




