import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    # 查找current-comment-page
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)   # 从a开始，找到第一个]，返回索引

    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')
    
    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1: # 找到一个jpg
            img_addrs.append(html[a+9:b+4])
        else:   # 找不到，移动b的位置
            b = a + 9
        a = html.find('img src=', b)    # 在b之后开始，再找img src
    return img_addrs

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open('http:' + each)
            f.write(img)

def download_me(folder='Image', pages = 10):
    os.mkdir(folder)    # 创建一个目录
    os.chdir(folder)    # 切换到一个目录

    url = 'http://jandan.net/ooxx/'
    # 获得页面的地址
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        # 打开地址
        page_url = url + 'page-' + str(page_num) + '#comments'
        # 获取图片地址保存为一个列表
        img_addrs = find_imgs(page_url)
        # 保存图标到指定文件夹
        save_imgs(folder, img_addrs)

if __name__ =='__main__':
    download_me()
