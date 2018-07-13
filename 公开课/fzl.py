#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/11 21:27
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os,time
import requests

if __name__ == '__main__':
    if 'images' not in os.listdir():
        os.makedirs('images')

    list_url = []
    for nums in range(1, 3):
        if nums == 1:
            url = "http://www.shuia.net/fzl"
        else:
            url = "http://www.shuia.net/fzl/index_%d.html"%nums
            # 设置网络请求头
            header = {
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
                }
            req = requests.get(url=url, headers=header)
            # 编码格式
            req.encoding = 'utf-8'
            # 解析成文档
            html = req.text
            # 遍历文档树
            bf = BeautifulSoup(html, 'lxml')
            # 搜索文档树
            targers_url = bf.find_all(class_ = 'item-img')
            for each in targers_url:
                # 将所有爬去的数据信息保存进列表里面 名字和地址用 = 分割
                list_url.append(each.img.get('alt') + "=" + each.get('href'))
            print(list_url)
    print("图片链接的数据采集完成")

    for each_img in list_url:
        img_info = each_img.split("=")
        target_url = img_info[1]
        fileName = img_info[0]+'.jpg'
        print("下载:" + fileName)

        # 设置网络请求头
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        img_req = requests.get(url=target_url, headers=header)
        img_req.encoding = 'utf-8'
        img_html = img_req.text
        img_bf_one = BeautifulSoup(img_html, 'lxml')
        img_url = img_bf_one.find("div",class_="wr-single-content-list")
        img_bf_two = BeautifulSoup(str(img_url), 'lxml')
        try:
            img_url = "http://www.shuaia.net" + img_bf_two.div.img.get('src')
            urlretrieve(url=img_url, filename='images/'+fileName)
            time.sleep(2)
        except:
            print("没有图片")
            break
    print("下载完成")