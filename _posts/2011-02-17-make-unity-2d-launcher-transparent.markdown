---
author: admin
comments: true
date: 2011-02-17 14:29:15
layout: post
slug: make-unity-2d-launcher-transparent
title: 将ubuntu10.10下的unity 2D launcher变透明
wordpress_id: 1607
categories:
- ubuntu
- 转载翻译
---

准备材料：
1 一张和显示器分辨率相当的壁纸，我的14寸本是1024x768,最后留一个备份
2 对壁纸剪切，抛去最左侧下方的一个长方形，这个长方形的宽度是58px，是因为launcher的宽度是58px，长度是768-24=744px，另存为1.png
运行命令： 
·[code language="bash"]sudo mv 1.png /usr/share/unity/themes/launcher_background_middle.png[/code]
当然源图片可以自己指定，目的地址不可以改变。 然后注销，重新登录进来看是否生效
注： 
由于unity2d更新频繁，可能导致背景在更新时恢复原样，用以下方法阻止更新
[code language="bash"]sudo dpkg-divert /usr/share/unity/themes/launcher_background_middle.png[/code]
当然，还可以用以下方法恢复初始背景图片
[code language="bash"]sudo dpkg-divert --remove /usr/share/unity/themes/launcher_background_middle.png[/code]
[code language="bash"]sudo apt-get install --reinstall unity-asset-pool[/code]
来自{[omgubuntu](http://www.omgubuntu.co.uk/2011/02/how-to-get-a-transparent-launcher-in-unity-2d/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed:+d0od+(Omg!+Ubuntu!))}
