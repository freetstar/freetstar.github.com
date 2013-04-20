---
author: admin
comments: true
date: 2011-04-25 18:46:52
layout: post
slug: python-os-path-elementtree-xml
title: python学习之os.path模块&&elementtree处理xml文件
wordpress_id: 1679
categories:
- PROGRAM
---

学习中，肯定有不对的地方！

python中os.path常用模块

> 

> 
> os.path.sep:路径分隔符      linux下就用这个了'/'
> 
> 

> 
> os.path.altsep: 根目录
> 
> 

> 
> os.path.curdir:当前目录
> 
> 

> 
> os.path.pardir：父目录
> 
> 

> 
> os.path.abspath(path)：绝对路径
> 
> 

> 
> os.path.join():       常用来链接路径
> 
> 

> 
> os.path.split(path):      把path分为目录和文件两个部分，以列表返回
> 
> 

见图：

![](http://i.imgur.com/2tn6g.png)

python中用ElementTree来读写处理xml文档

添加xml.etree.ElementTree模块

> 

> 
> import xml.etree.ElementTree as ET
> 
> 

两种解析xml方式

1解析xml文档

> 

> 
> ET.parse('test.xml')
> 
> 

2 解析xml字符串

> 

> 
> ET.fromstring(string)
> 
> 

得到xml的root元素

> 

> 
> tree=ET.parse('test.xml')
> 
> 

> 
> root=tree.getroot()
> 
> 

xml中元素(Element)属性

> 

> 
> 

> 
> tree=ET.parse('test.xml')
> 
> 

> 
> root=tree.getroot()
> 
> 

> 
> #root是一个特殊的元素(Element)
> 
> 

> 
> #元素的tag
> 
> 

> 
> 

> 
> root.tag
> 
> 

> 
> #元素的text
> 
> 

> 
> root.text
> 
> 

> 
> #元素的children类似于列表
> 
> 

> 
> root[0]表示root下的第一个子元素，root[1]表示root的第二个子元素，依次类推。。。
> 
> 

> 
> #元素的属性.attrib是一个字典。也就是用唯一的键，和其对应的值
> 
> 

> 
> root[o].attrib
> 
> 

xml中创建子节点

> 

> 
> #parent即父节点，tag则创建元素的tag
> 
> 

> 
> ET.SubElement(parent,tag)
> 
> 

xml中查找节点

> 

> 
> 方法为:find,findall
> 
> 

xml写到文件中

> 

> 
> tree=ET.parse('test.xml')
> 
> 

> 
> tree.write('test2.xml')
> 
> 

Element中有3个对象（不知道这样说准确否）

第一个是xml.etree.ElementTree本身，为了书写方便一般直接import xml.etree.ElementTre as ET

然后ET.function()来使用

第二个是ElementTree对象，获取方法

tree=ET.parse(文件或者xml字符串),

tree即ElementTree对象，常用的方法有

getroot() ：获取根元素

find(match) :找到顶层的第一个和match配对的元素

findall(match): 找到所有匹配的子元素

第三个是Element对象，即元素，也是最重要的

ElementTree调用函数的返回值通常是Element元素，其常用的方法有

tag: 获取tag值

text ：获取元素的文本内容

attrib :获取元素的属性，通常是字典数据类型，上边提到过，如{"ID":"07509876"}

getchildren() :获取元素的子元素

更多的资料查看官方文档：[here](http://docs.python.org/library/xml.etree.elementtree.html)
�元素的子元素

更多的资料查看官方文档：[here](http://docs.python.org/library/xml.etree.elementtree.html)
