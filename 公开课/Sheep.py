#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/13 20:58
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import requests, re, os

def get_urls():
    # 1. 获取页面
    response = requests.get("http://qq.yh31.com/zjbq/2920180.html")
    # 2. 正则表达式匹配图片地址
    # .* 匹配除了换行符的任意字符 ? 满足匹配时 匹配尽可能短的字符串
    url_add = r'img border="0".*? src="(.*?)"'

    # 3. 找到需要的数据 response.text 转成字符串   response.content 转成二进制
    url_list = re.findall(url_add, response.text)
    return url_list

def get_gif(url, name):
    # 获取图片的url
    response = requests.get(url)

    # 下载图片
    with open(r"F:\PyTest\公开课\images\%s.gif"%name, 'wb') as f:
        f.write(response.content)



# 定义一个主函数入口
if __name__ == '__main__':
    # 判断images 是否存在，如果不存在则新建
    if 'images' not in os.listdir():
        os.makedirs('images')
    url_list = get_urls()
    gif_name = 1
    for url in url_list:
        com_url = "http://qq.yh31.com" + url
        # 调用下载图片的函数 get_gif(url)
        get_gif(com_url, gif_name)
        gif_name += 1