#-*- coding:utf-8 -*-
# @Time : 2020/9/1 11:39 
# @Author : wangj38
# @File : user_page_loc.py
# @Software: PyCharm
from p_2020_08_25.Common.basepage import BasePage
from p_2020_08_25.PageLocator.user_page_loc import UserPageLocs as locs

class UserPage(BasePage):
	def get_user_left_money(self):
		user_left_money= self.get_text(locs.user_left_amount,'用户页面-查看用户余额')
		return float(user_left_money[:-1])

