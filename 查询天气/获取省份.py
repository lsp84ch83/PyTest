# _*_ coding:utf-8 _*_

import urllib.request

url = 'http://i.tq121.com.cn/j/wap2016/news/city_search_data.js'
content1 = urllib.request.urlopen(url).read()

print(content1)
