# -*- coding:utf-8 -*-
# Create By: My.Thunder
# Power By: Abnegate and Elly

from PIL import Image
import os

img_path = input('请输入图片路径：')
image = Image.open(img_path)
weight, height = image.size

num = 0
#获取切割次数
rowheight = height // 100
for row in range(rowheight):
    box = (0, row * 100, weight, (row + 1) * 100)
    img_click = image.crop(box) #切割
    img_click.save('C:\\Users\\Redhat\\Desktop\\待替换图片\\' + str(row) + '.jpg') #图片保存

box = (0, rowheight * 100, weight, height)
img_click = image.crop(box)
img_click.save('C:\\Users\\Redhat\\Desktop\\待替换图片\\' + str(rowheight+1) + '.jpg')

print('切割完成!')
print('总共切割图片：{}'.format(rowheight + 1))