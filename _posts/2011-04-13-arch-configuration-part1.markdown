---
author: admin
comments: true
date: 2011-04-13 23:06:17
layout: post
slug: arch-configuration-part1
title: arch配置文档
wordpress_id: 1661
categories:
- Opensource
---

最近新进了一台台式机




配置如下：




CPU i5-2300




内存 金士顿 DDR3-1333 单条4G




主板  微星H67MA-E35(B3)




硬盘 西数1T




显示器和电源机箱都是AOC的




罗技无线键鼠套装




显卡 i5自带的GPU




========================================================================================================




第一步就是装win7。。。有时候还是要用用windows的，主要是网银和qq连连看:)







第二步安装arch：




具体的安装过程就不多说了，我装的是x86_64,简单说下配置过程




=========================================================================================================<!-- more -->




配置源：




vi  /etc/pacman.d/mirrorlist




将其他的都保持注释或者注释掉，保留







Server = http://mirrors.163.com/archlinux/$repo/os/x86_64




Server = http://mirrors.archlinux.fr/$repo/os/x86_64




=========================================================================================================




配置用户






    
    useradd -m -g users -G audio,lp,optical,storage,video,wheel,games,power -s /bin/bash lgx







将lgx添加到这些组里，然后passwd lgx设置密码




 




安装sudo




pacman -S sudo




配置sudo




su - root




visudo




uncomment %wheel ALL=(ALL) ALL




=========================================================================================================







更新系统




sudo pacman -Syu




=========================================================================================================




配置alas




sudo pacman -S alas-utils




测试




aplay  /usr/share/sounds/alsa/Front_Center.wav







=========================================================================================================




安装显卡驱动




sudo pacman -S xf86-video-intel






    
    sudo pacman -S xorg-server xorg-xinit xorg-server-utils







sudo pacman -S mesa




注：xorg.conf 不适用于intel的显卡







=========================================================================================================







安装桌面环境




pacman -S gnome




直接以level5登录




vi /etc/inittab




将3的那行注释




uncomment这行 x:5:respawn:/usr/sbin/gdm -nodaemon




=========================================================================================================




安装ntfs支持//为了可爱的移动硬盘




pacman -S ntfs-3g







pacman -S hal  //为了自动挂载移动硬等等




=========================================================================================================




安装字体




sudo pacman -S wqy-zenhei  ttf-dejavu [wqy-microhei](https://aur.archlinux.org/packages.php?K=wqy-microhei&SeB=x)




=========================================================================================================







安装yaourt




sudo pacman -S yaourt




=========================================================================================================




安装flash插件




yaourt flashplugin




选择第一个，64位的flashplugin跑起来还算是很流畅的




=========================================================================================================




安装配置fcitx输入法：




sudo yaourt fcitx




可以在文本编辑器中敲出中文，浏览器等不行。




更新locale.gen




将zh_CN.UTF-8 zh_CN.GBK zh_CN.GB2312注释去掉，运行locale-gen




sudo vim /etc/profile




添加以下几行




export XMODIFIERS=@im=fcitx




export GTK_IM_MODULE=fcitx




export QT_IM_MODULE=fcitx




export XIM_PROGRAM=fcitx




最后在gnome的starup program中添加




fcitx -D &即可




=========================================================================================================




安装gnome-system-tools




sudo pacman -S gnome-system-tools




让gksu使用sudo而不是su




sudo gconftool-2 -s /apps/gksu/sudo-mode -t bool true




将dbus添加到/etc/rc.conf中




=========================================================================================================




配置vim




arch默认的vi不是vim的链接







删除vi




cd /usr/bin




sudo rm vi




sudo ln -s vim vi







然后git clone下github下的配置文件，将vimrc覆盖了原来的vimrc




还有一个现象




vim test时，vim的配置文件可以加载




sudo vim test ，加载的是root的vimrc




解决办法：sudo cp ~/.vimrc /root/.vimrc




=========================================================================================================




配置zsh




sudo pacman -S zsh




chsh -s /bin/zsh lgx




下次启动时生效




然后git clone下github下的配置文件，将zshrc覆盖主目录下的zshrc




=========================================================================================================




移除多余的不用的软件




epiphany




sudo pacman -Rsn epiphany ekiga orca gnome-themes-extras




=========================================================================================================




配置网络管理器




sudo pacman -S network-manager




vi /etc/rc.conf




在INTERFACES的eth0前加！




修改最后一行，在network前加！，成为






    
    DAEMONS=( ... !network <strong>dhcdbd networkmanager</strong> ... )







gpasswd -a lgx network //将自己添加到网络用户组




=========================================================================================================




美化




sudo pacman -S compiz-fushion compiz-manager  compiz-core emerald




在compiz设置管理器中设定窗口装饰命令emerald --replace，这样才有标题栏




然后还要设置移动窗口，这样窗口才能移动




在system->preference->startup application中，添加fusion-icon




配置gdm theme




yaourt gdm找一个安装




配置gtk主题引擎




yaourt gtktheme




==========================================================================================================




安装gdm




sudo pacman -S gdm




vi /etc/rc.conf




最后一行的最后添加gdm




vi ~/.xinitrc




uncomment exec gnome-session




==========================================================================================================




安装浏览器firefox




sudo pacman -S firefox //最新的4




yaourt chrome //把chrome和chromium装上




==========================================================================================================




安装办公软件




sudo pacman -S libreoffice




==========================================================================================================




安装pidgin




sudo pacman -S pidgin




==========================================================================================================




安装影音工具




sudo pacman -S mplayer mplayer-plugin codecs  gstreamer0.10-ugly gstreamer0.10-ffmpeg smplayer audacious vlc




==========================================================================================================\




安装下载工具




sudo pacman -S  aria2  deluge




==========================================================================================================




安装文本编辑器




sudo pacman -S gedit




==========================================================================================================




安装pdf阅读器




sudo pacman -S evince




==========================================================================================================




安装svn，git




sudo pacman -S subversion git-core




=========================================================================================================




 
