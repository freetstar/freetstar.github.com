---
    author: admin
    comments: true
    date: 2011-04-28 12:19:00
    layout: post
    slug: '%e5%ad%a6%e4%b9%a0python%e7%9a%84%e5%88%a9%e5%99%a8-ipython-part-i'
    title: 学习Python的利器-IPython Part I
    wordpress_id: 1692
    categories:
- python
---

Python的优点之一是具有可交互性的解释器，即Python shell，对于新生或者一些老鸟来说，能交互地在类似命令行上输入自己的程序并让Python进行解释执行，是十分方便的。通过Python解释器还可以很方便的学习Python模块的帮助文档，通常linux下打开交互式python的方法是敲入Python,然后回车，其实python自带的交互式解释器功能弱爆了，下面我给大家推荐**IPython**

** ** IPython的优点：

不仅具有卓越的Python Shell具有的特点，同时IPython提供了给予控制台命令环境的定制功能，可以十分轻松地将交互式Python Shell包含在各种Python应用中，如果你不介意的话，还可以把IPython当作zsh，bash之类的使用。IPython可以使用TAB补全，历史命令定制，语法高亮，shell语法。要知道许多系统管理员利用它来管理Linux操作系统。

IPython的社区：

邮件列表：[http://lists.ipython.scipy.org/mailman/listinfo/ipython-user](http://lists.ipython.scipy.org/mailman/listinfo/ipython-user)

IPython安装方法：

1各个发行版使用自带的包管理软件，安装IPython即可

2源代码安装:

    wget http://ipython.scipy.org/dist/0.10.2/ipython-0.10.2.tar.gz

    tar zxvf ipython[TAB]

    cd ipython[TAB]

    python setup.py install

IPython 使用：

对普通功能就赘述了，大家可以摸索下。着重描述下IPython自己独特的东西

安装好后第一次在命令行输入IPython,会提示您是第一次使用IPython，直接回车即可

** IPython的配置文件：**

通常在当前用户的主目录下，在ipython目录下有一个ipy_user_conf.py的配置文件，在文件里你可以象vim，zsh，bash那样指定你要的配置

**不一样的In和Out**（^_^不许邪恶的遐想）

小例子，在IPython命令行输入：

In [1]: a=1

In [2]: print a

1

In [3]: a

Out[3]: 1

In [4]: print In

['\n', u'a=1\n', u'print a\n', u'a\n', u'print In\n']

实际上每个命令之间是有一行空行，我这里为了方便给去掉了。可以观察下IPython的提示符，"In[数字]:" 数字表示输入的第几个命令，"OUT[数字]："对应第几个命令的输出结果。所有的命令输入都被保存到In列表中，实际上In是一个列表数据类型，Out是一个字典数据类型，这里就不多做介绍了

**TAB补全你要的**

例子：

In [1]: import os[TAB]

    os  os2emxpath  ossaudiodev

In [2]:os.pa[TAB]

    os.pardir  os.pathconf  os.pathsep 

    os.path  os.pathconf_names

IPython提供两类自动完成功能：完成与菜单完成.默认的是完成，即列出所有的可能性列表，菜单完成即是不提供列表，而是直接你TAB时，切换到下一个可供选择的选项中。

注：

1 通过import 自动完成功能所列出的项都是模块(import目的就是导入模块嘛，ipython智能吧)

2 其实默认的python shell也是支持TAB补全的，方法：

    import rlcompleter,readline

    readline.parse_and_bind('tab:complete')

**魔力编辑**

不同于Shell面向行的输入方式，也不同于文本编辑器，魔力编辑上上述的折中，好处是利用手边的资源，可以方便的编辑代码，同时也可以直接交互执行命令

**魔力函数**

IPython会将任何第一个字幕为%的行，视为对魔力函数的调用。魔力函数以%为前缀，参数中不包含括号或者引号

查看所有可用的魔力函数，方法1：输入lsmagic 方法2：输入%[TAB] (TAB是用来敲的)

    magci自己的magic，输入maigc，可以得到一个帮助文档，你可以象shell中的less命令那样阅读和操作这个文档，文档中有关于各个magic函数的用法，参数等等 

获得魔力函数的帮助方法:%魔力函数 ? 

文章主要参考《Python UNIX和Linux系统管理指南》一书
