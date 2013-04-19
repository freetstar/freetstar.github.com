---
author: admin
comments: true
date: 2010-11-28 21:00:40
layout: post
slug: learing-fping
title: ping？不，我们还有更强大的fping
wordpress_id: 1499
categories:
- 软件安装
---

fping命令简介：
           fping - 发 ICMP ECHO_REQUEST 包到网络主机
详细：
          fping类似于ping命令，发送ICMP的回显数据包给特定主机，要求对方给于回应。fping 与ping不同的是，fping允许同时设置很多主机，也可以将要发送主机的列表列表写在文件中。fping在发送消息时，如果对方没有反应，fping会接着给下个主机发送包，循环往复，而不是等待没有反应的主机给于反应。
          默认情况下，如果对方主机回应了，则下次fping命令则不再检查此主机，如果一个主机在特定时间限制或者尝试限制的次数下没能够反应，则被标志为无法到达。Fping和ping有许多的相同选项。
          和ping不同的时，fping更倾向于在脚本中被使用
安装方法：
	  [code language="bash"]sudo apt-get install fping[/code]
<!-- more -->
用法：
           [code language="bash"]fping   [options]   hosts[/code]
常用选项：
	  [code language="bash"]
	-a 显示有回应的主机
        -A 显示主机的IP地址
        -c  给每个主机发送的包的数量。这时会为每个包信息独立输出一行（还有额外的-q选项）
        -C  基本上同-c选项，但是输出和-c不太一样
	-d 解析主机名
	-f 从文件里读取主机列表，只有root用户可用。一般用户只能重定向
              %fping <targets_file
      -q 安静模式。不显示每个主机的结果，只显示最终的退出状态
      -rn 设置尝试次数，默认为3
      -Tn 设置超时时间，单位秒（默认10）
      -u  显示不可达的主机
	[/code]
 退出状态：
	0表示所有主机可达
        1 表示有的主机没有反应
        2  表示没有找到任何主机
        3 命令行参数错误
        4 系统调用失败
总结：
	fping命令以轮转的方式发出去大量的ping请求，比ping单独的对一个目的主机操作要简单和快速的多。乃利器也
	
         
