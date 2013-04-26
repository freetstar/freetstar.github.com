---
    author: admin
    comments: true
    date: 2011-08-31 16:56:51
    layout: post
    title: agent2d librcsc 静态编译方法
    wordpress_id: 1780
    categories:
- Opensource
---

今年国赛果不其然大部分队伍都开始尝试用agent2d和librcsc作为球队底层来开发2D的队伍，毕竟在“老师”压迫下，成绩最重要，而拿agent2d和librcsc开发2D球队相对来说是比较容易出成绩的。师大对这个底层做了近“3年”，对这个底层和平台有了一些自己的认识和理解，如果有时间和精力的我想集中人手作几份文档出来，这篇文章说一下agent2d和librcsc静态编译的方法，这里要感谢09年代表师大参赛的李辰:)

**一  librcsc**

1) 如果以前有对librcsc源码包编译安装至系统的默认位置,即/usr/local/lib，则运行下面的命令来移除已经安装好的库和编译好的文件
    sudo make uninstall
    make distclean

（如果当初用来编译安装的源码包被删除了，则找一份新的librcsc重新安装下，然后再运行上面2个命令就行）

2) 然后对librcsc静态编译
    2.1 ./configure --prefix=$HOME/rcsc --disable-shared --enable-static
    2.2 make
    2.3 make install

**二   agent2d**
1) 如果以前有对agent2d上层进行编译，则首先运行下面2条命令把以前的可执行文件和Makefile等清空
    1.1 make uninstall
    1.2 make distclean
2) 然后重新编译安装
    2.1 ./configure --with-librcsc=$HOME/rcsc
    2.2 make

有问题欢迎留言~
