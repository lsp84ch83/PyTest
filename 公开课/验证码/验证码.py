#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/15 20:18
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from PIL    import Image
import hashlib
import os
import math

"""
AI与向量空间的图像的识别
向量搜索引擎来做字符的识别
1. 不需要大量的训练迭代
2. 随时加入或者移除错误的数据查看结果
3. 很容易理解和编写代码
拿3篇文章，我们要怎么样计算他们的相似度
2篇文档的所使用相同的单词越多，那么
选择关键字 --- 向量之后 --- 特征
计算矢量的夹角来得到我们文章的相似度
"""
# 用pyton 来实现向量空间
class VectorCompare():
    # 计算矢量大小
    def magnitude(self,concordance):
        total = 0
        for word,count in concordance.items():
            total += count**2
        return math.sqrt(total)

    # 计算矢量之间的值
    def ralation(self,concordance1,concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count*concordance2[word]
        return topvalue/(self.magnitude(concordance1)*self.magnitude(concordance2))

# 将图像转变成矢量
def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1

im = Image.open("兔子.png")
print(im.getdata())
# 返回的是图像内容的像素序列值

V = VectorCompare()

# 添加我们的训练集
iconset = ['0','1', '2','3','4','5','6','7',]
imageset = []
for letter in iconset:
    for img in os.listdir('./iconset/%s/'%(letter)):
        temp = []
        if img != ".DS_Store" and img != "Thumbs.db":
            temp.append(buildvector(Image.open('./iconset/%s/%s'%(letter,img))))
        imageset.append({letter:temp})

# 打开图片 验证码
im = Image.open("验证码.gif")
# 将图片转换成 8位 像素的模式
im.convert("P")
im2 = Image.new("P", im.size, 255)
'''
his = im.histogram()
values = {}
for i in range(256):
    values[i] = his[i]
for j,k in sorted(values.items(), key=lambda x:x[1], reverse=True)[:10]:
    print(j,k)
# 得到图片中最多的10种颜色,220  227 需要的红色和灰色
'''
# 构造黑白的图片
temp = {}
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))    # im.getpixel() value or tuple() 含义：给定位置图像像素，元祖
        temp[pix] = pix
        if pix == 220 or pix ==227:
            im2.putpixel((y,x), 0) # 0代表黑色


# 提取单个字符图片
inletter = False
foundletter = False
start = 0
end = 0

letters = []
for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True

    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter == False
        end = y
        letters.append((start,end))

    inletter = False

# 对验证码图片进行切割
count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop((letters[0],0,letters[1],im2.size[1]))
    guess = []

    # 将切割得到的验证码小片段与每一个训练片段进行比较
    for image in imageset:
        for x,y in image.items():
            if len(y) != 0:
                guess.append((V.relation(y[0], buildvector(im3)),x))

    guess.sort(reverse=True)
    print('', guess[0])
    count +=1