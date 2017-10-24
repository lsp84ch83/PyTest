# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_class_name('s_ipt').send_keys('Python')
driver.find_element_by_id('su').click()

sleep(2)
driver.quit()
