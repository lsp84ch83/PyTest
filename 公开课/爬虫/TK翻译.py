import urllib.request
import urllib.parse
import json
import random
import tkinter as tk
import re
import tkinter.messagebox as tm
Error = False
dl = False
root = tk.Tk()
root.title('有道翻译器')
root.iconbitmap('favicon.ico')
v = tk.IntVar()
v2 = tk.IntVar()
i = 0
e1 = None
e2 = None
ip_list = []

class Ip:
    ip = ''
    dk = 80  #默认80
    lx = 'HTTP'
    
class Getip():
    def open_url(url):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586')
            page = urllib.request.urlopen(req)
            html = page.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            html = ''
            Errror = True
            return html
        except urllib.error.URLError as e:
            html = ''
            Error = True
            return html
        else:
            return html

    def get_ip(html):
        if Error == False:
            dk = []
            lx = []
            p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
            a = html.find('<td data-title="PORT">')
            b = html.find('</td>',a)
            dk.append(html[a+22:b])
            a = html.find('<td data-title="类型">')
            b = html.find('</td>',a)
            lx.append(html[a+20:b])
            iplist = re.findall(p, html)
            for each in iplist:
                for each_dk in dk:
                    for each_lx in lx:
                        ip = Ip()
                        ip.ip = each
                        ip.dk = each_dk
                        ip.lx = each_lx
                        return ip
        else:
            return None

def getipaddrs(i):
    url = "http://www.kuaidaili.com/free/inha/"+str(i)
    ipaddrs = Ip()
    ipaddrs = Getip.get_ip(Getip.open_url(url))
    i+=1
    if ipaddrs != None:
        return ipaddrs
    else:
        Error = False  #发生错误后自恢复
class Translation:
    def translation_youdao(context):
        try:
            url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
            data = {}
            data['type'] = 'AUTO'
            data['i'] = context
            data['doctype'] = 'json'
            data['xmlVersion'] = '1.6'
            data['keyfrom'] = 'fanyi.web'
            data['ue'] = 'UTF-8'
            data['typoResult'] = 'true'
            data = urllib.parse.urlencode(data).encode('utf-8')
            if dl == True:
                proxy_support = urllib.request.ProxyHandler({'http':random.choice(ip_list)})
                opener = urllib.request.build_opener(proxy_support)
                opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')]
                urllib.request.install_opener(opener)
            
            response = urllib.request.urlopen(url, data)
            html = response.read().decode('utf-8')
            target = json.loads(html)

        
        except urllib.error.HTTPError as e:
            i+=1
            html = ''
            Errror = True
            return html
        except urllib.error.URLError as e:
            html = ''
            i+=1
            Error = True
        else:
            try:
                tgt = target['translateResult'][0][0]['tgt']
            except KeyError:
                root.destroy()
            else:
                return (tgt)
    def translation_baidu_en_to_zh(context):
        try:
            url = 'http://fanyi.baidu.com/v2transapi'
            data = {'from':'en',
            'to':'zh',
            'query':context,
            'transtype':'trans',
            'simple_means_flag':'3'}
            data = urllib.parse.urlencode(data).encode('utf-8')
            if dl == True:
                proxy_support = urllib.request.ProxyHandler({'http':random.choice(ip_list)})
                opener = urllib.request.build_opener(proxy_support)
                opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')]
                urllib.request.install_opener(opener)

            response = urllib.request.urlopen(url, data)
            html = response.read().decode('utf-8')
            target = json.loads(html)
        except urllib.error.HTTPError as e:
            i+=1
            html = ''
            Errror = True
            return html
        except urllib.error.URLError as e:
            html = ''
            i+=1
            Error = True
        else:
            try:
                dst = target['trans_result']['data'][0]['dst']
            except KeyError:
                root.destroy()
            else:
                return (dst)
    def translation_baidu_zh_to_en(context):
        try:
            url = 'http://fanyi.baidu.com/v2transapi'
            data = {'from':'zh'}
            data = urllib.parse.urlencode(data).encode('utf-8')
            if dl == True:
                proxy_support = urllib.request.ProxyHandler({'http':random.choice(ip_list)})
                opener = urllib.request.build_opener(proxy_support)
                opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')]
                urllib.request.install_opener(opener)

            response = urllib.request.urlopen(url, data)
            html = response.read().decode('utf-8')
            target = json.loads(html)
        except urllib.error.HTTPError as e:
            i+=1
            html = ''
            Errror = True
            return html
        except urllib.error.URLError as e:
            html = ''
            i+=1
            Error = True
        else:
            try:
                dst = target['trans_result']['data'][0]['dst']
            except KeyError:
                root.destroy()
            else:
                return (dst)

def show():
    if v.get() == 1 and v2.get() > 1:
        getip = Getip()
        ip = Ip()
        ip = getipaddrs(i+1)
        if ip != None:
            ip_list.append((ip.ip+':'+ip.dk))
        text = e1.get(1.0,tk.END)
        if text != None:
            if v2.get() == 1:
                Text = Translation.translation_youdao(text)
            elif v2.get() == 2:
                Text = Translation.translation_baidu_zh_to_en(text)
            elif v2.get() == 3:
                Text = Translation.translation_baidu_en_to_zh(text)
            else:
                tm.showerror('错误','没有选择翻译方式')
                return
            try:
                e2['state']= 'normal'
                e2.delete(1.0,tk.END)
                e2.insert(tk.END,Text)
                e2['state']= 'disabled'
            except UnboundLocalError:
                tm.showerror('错误','无法翻译')
            except tk.TclError:
                tm.showerror('错误','无法翻译')
    else:
        text = e1.get(1.0,tk.END)
        if text != None:
            if v2.get() == 1:
                Text = Translation.translation_youdao(text)
            elif v2.get() == 2:
                Text = Translation.translation_baidu_en_to_zh(text)
            elif v2.get() == 3:
                Text = Translation.translation_baidu_zh_to_en(text)
            else:
                tm.showerror('错误','没有选择翻译方式')
                return
        try:
            e2['state']= 'normal'
            e2.delete(1.0,tk.END)
            e2.insert(tk.END,Text)
            e2['state']= 'disabled'
        except UnboundLocalError:
            tm.showerror('错误','无法翻译')
        except tk.TclError:
            tm.showerror('错误','无法翻译')
    

if __name__ == '__main__':
    tk.Label(root, text="需要翻译的内容：").grid(row=0, column=0)
    tk.Label(root, text="翻译结果：").grid(row=2, column=0)
    e1 = tk.Text(root,width=50,height=10)
    e2 = tk.Text(root,width=50,height=10, state="disabled")
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=2, column=1, padx=10, pady=5)
    c = tk.Checkbutton(root, text="翻译时使用代理",variable = v).grid(column=1, padx=0, pady=10)
    tk.Button(root, text="翻译", width=10,command=show).grid(row=1, column=1, padx=70, pady=10)
    tk.Radiobutton(root, text="有道(支持自动检测语种)", variable=v2, value=1).grid(row=4, column=0, padx=0, pady=0)
    tk.Radiobutton(root, text="百度(英文->中文)", variable=v2, value=2).grid(row=4, column=1, padx=0, pady=0)
    tk.Radiobutton(root, text="百度(中文->英文)", variable=v2, value=3).grid(row=4, column=2, padx=0, pady=0)
    tk.mainloop()
    
