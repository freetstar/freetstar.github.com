---
    author: admin
    comments: true
    date: 2011-01-07 22:42:34
    layout: post
    title: 一些积累的CLI Tricks
    wordpress_id: 1558
    categories:
- PROGRAM
---

删除文件中的空行
    grep . oldfile >newfile
    grep -v "^$" oldfile >newfile


压缩字符串里的空格
    tr -s " " " " strings

    scp小用：
    scp也可以在本地机器中当成cp用，如：
    cp file1 file2
    scp file1 file2
当然scp主要是用户网络传输的
    scp tem.pdf username@remotemachine:
注意：“：”，同志们可以想象下没有冒号会怎么样

充分利用alias吧
比如说：cd3 cd4
    alias cd3='cd ../..'
    alias cd4='cd ../../..'

用组合键对付长命令行
    ctrl+a 行首
    ctrl+e 行尾
    ctrl+u 光标前
    ctrl+k 光标后
    ESC+.调出上次你的命令所使用的参数
    Ctrl+R 搜索

用fc命令将上次执行过的命令放到编辑器中执行
当然也可以用Ctrl+x和Ctrl+e来执行

正用着vim了却想起来某个命令没有执行怎么办
    Solution1： 执行：！命令
    Solution2： Ctrl+z先挂起来，回来运行玩了命令再玩你

快速的给文件改后缀
    rename html htm  *.html

