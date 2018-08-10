#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/8/9 17:46
# @Author  : Soner
# @version : 1.0.0

#重写元素定位的方法
class Action(object):
    #初始化
    def init(self, se_driver):
        self.driver = se_driver

    #通过id定位
    def findId(self, id):
        try:
            f = self.driver.find_element_by_id(id)
            return f
        except Exception as e:
            #print("未找到%s"%(id))
            return False

    #通过class定位
    def findClassName(self, name):
        try:
            f = self.driver.find_element_by_class_name(name)
            return f
        except Exception as e:
            #print("未找到%s"%(name))
            return False

    #通过text定位
    def findAU(self, name):
        try:
            f = self.driver.find_element_by_android_uiautomator('text(\"' + name +'\")')
            return f
        except Exception as e:
            #print("未找到%s"%(name))
            return False

    #通过xpath定位
    def findXpath(self, xpath):
        try:
            f = self.driver.find_element_by_xpath(xpath)
            return f
        except Exception as e:
            #print("未找到%s"%(xpath))
            return False

    #通过content-desc
    def findAI(self, content_desc):
        try:
            f = self.driver.find_element_by_accessibility_id(content_desc)
            return f
        except Exception as e:
            #print("未找到%s"%(content_desc))
            return False