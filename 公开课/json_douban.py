#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/14 20:25
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import  requests
import json


# json.loads() 是把json字符串变成python字典
# json.loads() 通常是把网页返回给我们的json数据变成字符串，然后来提取数据
# strDict = '{"city":"长沙","name":"臭豆腐"}'
# a = json.loads(strDict)
# print(a)
# print(type(a))

# json.dumps() 是把python字典变成json对象
# json.dumps() 序列化时默认使用ascii编码
# json.dumps() 通常用来把字典变成字符串保存本地
# strDict = {"city":"长沙","name":"臭豆腐"}
# a = json.dumps(strDict, ensure_ascii=False)
# print(a)
# print(type(a))

# json.dump() 将python字典json字符串化后写入文件，针对的是文件
# dictStr = {"city":"长沙","name":"臭豆腐"}
# with open('dictStr.txt', 'w', encoding="utf-8") as f:
#     json.dump(dictStr, f, ensure_ascii=False)

class Douban(object):
    def __init__(self,name):
        self.start_url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%s&sort=recommend&page_limit=20&page_start={}"%name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        # 实例化对象的时候自动帮我们创建一个文件
        with open('douban.csv', 'a') as f:
            f.write('电影名, 评分, url, 图片地址' + '\n')
        # 所有列表的url
        self.url = []
        for i in range(15):
            url = self.start_url.format(i * 20)
            self.url.append(url)

    def get_json(self,url):
        ret = requests.get(url, headers=self.headers)
        # content_list 即使网页源码，是字典数据类型
        content_list = json.loads(ret.content.decode())
        # content 获取所有电影的信息
        content = content_list['subjects']
        result_list = []
        for i in content:
            result = {}
            result['电影名'] = i['title']
            result['评分'] = i['rate']
            result['url'] = i['url']
            result['图片地址'] = i['cover']
            print(result)
            result_list.append(result)
        return result_list

    def save(self,result_list):
        with open('douban.csv', 'a') as f:
            for result in result_list:
                f.write(result['电影名'] + ',' + result['评分'] + ',' + result['url'] + ',' + result['图片地址'] + '\n')

    def run(self):
        for url in self.url:
            result_list = self.get_json(url)
            self.save(result_list)



if __name__ == '__main__':
    douban = Douban("热门")
    douban.run()