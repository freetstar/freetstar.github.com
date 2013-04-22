---
author: admin
comments: true
date: 2010-10-30 17:01:00
layout: post
slug: teach_you_to_enjoy_the_zsh-1
title: 教你使用zsh之=======安装和配置zsh
wordpress_id: 1380
categories:
- 软件安装
---

	简介: 

	 相对于绝大多数linux发行版默认的shell--bash,zsh绝对是一个优秀的替代品.zsh是交互型shell,同时它也是一个强大的编程语言,许多bash,ksh,tcsh优秀的地方在zsh都被实现.同时zsh有许多原生的优秀特点. 

	诞生:

	Paul Falstad 在1990年发布了zsh的第一版,当时他还是Princeton University的一名学生.

	名字的来源: 

	 这个名字来自耶鲁大学的Zhong Shao教授,那时他在Princeton University做助教.Paul Falstad认为Shao的登录名"zsh"做为1个shell的名字挺合适的.于是zsh这个名字诞生了

	安装:

	本文以ubuntu10.10发行版为蓝本.  sudo apt-get install zsh

	第一次运行 

	 第一次运行时你会得到下列输出 

	 This is the Z Shell configuration function for new users,zsh-newuser-install.  

	 You are seeing this message because you have no zsh startup files(the files .zshenv, .zprofile, .zshrc, .zlogin in the directory~). This function can help you with a few settings that shouldmake your use of the shell easier.  

	 You can:  

	 (q) Quit and do nothing. The function will be run again next time.  

	 (0) Exit, creating the file ~/.zshrc containing just a comment.That will prevent this function being run again.  

	 (1) Continue to the main menu.  

	 (2) Populate your ~/.zshrc with the configuration recommended by the system administrator and exit (you will need to edit the file by hand, if so desired).  

	 因为是第一次运行,所以会出现配置界面.我们在这里暂时先选择0,以便实现随后的定制.

	特色 

	 Tab补全 

	 zsh实现了全面可编程化的补全方式,允许用户让shell自动补全各种命令的参数(即使那些与shell本身无关的命令), 自动填充shell的许多转换的定义以及许多恰当的参数类型.比如:输入tar xvf ,然后Tab键,系统会自动选择tar.gz文件,略过那些不符合的.现在zsh默认有500多个补全定义  

	 实现方法:  

	 %autoload -U compinit  

	 %compinit  

	 更高级的补全:  

	 % zstyle ':completion:*:descriptions' format '%U%B%d%b%u' 

	 % zstyle ':completion:*:warnings' format '%BSorry, no matches for: %d%b' 

	 它可以自动补全命令、参数、文件名、进程、用户名、变量、权限符等。  

	 选择提示符 

	 zsh有许多默认的提示符主题.首先你要初始化高级提示符支持  

	 %autoload -U promptinit  

	 %promptinit  

	 查看可用的提示符主题:  prompt -p  

	 这里我选择  promot elite2 red  

	 定制历史信息: 

	 这里我们设置记录命令历史文件位~/.histfile,在当前shell中记录1000个命令,在shell关闭后保存使用过的最后1000个命令  

	 HISTFILE=~/.histfile  

	 HISTSIZE=1000  

	 SAVEHIST=1000  

	 如果你不想保存重复的历史  

	 setopt hist_ignore_all_dups hist_ignore_space  

	 自动化的CD命令 

	 zsh允许你仅仅敲入你要进入的文件夹的路径,而不用输入cd.比如你要进入/etc/init.d  

	 首先打开autocd选项  setopt autocd  

	 然后输入  /etc/init.d 回车即可进入文件夹中  

	 扩展的文件名替换通配符 

	 文件名替换实现了在展开文件通配符,来出一些特定的文件.广大的shells一直都在使用文件名替换.比如:  

	 %ls foo*  

	 foo1 foo2 

	 强大的重定向功能: 

	 同时重定向stdout和stderr到file: command |& >file 同时重定向到多个文件: command >file.1 >file.2  

	 zsh的确是个强大的shell,它支持许多有趣的通配符扩展.你可以使用通配符号,他们是一些有特殊意义的字符.例如:列出当前文件夹下所有的符号链接文件:  

	 %ls *(@) 

	 zsh的通配符包括了"/"来表示目录,"."代表普通文件.更多的man zshexpn查看.如果没有匹配,zsh返回错误.  

	 还有其他的类型,比如"**/",表示让zsh匹配当前目录及当前目录的所有子目录.例如,找到当前目录下以及子目录下的任何"*.sh"或者"*.py"文件,  

	 %ls -l **/*.(sh|py)  

	 让配置保持生效 

	 为了一直使用扩展的文件名替换,将下边命令添加到~/.zshrc  
 
		autoload -Uz compinit
 
		compinit
 
		zstyle :compinstall filename '/home/capecchi/.zshrc'
 
		zstyle ':completion:*:descriptions' format '%U%B%d%b%u'
 
		zstyle ':completion:*:warnings' format '%BSorry, no matches for: %d%b'
 
		#Prompt setup
 
		autoload -U promptinit
 
		promptinit
 
		prompt elite2 yellow
 
		# History
 
		HISTFILE=~/.histfile
 
		HISTSIZE=1000
 
		SAVEHIST=1000
 
		#We set some options here
 
		setopt appendhistory autocd hist_ignore_all_dups hist_ignore

	 注:  ~/.zshrc文件可以来自交互和登录shell。如果你希望为非交互运行的zsh（即，通过cronjob）设定选项，那么你需要把那些命令添加在~/.zshenv后面  

	 更改用户默认的登录shell: 

	 chsh -s /bin/zsh username  普通用户可以更改自己的,root用户则可更改所有用户的

	参考:http://www.linuxaria.com/howto/introduzione-a-zsh?lang=it

	 [http://www.builder.com.cn/2007/0328/383678.shtml](http://www.builder.com.cn/2007/0328/383678.shtml)

	 [http://linuxtoy.org/archives/zsh.html](http://linuxtoy.org/archives/zsh.html)

