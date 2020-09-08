#-*- coding:utf-8 -*-
# @Time : 2020/8/31 15:57 
# @Author : wangj38
# @File : home_page_loc.py 
# @Software: PyCharm
from selenium.webdriver.common.by import By

class HomePageLocs:
	quit_loc = (By.XPATH, "//a[text()='退出']")

	# 抢投标按钮
	qiang_tou_biao_btn =(By.XPATH,"//span[text()=' 吃糖葫芦']/ancestor::a/following-sibling::div//a")