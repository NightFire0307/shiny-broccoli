# -*- coding:utf-8 -*-
#Create By：Mr.Thunder
#Power By:Abnegate
#Version: V2.2 Beta
#1、增加Flag标记区分
#2、增加微信喜帖复制
#3、代码逻辑优化
#4、增加判断底片月份逻辑
#5、移除S店
#6、格式化U盘 NTFS

import os
import re
import shutil
import time
from datetime import datetime

class picturecopy(object):

    def __init__(self):
        self.jxpath = 'S:\\刻盘\\我不是刻盘文件夹'
        self.zpcp_path = 'x:\\2018'
        self.zpccp_path = 'y:\\2018'
        self.wechatpath = 'S:\\微信喜帖\\接收'
        self.now_time = datetime.now().strftime('%m-%d')

    #判断U接入状态
    def judgeUSB(self):
        for i in 69, 72:
            diskname = chr(i) + ':'
            if os.path.isdir(diskname) is True:
                print('U盘 {} 已插入！'.format(diskname))
            else:
                print('U盘 {} 未插入，请检查！'.format(diskname))
        print('\r')

    #选择复制类型
    def choice(self):
        choice = input('请选择类型：\n1、1楼取件（输入1）\n2、送件（输入2）\n输入选择:')
        if choice == '1' :
            print('\n你的选择是：1楼取件')
            flag = 'w'
            self.inputNumber(flag)
        elif choice == '2' :
            print('\n你的选择是：送件')
            flag = 's'
            self.inputNumber(flag)
        else:
            print('\n选择错误！请输入：1 or 2')

    #复制USB盘符选择
    def choiceUSB(self):
        choice = input('输入复制的盘符：E OR H :')
        if str.upper(choice) == 'E' :
            return choice
        elif str.upper(choice) == 'H' :
            return choice
        else:
            print('输入盘符错误')

    #输入订单号
    def inputNumber(self, flag):
        number = input('请输入订单号(输入2 or Q or q 退出):')
        if number == '2' or number == 'q' or number == 'Q':
            self.judgeUSB(self)
        else:
            self.search(number, flag)

    #格式化盘符
    def Format_usb(self, usbchoice):
        os.system('format /FS:NTFS /Q {}:'.format(usbchoice))

    #搜索精修
    def search(self, number, flag):
        for jxdir in os.listdir(self.jxpath):  # 递归查询订单号文件夹
            if re.search(number, jxdir[0:]):
                print('搜索结果：{}'.format(jxdir))
                self.get_Time(os.path.join(self.jxpath, jxdir))
                # usbchoice = self.choiceUSB()
                # self.Format_usb(usbchoice)

                # self.createdir(usbchoice, jxdir)
                # os.system(u'xcopy /s \"{}\\{}\" \"{}:\\{}\"'.format(self.jxpath, jxdir, usbchoice, jxdir))
                #
                # self.searchdp(number, usbchoice)
                # os.rename('{}\\{}'.format(self.jxpath, jxdir), '{}\\{} {} {}'.format(self.jxpath, jxdir, flag, self.now_time))
                break

    #获取精修照片创建时间
    def get_Time(self, *args):
        self.mon, self.day = (time.localtime(os.path.getctime(args[0])).tm_mon,
                    time.localtime(os.path.getctime(args[0])).tm_mday)
        self.get_zpccp_path()

    def get_zpccp_path(self):
        for dir in os.listdir(self.zpccp_path):
            if re.search(str(self.mon), dir):
                self.dppath = os.path.join(self.zpccp_path, os.path.join(dir, str(self.day)))
                print(self.dppath)
            else:
                self.get_zpcp_path()

    def get_zpcp_path(self):
        for dir in os.listdir(self.zpcp_path):
            if re.search(str(self.mon), dir):
                self.dppath = os.path.join(self.zpcp_path, os.path.join(dir, str(self.day)))
                print(self.dppath)

    #搜索底片
    def searchdp(self, number, usbchoice):
        # usbchoice = picturecopy.choiceUSB(picturecopy, '')
        newDate = int(datetime.now().strftime('%m')) #获取当前月份
        oldDate = newDate - 3 #搜索的月份提前三个月
        for mouth in range(oldDate, newDate):  # 递归查询底片编号
            for dir, dir2, file in os.walk('{}\\{}月'.format(self.dppath, mouth)):
                for name in dir2:
                    if re.search('%s' % number, name):
                        print('搜索结果：{}\\{}'.format(dir, name))
                        self.createdir(usbchoice, name)
                        os.system(u'xcopy /s \"{0}\\{1}\" \"{2}:\\{3}\"'.format(dir, name, usbchoice, name))
                        self.wechart(number, usbchoice)

    #USB内建立文件夹
    def createdir(self, usbchoice, pathname):
        os.system('mkdir \"{}:\\{}\"'.format(usbchoice, pathname))

    #复制微信喜帖
    def wechart(self, number, usbchoice):
        for dir, dir1, file in os.walk(self.wechatpath):
            for name in file:
                if re.search(number, name):
                    print('{}\\{}'.format(dir, name))
                    shutil.copy('{}\\{}'.format(dir, name),'{}:\\'.format(usbchoice))

if __name__ == '__main__':
    p = picturecopy()
    p.judgeUSB()
    while True:
        p.choice()
