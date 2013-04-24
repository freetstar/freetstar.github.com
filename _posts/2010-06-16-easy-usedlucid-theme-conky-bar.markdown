---
    author: admin
    comments: true
    date: 2010-06-16 21:10:24
    layout: post
    slug: easy-usedlucid-theme-conky-bar
    title: 简单易用的lucid 主题conky栏
    wordpress_id: 653
    categories:
- ubuntu
- 转载翻译
---

[![](http://lh5.ggpht.com/_FJH0hYZmVtc/TBjJdF40qwI/AAAAAAAAIfY/J3feZjZRHNw/124144-1%5B3%5D_thumb%5B9%5D.jpg)](http://lh5.ggpht.com/_FJH0hYZmVtc/TBjJdF40qwI/AAAAAAAAIfY/J3feZjZRHNw/124144-1%5B3%5D_thumb%5B9%5D.jpg?imgmax=800)

这就是可爱漂亮的lucid conky栏.

安装方法:

1 运行命令 sudo apt-get install conky 

2 下载lucid conky主题 [here](http://gnome-look.org/content/show.php/Conky+Ubuntu+Lucid+Theme+-+English?content=124209&PHPSESSID=54fd24f0db9865e8c44e3ddaa19b6393),并解压

3 打开主文件,按下Ctrl+H来显示隐藏文件

4 将上述解压后的文件复制到主文件下

5 按下ALT+F2,运行conky -c /home/YOURUSERNAME/.conkytheme/conkyrc &,看到漂亮的conky栏了吧 ^ ^

6 打开系统-首选项- 启动应用程序,点击添加,名称和注释任意,命令即上述命令,这样将conky增加开机启动应用程序中

补充:

作者[Veoduendes](http://gnome-look.org/usermanager/search.php?username=Veoduendes)之前写的conky比较难配置,不过现在在作者的努力下,已经有了良好的配置向导

配置向导的一些特色:

可以调整conky来适应屏幕  

可以选择要展示的元素  

可以嵌入脚本  

保存设置,并顺序装载  

西班牙语和英语两种语言

配置向导下载:  

    ubuntu 32位和64位:[http://code.google.com/p/conkywizard/](http://code.google.com/p/conkywizard/)

若使用新的conky配置,运行conky -c ~/.ConkyWizardTheme/ConkyWizardTheme -q &,相应的开机启动也要做同样的改变

VIA{[OMG!Ubuntu](http://www.omgubuntu.co.uk/2010/06/easy-to-use-lucid-themed-conky-bar-now.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed:+d0od+(Omg!+Ubuntu!))}

