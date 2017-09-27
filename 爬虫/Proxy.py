import urllib.request

# 测试IP地址网站
url = 'http://www.whatismyip.com.tw'
# 设置代理服务器IP
proxy_support = urllib.request.ProxyHandler({'http':'111.13.7.42:81'})
# 使用设置的代理IP
opener = urllib.request.build_opener(proxy_support)
# 修改返回服务器headers的值
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
