# -*- coding:utf-8 -*-
# Create By: My.Thunder
# Power By: Abnegate and Elly
'''
学习ZipFile库
'''

import zipfile
import os
from zipfile import BadZipFile, ZipInfo, is_zipfile

class Zip_Learn():
    def Input_zippath(self):
        self.path = input('请输入压缩包路径:')
        self.file_name = os.path.splitext(self.path)
        self.Check_zipFile()

    #检测ZIP文件是否有效
    def Check_zipFile(self):
        if not zipfile.is_zipfile(self.path):
            print(f'该压缩包不是有效的ZIP文件')
            self.Input_zippath()
        elif not self.path.endswith('.zip'):
            print(f'该文件后缀名:{self.file_name}')
            self.Input_zippath()
        else:
            self.zip = zipfile.ZipFile(self.path, 'r')
            self.User_choice()

    #判断用户选择
    def User_choice(self):
        choice = input('1、解压\n2、查看压缩包内容\n3、添加一个文件到压缩包\n4、退出\n请选择:')
        if choice == '1':
            self.unzip_file()
        elif choice == '2':
            self.list_file()
        elif choice == '3':
            self.add_file()
        elif choice == '4':
            exit()
        else:
            print('请输入正确的数字!')

    #解压压缩包
    def unzip_file(self):
        unzip_path = input('请输入要解压到的路径:')
        try:
            self.zip.extractall(path=unzip_path) #解压ZIP
            print('解压完毕!')
            self.User_choice()
        except RuntimeError as e:
            print('该ZIP文件有密码')

    #查看ZIP包内容
    def list_file(self):
        zip_list = self.zip.namelist() #获取ZIP包内的文件名
        '''
        这里防止解压出来的中文文件名为乱码
        '''
        for name in zip_list:
            try:
                name = name.encode('cp437').decode('gbk')
            except:
                name = name.encode('utf-8').decode('utf-8')
            print(name)
        print('\n')
        self.User_choice()

    #添加一个文件到ZIP压缩包
    def add_file(self):
        self.zip = zipfile.ZipFile(self.path, 'w')
        add_file_path = input('请输入需要添加的文件路径:')
        self.zip.write(add_file_path) #写入文件到ZIP
        self.User_choice()

if __name__ == '__main__':
    zip_learn = Zip_Learn()
    zip_learn.Input_zippath()

    zip_learn.zip.close()
