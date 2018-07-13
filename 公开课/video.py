#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/10 20:41
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company


import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
	list_url = []
	for nums in range(1,3):
		if nums == 1:
			url = "http://www.shuia.net/fzl"
		else:
			url = "http://www.shuia.net/fzl/index_%s.html"%nums
			# 设置网络请求头
			header = {
				"User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
			}
			req = requests.get(url=url, headers=header)
			# 编码格式
			req.encoding = 'utf-8'
			# 解析成文档
			html = req.text
			# 遍历文档树
			bf = BeautifulSoup(html, 'lxml')
			# 搜索文档树
			targers_url = bf.find_all(class_='item-img')
			for each in targers_url:
				# 将所有爬去的数据信息保存进列表里面 名字和地址用 = 分割
				list_url.append(each.img.get('alt') + "=" + each.get('href'))
	print("图片链接的数据采集完成")