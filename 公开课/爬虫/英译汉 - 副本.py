# _*_ coding:utf-8 _*_

import urllib
import json


content = raw_input('请输入需要翻译的内容：')
url = 'http://fanyi.baidu.com/v2transapi'
data = {}
data['from'] = 'en'
data['to'] = 'zh'
data['query'] = content
data['transtype'] = 'translang'
data['simple_means_flag'] = '3'

data = urllib.urlencode(data).encode('utf-8')

response = urllib.urlopen(url,data)
html = response.read().decode('utf-8')

target = json.loads(html)
print ('翻译结果：%s' % (target['trans_result']['data'][0]['dst']))
