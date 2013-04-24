---
    author: admin
    comments: true
    date: 2011-05-08 02:39:01
    layout: post
    slug: python-is-cool-and-perl-is-not-especially-for-cc-programmers
    title: Python很酷，尤其对C/C++程序员来说是这样，然而Perl却不是
    wordpress_id: 1697
    categories:
- PROGRAM
---

python是一个很cool的脚本编程语言，perl很有用但是用起来很痛苦。对于几乎所有的任务，python有充足的理由是第一选择，尤其是对那些不熟悉perl或者python的C/C++程序猿们。对那些了解perl的C/C++程序员来说，python也堪称一个更好的选择

WHY？！

看了以下例子你就明白:

例子1：读取整个文件
    perl

    my $text = do { local( @ARGV, $/ ) = $file ; <> } ;

我看了半天是没看懂啥意思，ARGV在这里是干嘛的，来看看我找的其他例子

    local( *FH ) ;
    open( FH, $file ) or die "Problem\n"
    my $text = do { local( $/ ) ; } ;

另外一个

    my $holdTerminator = $/;
    undef $/;
    my $buf = ;
    $/ = $holdTerminator;
我该说什么了，perl你不尴尬嘛

    python

fileContents = file("filename").read()

例子2：定义一个func函数，返回int值，第四个参数默认值为0

    C++

int func(int parm1, int parm2, int parm3, int parm4 = 0);

    perl


    sub func
    {
    my $parm1 = shift;
    my $parm2 = shift;
    my $parm3 = shift;
    die "Usage: func(parm1, parm2, parm3, parm4 = 0)"
    unless defined($parm3);
    my $parm4 = shift || 0;
    ...

看着是不是怪怪的，即使你会用perl。用如此笨拙的代码来实现这么简单的东西。die用来处理参数，
perl不担心你是否没有传入参数或者传了10个以上的参数。perl中函数中的变量默认是全局的，需要用my设置为局部变量。
要知道大部分c/c++ 程序猿可不习惯这个


    python

        def func(parm1, parm2, parm3, parm4 = 0):
    ...
    python会自己处理参数个数，并且设置参数默认值，而且函数里默认的值是局部变量哦

例子3：打印当前的进程名，并跟随一个换行符

    C++

cout < < argv[0] << '\n';

    perl


    print "$0\n";
看着挺顺眼的是不，$0是进程的名字。或许你会尝试用$ARGV[0]代替$[0]，要知道C++里我是能用ARGV[0]表示进程名的，但是结果却不是你要的
    perl中ARGV仅仅包含要处理的参数，而不包括进程名（译者说，实际上shell一般默认$0也是进程名的


    python


    print sys.argv[0]
#好吧，让你比较困惑的是还要加一个sys


例子4：文件迭代，代开一个in.txt文件，对每行进行迭代操作

    C++


    ifstream infile("in.txt");
    const int MAX_LINE_LEN = 256;
    char line[MAX_LINE_LEN];
    while(infile.getline(line, MAX_LINE_LEN))
{
... do something with line
}
//要创建一个buffer来存放每一行


    perl


    open(INFILE, "in.txt") || die 'Couldn't open "in.txt"';
    while()
    {
    ... do something with $_
    }
open看起来挺好的。。加了个die代码之后变得丑了


    Python


        infile = open("in.txt")
        for line in infile:
    ... do something with line
好简洁吧


例子5：检查字符串的开头是否以'H'开始，假设这个字符串是从文件迭代中获得的

    C++


    if(line[0] == 'H')
    {
    ...

    perl

    if(substr($_, 0, 1) eq 'H')
    {
    ...
    perl中没有字符串操作符，你要调用substr函数，而且等于是eq而不是==


    python

    if line[0] == 'H':
...
    c++程序猿更习惯这个吧
或者

    if line.startswith('H'):


例子6：将一个列表传入函数中，使其能够在函数中修改它，而不是得到列表的拷贝
    C++

    void addItem(vector<string>& theList)
{
    theList.push_back("xyz");
}

    vector<string> aList;
    aList.push_back("abc");
    addItem(aList);
这是通过C++中的引用传值进行的


    Perl

    sub addItem
    {
        my $listRef = shift;

        push(@$listRef, 'xyz');
    }

    my @aList = ('abc');
    addItem(\@aList);
这里用到了很多Perl特有的特点，用\表示alist是通过引用传值的等等。其实比较复杂


    Python

    def addItem(theList):
        theList.append('xyz')

    aList = ['abc']
    addItem(aList)
python中一切是通过引用传递的

还有以下例子：
[Array and string length](http://www.strombergers.com/python/python_perl_length.html)
[Print a list that belongs to a hash](http://www.strombergers.com/python/python_perl_print_hash_ref.html)
[Trim whitespace from a string](http://www.strombergers.com/python/python_perl_whitespace.html)
[Classes](http://www.strombergers.com/python/python_perl_class.html)
[Inheritance](http://www.strombergers.com/python/python_perl_inheritance.html)
[Magic](http://www.strombergers.com/python/python_perl_magic.html)
[Exceptions](http://www.strombergers.com/python/python_perl_exceptions.html)
[Assert](http://www.strombergers.com/python/python_perl_assert.html)
[Code Maintenance](http://www.strombergers.com/python/python_perl_maintenance.html)

来看看各路大神怎么推崇Python的吧
["Perl? Ha, ha, ha. Try Python" O'Reilly ad.](http://www.strombergers.com/python/perl_ha_ha_ha.html) 
[Bruce Eckel talks about Python](http://www.artima.com/intv/aboutmeP.html)当你发现Python的高效时，你会觉得我为什么要把生命中的其他时间浪费在其他语言上
[Why Hate Perl](http://c2.com/cgi-bin/wiki?WhyHatePerl) 为神马讨厌Perl
[Why I Promote Python](http://www.prescod.net/python/why.html)
来看看Eric Raymond的意见[Eric Raymond's "Why Python?"](http://www.linuxjournal.com/article.php?sid=3882)

原文在此：[here](http://www.strombergers.com/python/)
