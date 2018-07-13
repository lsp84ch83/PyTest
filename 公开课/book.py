#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/8 20:30
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import urllib.request
import re

# 获取主页面源代码
# 获取章节超链接
# 获取章节超链接源代码
# 获取小说内容
# 下载小说

# 获取小说内容
def getNovelContent():
    # 获取主页面源代码
    html = urllib.request.urlopen("http://www.quanshuwang.com/book/9/9055").read()
    # status 状态码 200
    # print(html.status)
    # 解码
    html = html.decode('gbk')

    # 获取章节超链接
    # 正则表达式
    req = '<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    urls = re.findall(req,html)
    # print(urls)
    for i in urls:
        # 获取章节url地址
        novel_url = i[0]
        # 获取章节名字
        novel_name = i[1]
        # 获取章节源代码
        chapt = urllib.request.urlopen(novel_url).read()
        chapt_html = chapt.decode("gbk")
        # 获取小说内容
        reg = '</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<scrpit type="text/javascript">'
        # S 多行匹配
        reg = re.compile(reg, re.S)
        chapt_content = re.findall(reg, chapt_html)
        # 替换内容
        chapt_content = chapt_content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;", "")
        # 再次替换其它内容
        chapt_content = chapt_content.replace("<br />", "")

        # 下载小说
        print("正在下载：%s"%novel_name)
        # f = open("{}.txt".format(novel_name), "w")
        # f.write(chapt_content)
        # f.close()
        with open('{}.txt'.format(novel_name), "w") as f:
            f.write(chapt_content)


getNovelContent()