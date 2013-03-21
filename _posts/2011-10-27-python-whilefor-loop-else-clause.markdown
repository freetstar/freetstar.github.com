---
comments: true
date: 2011-10-27 17:45:32
layout: post
slug: python-whilefor-loop-else-clause
title: 小说Python中的while/for循环后的else
wordpress_id: 1843
categories:
- python
---

首先来看c/c++语言，在c/c++中我们在处理一个循环时，通常是如下形式



    
    for(i=0;i<n;i++)
          {your code}//可能有必要的break或者continue语句




或者



    
    while(True)
          {your code}//可能有必要的break或者continue语句




<!-- more -->



    
     




基本上是for/while关键字加上条件，然后循环体内写代码，代码内可能包含了必要的break或者continue语句来跳出循环或者跳过当此循环。而循环之后再则是其他语句，与前边的循环无直接关系  
我们再来看python语言，在Python中的while或者for循环之后还可以有**else子句**，形如下：




> 

>     
>     for x in range(1,5):
>           if x == 6 :
>                print "found the number",x
>                break;
>     else:
>           print "not found!"
> 
> 





保存上边的代码，运行得到“not found”,**WHY？**我们先来看看python官方文档中的解释，原文在[这儿](http://docs.python.org/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)：




> 

> 
> Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with [for](http://docs.python.org/reference/compound_stmts.html#for)) or when the condition becomes false (with [while](http://docs.python.org/reference/compound_stmts.html#while)), but not when the loop is terminated by a [break](http://docs.python.org/reference/simple_stmts.html#break) statement.
> 
> 





翻译：**循环语句后可以有一个else从句，这个else从句在因为for循环中list全部遍历完或者因为while循环中条件不满足而执行，而如果循环中有break语句执行了则else从句就不执行了**。。




简单理解来：for循环中if条件一直不满足，则最后就执行else语句  
我们这里来简单想象下如果用c语言式的写法，即添加found flag




> 

>     
>     found = false
>     for x in range(1,5):
>          if x == 6:
>               found = True
>               print "found the number",x
>               break;
>      if !found:
>          print "nout found!"
> 
> 





每个人有可能对这样的实现有自己的理解，可能大家更喜欢或者习惯使用found flag：）




更多的讨论，在[这里](http://nedbatchelder.com/blog/201110/forelse.html)
