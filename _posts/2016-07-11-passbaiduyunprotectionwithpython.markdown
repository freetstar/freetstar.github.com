---
title: 爬虫中使用Python穿越百度云防护
layout: post
guid: urn:uuid:5f5801a5-3229-4f37-8af0-b6aa12831a4a
tags:
  - 
---

在做爬虫时，直接访问目标URL时scrapy会返回503响应，手工访问后,发现是网站采取了百度云加速的防护机制:直接
返回一个页面，页面内部有一段隐藏的form，然后js代码随机生成form中某个input的值，最后进行提交，提交之后
服务器会返回一个cf_clearance的cookie，获取这个cookie后,休眠五秒钟，再用此cookie去访问目标URL，目的当然是用来过滤我们机器人的....


总体的解决思路就是用beautifulsoup和re模块爬下对应的input value，然后使用pyv8模拟js代码执行表单动作，获取返回的cookie值。

这里已经有高手用perl语言实现的版本，见[**这里**](https://www.digglife.net/articles/how-to-cheat-baidu-yunjiasu.html ),

我用Python实现的,在[**这里**](https://github.com/freetstar/scrapypassbaiduyunprotection)
