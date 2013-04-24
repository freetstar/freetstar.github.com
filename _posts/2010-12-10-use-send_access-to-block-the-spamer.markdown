---
    author: admin
    comments: true
    date: 2010-12-10 13:34:52
    layout: post
    slug: use-send_access-to-block-the-spamer
    title: 小记：给postfix设置黑名单
    wordpress_id: 1530
    categories:
- 服务器
---

公司的邮箱近几天总是收到某一个QQ邮箱的垃圾邮件，公司的MTA用的是postfix（postfix现在很流行啊），我简单记录下怎么给postfix设置黑名单：
Step 1 在主配置文件中增加限制语句
    #vi /etc/postfix/main.cf
在最后添加这样的一句话
    smtpd_sender_restrictions = check_sender_access hash:/etc/postfix/sender_access
    //即限制往本机发邮件的人
Step 2 编辑黑名单
    #vi /etc/postfix/sender_access
    spamer1@expample.com  REJECT
    spamer2@expamle.com   REJECT
//其中对应的邮箱设置成实际在打扰你的邮箱即可
Step 3 转换数据库模式
    #postmap /etc/postfix/sender_access
Step 4 重新加载postfix服务
    #service postfix reload
Step 5 做必要的测试
用自己的邮箱给公司的邮箱发一封邮件，若提示退信则成功

学习资料：[http://blog.chinaunix.net/u/166/showart_691664.html](http://blog.chinaunix.net/u/166/showart_691664.html)
推荐：postfix中文权威指南
