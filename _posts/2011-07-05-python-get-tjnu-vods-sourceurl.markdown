---
author: admin
comments: true
date: 2011-07-05 10:38:14
layout: post
slug: python-get-tjnu-vods-sourceurl
title: 用Python抓取天津师范大学VOD视频资源的地址
wordpress_id: 1750
categories:
- python
---

好不容易，软磨硬泡地在学校14号楼住下来，要不就去睡大街了，学校的理由：只让重修的同学住14号，然后我就好不容易“重修”了。接下来就是白天博理晚上14号楼的生活。。然后就每天就只能教育网了，教育网什么最好，VOD!之前一直惦记着下载VOD上的资源，看到以前师大物电的同学有过寻找VOD真实资源的经过，[天津师范大学校园网（教育网）VOD下载方法](http://www.liboxia.com/archives/651)，





于是想用python搞一个。简单实现了下，输入想要下载的剧集id和集数(这个需要去网页的源码理看,上边的链接里有介绍),然后自动解释出下载链接的真实地址,





思路：





1 首先访问http://59.67.75.254/actIndex.do页面，这是资源的列表页，但是需要匿名登陆才可以看见，而为什么在这里先访问的actIndex.do页面，而不是先匿名登陆，因为我发现首先访问http://59.67.75.254/login.jsp登陆页面没有匿名访问选项，偶然发现先访问actIndex.do页面的话，在http回话中会有一个附有JesseionID的URL做为Response headers的Location返回，然后只要访问这个带JesseionID的URL，就可以实现登录的目的  

 2 访问上述所说的带JesseionID的URL，这个页面实际上http://59.67.75.254/login.jsp?JESSEIONID=XXX,这里简单的用一个GET请求即可





3 再次访问actIndex.do页面，这时候就真正登录进来了,可以查看资源列表文件了





4 在actIndex.do页面,选择某个想要看的视频，查看页面源文件，查看此视频对应的progid是多少，每个视频文件的progid唯一的，还有查看每个有多少集，举个例子:柯南剧场的独有的progid是3349，而 柯南剧场的有400多集，所以柯南剧场对应的volume就从1-400多这个范围移动，这个具体的含义不懂得话还可以参考上边物电的同学的链接





5 接着访问下载页面http://59.67.75.254/actDownload.do，用GET方法请求，带着上边的progid和volume信息,在http会话中发现在response headers中还有Location标志，指向下载的download.jsp页面，这时urilib2会自动访问download.jsp，然后做一个跳转，在接收回来的response body会有真实资源的地址，如





<html><head><title>下载</title><script language ="javascript" src ="./js/vod.js"></script><script language=javascript> DownLoadPath('59.67.75.254:2880','/moive2/娱乐天地/动漫/116009427841.rmvb','3499','RMVB','名侦探柯南');</script></head></html>  


  


  

   

 6 那么下载的话，链接就是  

 http://59.67.75.254:2880/moive2/娱乐天地/动漫/116009427841.rmvb  ，文件名可以自己更改下





**要注意的：**





1 师大VOD需要登录后才能观看，这一步在代码里已经实现





2 师大VOD还检测VOD客户端安装没有，所以使用代码前一定要安装vod客户端。。当然他是用js检测的vod安装情况，要是屏蔽或者欺骗js代码就好了，可惜不会





3 貌似只支持IE内核的浏览器，我觉得可能有2个原因：(1) js利用ie的某些东西检测vod安装情况和版本 (2) 应用本身不支持。而我我在代码中用的是MSIE9的user-agent,代码也是在win7+ie9下运行的





代码丑陋，见笑：




    
    <span style="font-size: medium;"># -*- coding=gb2312 -*-
     import urllib
     import urllib2
     import cookielib
     import re
    
     user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'
     #注册一个cookie的opener,用来带着cookie访问url
     cookie = cookielib.CookieJar()
     cookie_support= urllib2.HTTPCookieProcessor(cookie)
     opener = urllib2.build_opener(cookie_support)
     urllib2.install_opener(opener)
     headers = {'User-Agent':user_agent,"Keep-Alive":"115"}
    
    #首先访问actIndex页面
     url2 = 'http://59.67.75.254/actIndex.do'
     req2 = urllib2.Request(url2,headers)
     response2 = opener.open(url2)
     the_page2 = response2.read()
    #print the_page2
    #获取SessionID,然后从第一次访问时返回的response2中截取url,也就是带sessionid的登录url 
     url1 = response2.geturl()
     response1 = opener.open(url1) the_page1 = response1.read()
    
    #再次访问actIndex页面，这时候就以匿名用户的身份登录喽
     url3 = 'http://59.67.75.254/actIndex.do'
     req3 = urllib2.Request(url3,headers)
     response3 = opener.open(url3)
     the_page3 = response3.read()
     #print the_page3
    
    #登录好之后进行下载的操作
     url4 = 'http://59.67.75.254/actDownload.do'
     values = {'volume':'1',
     'progid':'3499'
     }  //这个即表示3499这个id的剧集中的第一集
     data = urllib.urlencode(values)
     req4 = urllib2.Request(url4,data,headers)
     response4 = urllib2.urlopen(req4)
     the_page4 = response4.read().decode('gb2312')
     result = re.findall("'59.67.75.*'",the_page4)
     print "http://"+str(result[0].encode('gb2312').split(',')[0]).strip("'") + str(result[0].encode('gb2312').split(',')[1]).strip("'")
      //打印出vod视频链接</span>
