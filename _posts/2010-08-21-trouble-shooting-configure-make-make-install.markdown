---
    author: admin
    comments: true
    date: 2010-08-21 15:23:21
    layout: post
    title: 解决./configure ，make，make install的报错
    wordpress_id: 1180
    categories:
- 问题解决
---

Linux下从源代码下编译安装一个软件有时候会报错，遇到一些麻烦。有些情况即使你用了很多方法去尝试解决，但问题依然存在，那怎么办呢？本教程教你怎么解决Linux软件编译时遇到的问题

注意：编译安装一个软件不会被系统的包管理系统记录信息，这对于卸载和记录软件的行为都是不利的，建议您尽量使用打包好的包(.rpm .deb)

我们分3类错：

    ./configure 错误

    make 错误

    make install 错误

识别这些错误应该是很简单的：./configure的错误会被configure脚本输出，make和make install错误也应该很明显被识别。下面分类说明3种错误和解决办法：

一：  ./configure 错误

以下根据错误出现频率一一道来。第一个是经常性出现错误（是选择性的）。（）中表示可选，OR表示有一致的解决办法，<>表示内的文字由具体情况具体表示

1 。(configure:) (error:) <somename> (<someversion> (or higher)) not found. (Please check your installation!) OR checking for <somename>... (configure:) (error:) not found. OR (configure:) (error:) <somename> (<someversion> (or newer)) is required to build <package-you're-trying-to-compile>

这表明<somename>的包的-dev或者-devel版本没有安装。请使用你发行版的包管理器（或者其他寻找和安装包的方法）来寻找<somename>包并且安装，如果可能的话安装-dev 或者-devel版本

如果-dev 或者-devel版本已经安装了，或者不存在，查看一下已经安装的版本号。它足够高吗？是不是比<someversion>要低，这样你要常识升级这些包。如果还不行的话，你可以尝试编译你要编译软件的以前的版本。老版本通常使用老版本的库/程序

如果./configure 提示找不到的是一个库（通常提示lib<something>）,并且你确定了已经安装了正确版本的库，现在尝试找到你的库文件的位置。如果库文件路径不包括在你的ld.conf 文件（通常是/etc/ld.conf或者是/etc/ld.so.conf）你应该在此文件中添加，然后运行ldconfig命令（/sbin/ldconfig）需要注意的是：运行ldconfig 通常需要root权限。如果您不知道怎么办，待回看一下下Make install错误的第一点

记：如果您没有修改ld.conf文件的权限，您还可以将库文件路径添加到LD_LIBRARY_PATH变量中。当然这是个笨方法，也不是最好的方法，但是当你没有其他选择时，你只好这么做了：

    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/your/library/directory"

当然，将您的库文件路径。注意当您运行编译好的软件时，LD_LIBRARY_PATH必须包含您的库文件夹路径

2。(configure:) (error:) cannot find header (file) <somename>.h OR (configure:) (error:) (header) (file) <somename>.h missing! OR <similar>

configure脚本提示找不到".h文件。这个错误和上面的错误是类似的，它也要求您安装特定包的-dev或者-devel版本。然而，它并不能清楚显示你需要安装哪个包，而<somename>会是一个特别广泛的包，你可以尝试在web上搜索<somename>.h看它属于那个包，然后尝试用您系统的包管理器这安装这个包（如果可能的话，同时安装它的-dev或者-devel版本 ）

3。 (configure:) (error:) no acceptable cc found in <somedirectories>

您没有安装gcc或者cc环境变量没有设置。用包管理器检查gcc是否已经安装，如果没有的话，安装它。如果安装了尝试用这个命令

    export CC="/usr/bin/cc"

如果要永久性的话，你可以将这个命令添加的/etc/profile中（当任何用户登陆进来时会执行这个文件里很多的命令）这样，您以后就不要再设置了。

4。(configure:) (error:) C++ preprocessor "/lib/cpp" fails sanity check

您的g++包或者失踪了或者conrrupted了，请检查您的包管理器（或者其他寻找和安装包的方法）去寻找g++和安装相应的包。注意，许多发行版并不称为g++，比如说，Fedora，在yum源里用gcc-g++来表示g++包。如果您找不到g++，你可以寻找c++，cpp和/或者gcc

5。(configure:) (error:) C++ preprocessor "CC (-E)" fails sanity check

这个是libtool的一些特定有bug的版本，它使configure脚本检查libtool支持的编辑器。这个最快的解决办法就是安装g++（解决办法如上）

二：  Make 错误

make错误通常很具体，并不能够写一个抽象的总结。我会给你一些可能有所帮助的东西 

如果您在使用gcc 4编译（使用gcc -dumpversion来查看）（我的补充gcc --version也可），可以尝试用旧版本。首先，请确定包的旧版版已经安装了。可以这样做

    ls /usr/bin/gcc*

如果返回有这个

    /usr/bin/gcc /use/bin/gcc32

这样的话，你可以用gcc32这个老的版本命令来编译。如果不行的话，请用您的包管理器来安装旧版本的gcc（通常是称之为compat-gcc或者gcc-<versionbumber>）安装之后，您会通过上边的命令上面边命令检测到已经安装的gcc。让./configure make make install 使用gcc版本的方法如下：

    CC="/usr/bin/gcc32" ./configure 
    CC="/usr/bin/gcc32" make
    CC="/usr/bin/gcc32" make install

注意：大多数情况下，您可以不带/usr/bin ，只输入gcc即可。然而，一些不标准的Makefikes可能采取不同的方法。因此，写全路径是最安全的方法。当然，具体/usr/bin/gcc32要用您具体的路径代替

有时候make报的错只是由于一个bug引起的。尝试获得最新版的软件（使用CVS或者SVN或者源，或者下载每日快照）并且常识编译查看时候他们已经修复了bug。

    make报的错还可能由特定库/程序的错误版本造成的。特别是特别新或者旧的软件会遇到这个问题。查看以下软件的依赖（他们通常在软件的网站上显示出来）拿那些包的版本与你系统里的包的版本对比（他们通常可以用系统的包管理器查看）如果电脑中的包版本比网站要求的版本的高，你可能在编译一个老版本的软件。如果你确实需要编译他，尝试降低依赖。然而，寻找其他方法来安装软件或者找一个替代品是最好的方法。如果您系统的特定软件版本比要求的版本低，您可以或者编译一个bleeding-edge包，或者您的发行版太旧了，或者都有包括。。。你应该常识更新需要的库/软件，或者编译一个老版本的程序。还有，查看是否有针对您发行版的包存在着。安装这样的包比常识安装这些错误会很麻烦的。

还有就是在网络中搜索您特定的错误，如果您找不到任何有用的东西，可以省略行号（他们根据版本号不一样），版本号码（你可以用"*"来代替他们，如果他们包含在文件内部）非字母的字符比如说引号，他们影响搜索引擎的搜索。你可以在很多mailing列表上找到很多信息。一些情况下，还会有源代码的补丁。可以这样来打补丁

    patch -Npl -i <patchfile>

注意当你打补丁时你应该在源代码路径中

三：  Make install 错误 

这些错误理解起来很容易，但是我还是列一下吧～通常有两大失败原因 

1.你没有root权限。尝试用sudo make install命令或者使用su命令成为root用户。

    sudo make install

提示输入密码时，输入您自己的密码或者系统管理员的密码

    su

这样就可以成为root用户，提示输入密码时，要输入系统管理员的密码。这样成为root之后，只需要运行make install命令即可。然后Ctrl+D或者exit，logout命令来退出。对于sudo来讲的话，它只用root权限来运行一次命令，并不会以root身份登录的。

2.  您编译的包没有安装目标。这样，您就需要将编译好的二进制文件放到bin文件夹中。在源代码路径下运行ls命令，可执行文件应该会以亮绿色显示的。您需要将这些文件拷贝到/usr/bin或者/usr/local/bin 中，至于哪个就是看您爱好了。命令大致如下

    cp <executeablefile> /usr/bin

然后，如果使用多次，可能会是您的/usr目录看起来一团糟。您可以将可执行文件所在的路径添加到您的PATH路径中。进入到可执行文件的路径，执行pwd命令查看全路径名

然后将pwd命令的输出放到这个命令中

    export PATH="$PATH:<pwdoutput>"

现在，运行可执行文件，它就开始工作了。将上述命令添加到您的/etc/profile文件中，这样可永久保存。

我同意这样做不太好，不够简洁和方便。但是有时候开发者没有时间开创建一个安装目标。我们不应该对此感到气氛。。。想想他们为了让我们使用有用和有趣的程序而做出的努力吧

其他问题：

这是一些其他常见的问题，并附上解决办法：

1.一切正常，但是当我要运行我刚才安装的软件时，bash提示找不到。这通常是由于make install将每个东西都安装在了/usr/local或者/opt/<packagename>.检查一下make install 将文件复制到了哪里。可以将可执行文件的路径添加到PATH路径中（下面的例子假设您装包安装在了/usr/local）

    export PATH="$PATH:/usr/local/bin"

当然，您可以用相应的路径来代替/usr/local/bin文件夹。如果希望不用再输入的的话，将输入命令添加到您的/etc/profile中，这样您就不需要重复输入了另外，你可以在configure的时候，控制包安装在哪个目录。。。比如说：

./configure --prefix=/usr

您可以将/usr用您想安装的目标路径代替。注意，您只是在设置prefix，二进制文件会安装杂prefix子目录下，头文件也是～当使用了上述的frefix，你可以在/usr/bin找到二进制文件

2.当我想安装一个老版本的包，我在互联网上找打不到源代码包。然而，你还是有个小希望的。尝试搜索您想寻找的rpm的版本，下载相应的src rpm包。并且解包

    rpm系：rpm2cpio <rpmfile>|cpio -idv

这样，您就可以使用从rpm里解压缩出来的源文件

原文： [http://www.linuxtutorialblog.com/post/troubleshooting-configure-make-and-make-install-tutorial](http://www.linuxtutorialblog.com/post/troubleshooting-configure-make-and-make-install-tutorial)

我记：  

1 。configure程序带有很多参数，可以通过 ./configure --help 查看详细内容,通常位于前面的是常规configure的参数说明，末尾是该程序的可用参数说明。  

2。pkg-config编译问题请参阅：[http://www.linuxeden.com/forum/viewthread.php?tid=164524](http://www.linuxeden.com/forum/viewthread.php?tid=164524)

3 。我喜欢以编译的方式安装软件。。虽然包管理系统没办法记录。。

4。推荐这篇文章，也很不错  

[http://www.linuxeden.com/forum/viewthread.php?tid=164524](http://www.linuxeden.com/forum/viewthread.php?tid=164524) 

