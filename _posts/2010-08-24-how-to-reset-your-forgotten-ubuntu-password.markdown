    author: admin
    comments: true
    date: 2010-08-24 14:38:01
    layout: post
    slug: how-to-reset-your-forgotten-ubuntu-password
    wordpress_id: 1190
    categories:
- 问题解决
---

一：以root身份登陆

1 ）命令

如果你使用单系统，在开机的时候按下ESC键，以此来进入Grub界面。如果您是双系统的话，系统会自动进入grub界面

然后选择"recovery mode"，下一步选择"_drop to root sheel prompt"，这样你以root的身份进入系统_

2 ）高级方法

有时候进入grub之后并不能找到"recovery mode"，这种情况下，选择默认的grub启动项（通常是第一个），按"E"键来编辑Grub选项，找到包含

    ro quiet splash的行，用 rw init=/bin/bash替换，然后按Ctrl+X（或者B键）来以修改后的Grub加载系统

这样，你以root身份登陆系统，然后开始重设你的密码。

二：重设密码

1）用以下命令重设密码：

    psaawd user

//user是你要对其重设密码的用户的用户名

2）将你所做的改动保存到磁盘上

    sync

3) 重启系统

    reboot -f

三：正常使用您的系统吧

    via{[HERE](http://www.panoet.com/)}

