# -*- coding:utf-8 -*-
#Create By：Mr.Thunder
#Power By: Abnegate and Elly

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
    def choice_flag(self):
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
        self.number = input('请输入订单号(输入2 or Q or q 退出):')
        if self.number == '2' or self.number == 'q' or self.number == 'Q':
            self.judgeUSB(self)
        else:
            self.search(flag)

    #格式化盘符
    def Format_usb(self):
        os.system('format /FS:NTFS /Q {}:'.format(self.choice))

    #搜索精修
    def search(self, flag):
        for jxdir in os.listdir(self.jxpath):  # 递归查询订单号文件夹
            if re.search(self.number, jxdir[0:]):
                print('搜索结果：{}'.format(jxdir))
                self.choice = self.choiceUSB()
                self.Format_usb()

                self.createdir(jxdir)
                os.system(u'xcopy /s \"{}\\{}\" \"{}:\\{}\"'.format(self.jxpath,
                                                                    jxdir,
                                                                    self.choice,
                                                                    jxdir))

                self.get_Time(os.path.join(self.jxpath, jxdir))
                os.rename('{}\\{}'.format(self.jxpath, jxdir), '{}\\{} {} {}'.format(self.jxpath,
                                                                                     jxdir,
                                                                                     flag,
                                                                                     self.now_time))
                break

    #获取精修照片创建时间
    def get_Time(self, *args):
        self.mon = time.localtime(os.path.getctime(args[0])).tm_mon
        self.start = time.clock()
        self.is_zpccp_path()

    '''
    搜索方式：通过获取照片的最后修改月份，每次向前推移一个月搜索，并且循环判断是否属于当前存储盘
    '''

    def is_zpccp_path(self):
        for dir in os.listdir(self.zpccp_path):
            if re.match(str(self.mon), dir):
                if self.searchdp(self.zpccp_path, self.mon) == None:
                    self.is_zpcp_path()
                    self.mon = self.mon - 1 #每次减少一个月
                    self.is_zpccp_path()
        self.is_zpcp_path()

    def is_zpcp_path(self):
        for dir in os.listdir(self.zpcp_path):
            if re.match(str(self.mon), dir):
                self.searchdp(self.zpcp_path, self.mon)

    #搜索底片
    def searchdp(self, dppath, mounth):
        for dir, dir2, file in os.walk('{}\\{}月'.format(dppath, mounth)):
            for name in dir2:
                if re.search('%s' % self.number, name):
                    print('搜索结果：{}\\{}\n'.format(dir, name))

                    self.stop = time.clock()
                    print('搜索耗时：' + str(self.stop - self.start) + '秒')
                    self.createdir(name)
                    os.system(u'xcopy /s \"{0}\\{1}\" \"{2}:\\{3}\"'.format(dir,
                                                                            name,
                                                                            self.choice,
                                                                            name))
                    self.wechart()
                    return 1

    #USB内建立文件夹
    def createdir(self, pathname):
        os.system('mkdir \"{}:\\{}\"'.format(self.choice, pathname))

    #复制微信喜帖
    def wechart(self):
        for dir, dir1, file in os.walk(self.wechatpath):
            for name in file:
                if re.search(self.number, name):
                    print('{}\\{}'.format(dir, name))
                    shutil.copy('{}\\{}'.format(dir, name),'{}:\\'.format(self.choice))

if __name__ == '__main__':
    p = picturecopy()
    p.judgeUSB()
    while True:
        p.choice_flag()
