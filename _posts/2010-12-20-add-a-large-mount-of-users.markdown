---
    author: admin
    comments: true
    date: 2010-12-20 11:10:57
    layout: post
    title: 给Linux系统添加大量用户的方法
    wordpress_id: 1540
    categories:
- PROGRAM
---

方法一：
给系统添加大量用户，并初始化密码
    # cat -n add.sh     
    1 #!/bin/bash
    2 echo -e "Beginning addusers now!!!\n "
    3 for ID in `seq 1 10`
    4 do
    5         useradd -s /bin/bash temp$ID
    6         echo "passwd"|passwd --stdin temp$ID
    7 done
可以根据自己的情况给用户添加选项，同时也可以将用户列表写到某个特定文件中去，$（cat userlist）来读取    
#另外redhat4U8下的useradd和adduser是一个东东，不存在神马传说中的区别，如果您有兴趣的话，可以围观下这个http://hi.chinaunix.net/?uid-20766364-action-viewspace-itemid-34721                                                                                            
方法二：
生成一个类似于/etc/passwd格式的文件，注意用户ID和组ID的设置，第二列是密码
    cat userlist.txt
        test123:test:1000:1000:/home/test123/:/sbin/nologin
        test124:test:1001:1001:/home/test124/:/sbin/nologin
然后运行
    newusers userlist.txt
    cp -r /etc/skel/* /home/{test123,test124}

方法三:
手动添加大量用户
    vi /etc/passwd 
    test125:x:840:840::/home/test125:/bin/bash
    vi /etc/group
    test125:x:840:

创建用户的主目录并设置权限
    mkdir /home/test125;chmod 700 /home/test125
    chown test125:test125 /home/test125
拷贝模板
    cp -r /etc/skel/* /home/test125
设置密码
    passwd test125

