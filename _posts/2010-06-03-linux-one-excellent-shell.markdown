---
    author: admin
    comments: true
    date: 2010-06-03 20:13:57
    layout: post
    slug: linux-one-excellent-shell
    title: linux下一款优秀的shell
    wordpress_id: 245
    categories:
- PROGRAM
---

对于学习和使用linux的人来讲,掌握强大和伟大的CML是必要的,掌握一款合适自己的shell(命令解释器)是非常必须的

通常大多数linux发行版默认的shell是bash(Bourne Again shel),他的优点是

直观而又灵活,或许是初学者的最明智选择同时对高级和专业用户来说也是一个强有力的工具

下面介绍一款同样优秀的shell-----Friendly Interactive Shell,简称为fish,他的优点是

提供简明的语法，显著改善了用户体验。与其他 shell 一样，fish 也提供重定向、快捷方式、globbing（即通配符的展开）、子 shell、制表符补全和变量。但是，与其他 shell 不同，fish 还提供颜色编码的 CLI、功能丰富的命令行编辑器和大量文档。同时fish兼容bash的大部分命令,只有少数快捷键不一致.

    fish安装:

    sudo apt-get install fish

使fish成为默认的shell:

    sudo usermod -s /bin/fish 用户名

注销后进入系统,打开终端模拟器,提示您[![](/media/images/2010-06-03-linux-one-excellent-shell/Screenshot-300x65.png)](/media/images/2010-06-03-linux-one-excellent-shell/Screenshot-300x65.png)

可以输入bash或者exit来退回到默认的shell.

