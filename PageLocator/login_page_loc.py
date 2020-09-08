#-*- coding:utf-8 -*-
# @Time : 2020/8/31 15:50 
# @Author : wangj38
# @File : login_page_loc.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


class LoginPageLocs:

	user_loc = (By.XPATH, "//input[@name='phone']")
	passwd_loc = (By.XPATH, "//input[@name='password']")
	login_btn = (By.XPATH, "//button[text()='登录']")
	ts_info = (By.XPATH, "//div[@class='form-error-info']")
	fc_info = (By.XPATH, "//div[@class='layui-layer-content']")
	yzm_loc = (By.XPATH, "//input[@name='vcode']")