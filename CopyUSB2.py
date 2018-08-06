# -*- coding:utf-8 -*-
#Create By：Mr.Thunder
#Power By:Abnegate
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
        self.choice = input('输入复制的盘符：E OR H :')
        if str.upper(choice) == 'E' :
            return choice
        elif str.upper(choice) == 'H' :
            return choice
        else:
            print('输入盘符错误')

    #输入订单号
    def inputNumber(self, flag):
        self.number = input('请输入订单号(输入2 or Q or q 退出):')
        if self.number == '2' or self.number == 'q' or self.number == 'Q':
            self.judgeUSB(self)
        else:
            self.search(flag)

    #格式化盘符
    def Format_usb(self):
        os.system('format /FS:NTFS /Q {}:'.format(self.usbchoice))

    #搜索精修
    def search(self, flag):
        for jxdir in os.listdir(self.jxpath):  # 递归查询订单号文件夹
            if re.search(self.number, jxdir[0:]):
                print('搜索结果：{}'.format(jxdir))
                self.jxdir = jxdir
                self.get_Time(os.path.join(self.jxpath, jxdir))
                # self.Format_usb(usbchoice)

                # self.createdir(usbchoice, jxdir)
                # os.system(u'xcopy /s \"{}\\{}\" \"{}:\\{}\"'.format(self.jxpath, jxdir, usbchoice, jxdir))
                #
                # self.searchdp(self.number, usbchoice)
                # os.rename('{}\\{}'.format(self.jxpath, jxdir), '{}\\{} {} {}'.format(self.jxpath, jxdir, flag, self.now_time))
                break

    #获取精修照片创建时间
    def get_Time(self, *args):
        self.mon = time.localtime(os.path.getctime(args[0])).tm_mon
        self.get_path()

    def get_path(self):
        for dir in os.listdir(self.zpccp_path):
            if re.match(str(self.mon), dir):
                self.is_path(self.zpccp_path)
                return

        for dir in os.listdir(self.zpcp_path):
            if re.match(str(self.mon), dir):
                self.is_path(self.zpcp_path)
                return

    #判断月份是否属于当前共享盘符
    def is_path(self, path):
        if path == self.zpccp_path:
            if self.searchdp(self.zpccp_path) == None: #判断Return结果
                self.mon = self.mon - 1
                self.get_path()
        elif path == self.zpcp_path:
            if self.searchdp(self.zpcp_path) == None:
                self.mon = self.mon - 1
                self.get_path()

    #搜索底片
    def searchdp(self, path):
        for dir, dir2, file in os.walk('{}\\{}月'.format(path, self.mon)):
            for name in dir2:
                if re.search('%s' % self.number, name):
                    print('搜索结果：{}\\{}'.format(dir, name))
                    return 1
                    '''
                    上面是判断None，所以需要一个返回值来跳出函数循环
                    '''
                    # self.createdir(usbchoice, name)
                    # os.system(u'xcopy /s \"{0}\\{1}\" \"{2}:\\{3}\"'.format(dir, name, usbchoice, name))
                    # self.wechart(self.number, usbchoice)

    #USB内建立文件夹
    def createdir(self, pathname):
        os.system('mkdir \"{}:\\{}\"'.format(self.usbchoice, pathname))

    #复制微信喜帖
    def wechart(self):
        for dir, dir1, file in os.walk(self.wechatpath):
            for name in file:
                if re.search(self.number, name):
                    print('{}\\{}'.format(dir, name))
                    shutil.copy('{}\\{}'.format(dir, name),'{}:\\'.format(self.usbchoice))

if __name__ == '__main__':
    p = picturecopy()
    p.judgeUSB()
    while True:
        p.choice()
