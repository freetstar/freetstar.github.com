---
author: admin
comments: true
date: 2011-05-11 17:57:12
layout: post
slug: pygtkrandomnum
title: 用PyGTK实现的一个抽奖小程序
wordpress_id: 1705
categories:
- PROGRAM
---

为即将到来的TJLUG的第三次线下活动写的一个抽奖小程序,随机生成1,200之间的号码,点击开始按钮开始滚动数字,停止按钮开始停止数字,并选择当前数字为中将号码
python源代码:
[code language="python"]
#-*- coding: utf-8 -*-
import sys
import os
import random
import time
import threading

try:
    import pygtk
    pygtk.require('2.0')
except:
    pass

try:
    import gtk
except:
    print "GTK Not avaliable!"
    sys.exit(1)

class update(threading.Thread):
    def __init__(self):
        """初始化线程"""
        threading.Thread.__init__(self,name="update")
        self.label=None
        self.num=0
        self.over=False

    def setNum(self,widget,data):
        """设置label的text值"""
        widget.set_text(str(data))
        return True

    def kill(self):
        """设置标志位,来杀死线程"""
        self.over=True

    def run(self):
        while not self.over :
            self.num=random.randint(1,200)
            self.setNum(self.label,self.num)
            time.sleep(0.1000)


class lucky():
    """抽奖的一个小程序"""
    def on_window_destroy(self,widget,data=None):
        gtk.main_quit()

    def __init__(self):
        """读取glade文件,并自动链接信号"""

        #从xml文件中读取数据,并链接必要的信号
        self.builder=gtk.Builder()
        self.file=sys.path[0]+"/lucky.glade"
        self.builder.add_from_file(self.file)
        self.builder.connect_signals(self)
        for widget in  self.builder.get_objects():
            if issubclass(type(widget),gtk.Buildable):
                name=gtk.Buildable.get_name(widget)
                setattr(self,name,widget)
      
        #显示所有窗体
        self.window.set_size_request(800,500)
        self.window.show()

    def on_startbutton_clicked(self,widget,data=None):
        """开始抽奖"""
        self.u=update()
        self.u.label=self.luckylabel
        self.u.setDaemon(True)
        self.u.start()

    def on_stopbutton_clicked(self,widget,data=None):
        """停止,显示当前号码"""
        self.u.kill()

    #主循环
    def main(self):
            gtk.main()

if __name__=="__main__":
    gtk.gdk.threads_init()
    lc=lucky()
    lc.main()
[/code]
<!-- more -->
Glade源文件
[code language="bash"]
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <requires lib="gtk+" version="2.16"/>
  <!-- interface-naming-policy project-wide -->
  <object class="GtkWindow" id="window">
    <child>
      <object class="GtkTable" id="table">
        <property name="visible">True</property>
        <property name="n_rows">3</property>
        <property name="n_columns">3</property>
        <property name="homogeneous">True</property>
        <child>
          <object class="GtkButton" id="startbutton">
            <property name="label" translatable="yes">start</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="receives_default">True</property>
            <signal name="clicked" handler="on_startbutton_clicked"/>
          </object>
          <packing>
            <property name="left_attach">1</property>
            <property name="right_attach">2</property>
            <property name="top_attach">2</property>
            <property name="bottom_attach">3</property>
            <property name="x_options">GTK_EXPAND</property>
            <property name="y_options"></property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="stopbutton">
            <property name="label" translatable="yes">stop</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="receives_default">True</property>
            <signal name="clicked" handler="on_stopbutton_clicked"/>
          </object>
          <packing>
            <property name="left_attach">2</property>
            <property name="right_attach">3</property>
            <property name="top_attach">2</property>
            <property name="bottom_attach">3</property>
            <property name="x_options"></property>
            <property name="y_options"></property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="luckylabel">
            <property name="visible">True</property>
            <property name="label" translatable="yes">100</property>
            <property name="justify">center</property>
            <property name="ellipsize">middle</property>
            <attributes>
              <attribute name="weight" value="medium"/>
              <attribute name="size" value="200000"/>
              <attribute name="foreground" value="#e3970be40be4"/>
            </attributes>
          </object>
          <packing>
            <property name="right_attach">3</property>
            <property name="bottom_attach">2</property>
          </packing>
        </child>
        <child>
          <placeholder/>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkTextBuffer" id="textbuffer1"/>
</interface>
[/code]
