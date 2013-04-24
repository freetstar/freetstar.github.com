---
    author: admin
    comments: true
    date: 2011-07-16 18:52:40
    layout: post
    slug: ubuntu-eclipse-cdt
    title: ubuntu下用Eclipse搭建C++开发环境
    wordpress_id: 1758
    categories:
- PROGRAM
---

**第一步:下载Eclipse包**

32位:[链接](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/indigo/R/eclipse-linuxtools-indigo-incubation-linux-gtk.tar.gz)   64位:[链接](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/indigo/R/eclipse-linuxtools-indigo-incubation-linux-gtk-x86_64.tar.gz) 注意选择的是[Eclipse IDE for C/C++ Linux Developers (includes Incubating components)](http://www.eclipse.org/downloads/packages/eclipse-ide-cc-linux-developers-includes-incubating-components/indigor)这个IDE

不推荐使用Ubuntu源中的Eclipse

**第二步:解压缩下载好的Eclipse包至/opt目录**

    sudo tar zxvf eclipse-linuxtools-indigo-incubation-linux-gtk-x86_64.tar.gz -C /opt

**第三步:创建Gnome2的面板快捷方式**

在panel上单击右键添加自定义的程序,

名称:Eclipse

命令:/opt/eclipse/eclipse

图标: /opt/eclipse/icon.xpm
**第四步: 配置CDT**

打开Eclipse,打开Help->Install New Software,然后点击Add按钮,在弹出的对话框中
Name项填入CDT

Location项填入**[**http://download.eclipse.org/tools/cdt/releases/indigo**](http://download.eclipse.org/tools/cdt/releases/indigo)**

点击Ok按钮,在下边出现的列表中,

第一个CDT Main Features基本都要安装

第二个中务必要把包含GNU字眼选择安装

然后根据提示选择下一步,接受协议,并且安装,安装成功后就restart eclipse

**第五步:配置Autotools支持**

基本上同第四步一致:

Name项填入Autotools

Localtion项输入:http://download.eclipse.org/technology/linuxtools/update

点击Ok按钮,在下边出现的列表中,将此选项选中,然后安装即可

Autotools support for CDT (Incubation) 3.0.0.201106060936 

