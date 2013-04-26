---
author: admin
comments: true
date: 2011-09-26 19:44:44
layout: post
title: vim中用Zen Coding编写HTML
wordpress_id: 1800
categories:
- PROGRAM
---

在vim里编写HTML，<a href="https://raw.github.com/mattn/zencoding-vim/">zencoding.vim</a>是一个非常理想的插件

vim.org主页：[http://www.vim.org/scripts/script.php?script_id=2981](http://www.vim.org/scripts/script.php?script_id=2981)

**安装方法：**

    cd ~/.vim

    unzip zencoding-vim.zip

还有其他安装方法，可以参考主页里的方法和本页14点

**使用方法**：基本上是[英文版](https://raw.github.com/mattn/zencoding-vim/master/TUTORIAL)的翻译

1 **展开缩写**

输入
    div>p#foo$*3>a，按下'<c-y>,'

结果

    <div>
    <p id="foo1">
    <a href=""></a>
    </p>
    <p id="foo2">
    <a href=""></a>
    </p>
    <p id="foo3">
    <a href=""></a>
    </p>
    </div>

2 **嵌套代码**

输入

---------------------
    test1
    test2
    test3
---------------------

然后用shift+v把所有的代码选中，按下'<c-y>,'

在状态栏下会有Tag：提示，输入ul>li*  
结果

<ul>
<li>test1</li>
<li>test2</li>
<li>test3</li>
</ul>

如果在Tag：提示附近输入 blockquote  
结果

---------------------
<blockquote>
    test1
    test2
    test3
</blockquote>
---------------------

3 **选择下一层标签** ，输入模式下输入<c-y>d  
4 **选择上一层标签**，输入模式下输入<c-y>D  
5 **移动到下一个编辑点**，输入模式下输入<c-y>n  
6 **移动到上一个编辑点**，输入模式下输入<c-y>N  
7 **更新img大小**  
移动光标到

    ---------------------
    <img src="foo.png" />
    ---------------------

输入<c-y>i,编辑大小，得到结果

    ---------------------
    <img src="foo.png" width="32" height="48" />
    ---------------------

8 **合并行**

    ---------------------
    <ul>
    <li></li>
    <li></li>
    <li></li>
    </ul>
    ---------------------

选择其中的任意一个包含<li> 标签的行，按下“J” ,结果

    ---------------------
    <ul>
    <li></li><li></li><li></li>
    </ul>
    ---------------------

9 **移除tag**  
将光标移动到<a>块上

    ---------------------
    <div>
    <a>cursor is here</a>
    </div>
    ---------------------

输入'<c-y>k'，结果

    ---------------------
    <div>

    </div>
    ---------------------

原地不动地输入'<c-y>j'，结果

    ---------------------

    ---------------------
啥也没有了吧

10 **切割和组合Tag**

移动光标至block块
    ---------------------
    <div class="foo">
        cursor is here
    </div>
    ---------------------
输入模式下输入'<c-y>j'
    ---------------------
    <div class="foo"/>
    ---------------------
原地不动地在输入'<c-y>j'
    ---------------------
    <div class="foo">
    </div>
    ---------------------

11 **将代码转换成注释**

移动光标至需要修改的块
    ---------------------
    <div>
        hello world
    </div>
    ---------------------
输入模式下输入 '<c-y>/'
    ---------------------
    <!-- <div>
        hello world
    </div> -->
    ---------------------
原地不动地再输入 '<c-y>/'，看，又回来了
    ---------------------
    <div>
        hello world
    </div>
    ---------------------

12 **将URL装换成引用**

输入一个http://格式的链接
    ---------------------
        http://www.google.com/
    ---------------------
输入 '<c-y>a'，结果
    ---------------------
    <a href="http://www.google.com/">Google</a>
    ---------------------

13 <strong>从URL中创建引用的文本</strong>
    ---------------------
        http://github.com/
    ---------------------
输入 '<c-y>A'，自动在网络上查询必要的资源并显示，怎么样，方便吧
    ---------------------
    <blockquote>
    <a href="http://github.com/">Secure source code hosting and collaborative development - GitHub</a><br />
    <p>How does it work? Get up and running in seconds by forking a project, pushing an existing repository...</p>
    <cite>http://github.com/</cite>
    </blockquote>
    ---------------------

14 **安装zencoding.vim**

    # cd ~/.vim
    # unzip zencoding-vim.zip
        or if you install pathogen.vim:
    # cd ~/.vim/bundle # or make directory
    # unzip /path/to/zencoding-vim.zip
        if you get sources from repository:
    # cd ~/.vim/bundle # or make directory
    # git clone http://github.com/mattn/zencoding-vim.git

15 **定制**

    ---------------------
    # cat >> ~/.vimrc
        let g:user_zen_settings = {
    \ 'php' : {
    \ 'extends' : 'html',
    \ 'filters' : 'c',
    \ },
    \ 'xml' : {
    \ 'extends' : 'html',
    \ },
    \ 'haml' : {
    \ 'extends' : 'html',
    \ },
    \}
    ---------------------
      let g:user_zen_expandabbr_key = '<c-e>'//即"<c-y>,"都变成<c-e>了

      let g:use_zen_complete_tag = 1
