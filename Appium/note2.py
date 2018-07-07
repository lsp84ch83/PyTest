#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/4/1 15:36
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from appium import webdriver
from selenium.webdriver.common.by import By
import xlwt,xlrd,xlutils
from time import sleep

# 获取手机信息 -- 并存到字典中
desired_caps = {
    'platformName' : 'Android',     # 平台
    'platformVersion' : '4.4',    # 版本号
    'deviceName' : '192.168.103.101:5555',  # 设备名称
    'appPackage' : 'com.youdao.note',   # 应用包名
    'appActivity' : '.activity2.SplashActivity',   # Activity名
    'unicodeKeyboard' : 'True',     # 防止键盘中文不能输入
    'resetKeyboard' : 'True'   # 重置设置生效
}
# 启动 appium
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(3)
# 读取Excel
wb = xlrd.open_workbook('F:\PyTest\Appium\data.xls')
sh = wb.sheet_by_name('note')
r_num = sh.nrows
#  循环读取excel
for i in range(1, r_num):
    title = sh.cell_value(i, 1)
    content = sh.cell_value(i, 2)
    expect = sh.cell_value(i, 3)

    # 新建笔记
    driver.find_element(By.ID, 'com.youdao.note:id/add_note_floater_open').click()
    # 选择新建笔记
    driver.find_element(By.NAME, '新建笔记').click()

    # 输入笔记名称
    driver.find_element(By.ID, 'com.youdao.note:id/note_title').send_keys(title)
    # 输入笔记内容
    driver.find_element(By.XPATH, '//android.widget.LinearLayout[@resource-id=\"com.youdao.note:id/note_content\"]/android.widget.EditText[1]').send_keys(content)

    # 保存笔记
    driver.find_element(By.NAME, '完成').click()

    # 验证
    if expect == 'ok':
        if driver.find_element(By.NAME, title) and driver.find_element(By.NAME, content):
            print("success")
        else:
            print("fail")
    elif title == '':
        res1 = driver.find_element(By.ID, 'com.youdao.note:id/title').text
        res2 = driver.find_element(By.ID, 'com.youdao.note:id/summary').text
        if res1 == res2:
            print('success')
        else:
            print('fail')

driver.quit()