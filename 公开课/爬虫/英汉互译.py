# _*_ coding:utf-8 _*_

import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入需要翻译的内容(输入"q!"退出程序)：')
    if content == 'q!':
        break
    url = 'http://fanyi.baidu.com/v2transapi'

    data = {}
    data['from'] = 'auto'
    data['to'] = 'auto'
    data['query'] = content
    data['transtype'] = 'translang'
    data['simple_means_flag'] = '3'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0')

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print('翻译结果：%s' % (target['trans_result']['data'][0]['dst']))
    time.sleep(2)
