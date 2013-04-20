---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

---
author: admin
comments: true
date: 2010-06-29 23:11:39
layout: post
slug: ubunt10-04-reslove-problem-2
title: 我的ubuntu10.04 使用笔记 问题解决
wordpress_id: 756
categories:
- ubuntu
- 问题解决
---

	继上一次[问题总结](http://www.freetstar.com/index.php/ubunt10-04-reslove-problem-1)之后放出问题总结二

	1 双击后缀为txt的文件提示打开方式

> 
	
> 
> 
		 打开文件管理器->编辑->首选项->行为，在"可执行文本文件"中勾选"打开时查看可执行文本文件"
	
> 
> 

	2 启用ctrl+alt+backspace

> 
	
> 
> 
		 系统>首选项->键盘快捷键 中找到注销，同时按下上边的组合键即可
	
> 
> 

	3  gnome面板恢复初始状态

> 
	
> 
> 
		 把你的gnome配置文件都删掉，然后再重新进入(ctrl+alt+backspace）
	
> 
> 
	
> 
> 
		 rm -rf ~/.gnome* ~/.gconf*<!-- more -->
	
> 
> 

	4开机提示要输入登录密钥 

> 
	
> 
> 
		 打开终端输入seahorse，切换到密码选项卡，右键更改密码，都不要填，直接提交，这样就去掉默认密钥环的密码了。
	
> 
> 

	5u盘无法卸载的情况

> 
	
> 
> 
		 sync
	
> 
> 
	
> 
> 
		 fuser -km /media/usbdisk
	
> 
> 

	6 清除僵死进程

> 
	
> 
> 
		 ps -eal | awk '{ if ($2 == "Z") {print $4}}' | xargs sudo kill -9
	
> 
> 

	7 解压rar乱码问题

> 
	
> 
> 
		 本人安装时是sudo apt-get install rar unrar ,只需要sudo apt-get autoremove rar 即可,即把rar卸载就可解决乱码问题
	
> 
> 

