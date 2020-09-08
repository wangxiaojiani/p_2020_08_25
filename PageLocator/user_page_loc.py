#-*- coding:utf-8 -*-
# @Time : 2020/9/1 15:06 
# @Author : wangj38
# @File : user_page_loc.py
# @Software: PyCharm

from selenium.webdriver.common.by import By

class UserPageLocs:
	user_left_amount =(By.XPATH,"//ul[@class='per_list_right']/li[@class='color_sub']")