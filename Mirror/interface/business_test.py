#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/4/4 11:11
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from Mirror.data.basecase import BasecaseClass


class Business(BasecaseClass):
    def setUp(self):
        BasecaseClass.smtUP(self)
        sleep(3)

    def tearDown(self):
        BasecaseClass.tmarDown(self)

    # 引导页
    def test_boot_page(self):
        ''' 跳过引导页 '''
        sleep(1)
        # 划过哈罗同行引导页
        TouchAction(self.driver).press(x=569, y=857).move_to(x=157, y=863).release().perform()
        sleep(1)
        # 划过快捷巴士引导页
        TouchAction(self.driver).press(x=569, y=857).move_to(x=157, y=863).release().perform()
        sleep(1)
        # 划过快捷购票引导页
        TouchAction(self.driver).press(x=569, y=857).move_to(x=157, y=863).release().perform()
        sleep(1)
        # 划过专座引导进入首页
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/entry_btn').click()
        sleep(5)
        self.assertIsNotNone(self.driver.find_element(By.ID,'cn.com.haoluo.www:id/tip_view'),msg="不存在")

    def test_guide_purchase(self):
        self.test_boot_page()
        ''' 跳过购票指示 '''
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/tip_view').click()
        sleep(2)
        # try:
        #     self.driver.find_element(By.ID,'cn.com.haoluo.www:id/tip_view')
        #     print("pass")
        # except:
        #     pass_1 = True
        # if pass_1 == True:
        #     self.assertIsNone(None,'存在')
        # else:
        #     self.assertIsNone(not None,"不存在")

    @unittest.skip
    def test_registered_account(self):
        ''' 注册用户 '''
        self.test_guide_purchase()
        # 跳转注册界面
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/tv_register').click()
        # 输入要注册的手机号
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/et_phone').send_keys('13511001101')
        # 输入密码
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/et_password').send_keys('111111')
        # 点击获取验证码
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/tv_get_verify').click()
        # 输入验证码
        vcode = input()
        sleep(5)
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/et_verify_code').send_keys(vcode)
        # 收起键盘
        TouchAction(self.driver).tap(x=661, y=768).perform()
        # 提交注册
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/tv_confirm').click()

    def test_sign(self):
        ''' 登录操作 '''
        self.test_guide_purchase()
        # 点击票夹跳转登录
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/bottom_bar_action_button').click()
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/et_phone').send_keys('13521895260')
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/et_password').send_keys('111111')
        TouchAction(self.driver).tap(x=661, y=768).perform() # 收起键盘
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/bt_confirm').click()
        sleep(3)
    @unittest.skip
    def test_ticket_purchase(self):
        self.test_sign()
        # 进入购票列表
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/check_lines_button').click()
        # 切换到上班列表
        self.driver.find_element(By.NAME,'上班').click()
        # 购买Z110车票
        self.driver.find_element(By.NAME,'Z110').click()
        # 进入车票界面，上车站点为首站
        self.driver.find_element(By.NAME,'上车站点').click()
        self.driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[2]').click()
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/dialog_confirm_btn').click()
        # 选择下车站点为最后一站
        self.driver.find_element(By.NAME,'下车站点').click()
        TouchAction(self.driver).press(x=191, y=1233).move_to(x=0, y=-250).release().perform()
        self.driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[2]').click()
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/dialog_confirm_btn').click()
        # 点击购买，使用哈罗币
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/reserve_ticket_buy_button').click()
        # 确认支付
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/pay_confirm_button').click()
        # 购买成功，确认
        self.driver.find_element(By.ID,'cn.com.haoluo.www:id/button_one').click()

if __name__ == '__main__':
    unittest.main()