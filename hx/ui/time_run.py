#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 11:44

__author__ = 'Soenr'

from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from datetime import datetime
from hx.ui.urls import urls
from hx.ui.urlname import urlname
import time,random


driver = webdriver.Chrome()
# 设定页面加载限制时间
driver.set_page_load_timeout(10)
# 如果10秒内没有加载完成就会报错
#selenium.common.exceptions.TimeoutException: Message: timeout: Timed out receiving message from renderer: 1.684
driver.implicitly_wait(10)

url = input("输入需要测试的网站：http://")
driver.get("http://" + url)

# 获取账号密码
fp = open("user.txt","r").readline()
name = fp.split(",")[0]
pwd = fp.split(",")[1]

# 登录相应权限账号
driver.find_element_by_id("LAY-user-login-username").send_keys(name)
driver.find_element_by_name("password").send_keys(pwd)
driver.find_element_by_id("js_login_submit_btn").click()

time.sleep(3)

number = int(input("输入随机次数："))
log = open("%s随机%d次log.txt"%(url,number),"w",encoding="utf-8")
total_time = datetime.now()
total_time = total_time - total_time

key,value = [],[]
for k,v in urls.items():
    key.append(k)
    value.append(v)


# 主体执行循环
for i in range(1,number+1):
    # 获取随机URL地址
    num = random.randint(0,len(urlname))
    name = key[num]
    url_address = value[num]
    print("=======================%d======================="%i,file=log)
    print("功能名称：%s    URL:%s"%(name,url+url_address),file=log)

    # 获取当前时间
    star_time = datetime.now()
    print("开始时间：%s"%(star_time),file=log)

    # 打开获取的URL地址，缺少判断条件
    try:
        driver.get("http://%s%s"%(url,url_address))
    except TimeoutException:
        # 报错后就强制停止加载
        # 这里是js控制
        driver.execute_script('window.stop()')
        print(driver.page_source)

    # 获取加载完时间
    end_time = datetime.now()
    print("结束时间：%s"%(end_time),file=log)

    # 计算加载时间
    delay_time = (end_time - star_time)
    print("消耗时间：%s秒%s毫秒"%(delay_time.seconds,delay_time.microseconds/1000),file=log)

    # 累计总时间
    total_time += delay_time
    time.sleep(3)


print("==============================================",file=log)
print("平均时间：%d 毫秒"%((total_time.seconds*1000+total_time.microseconds/1000)/number),file=log)
log.close()
driver.quit()