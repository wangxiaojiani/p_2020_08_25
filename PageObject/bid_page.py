#-*- coding:utf-8 -*-
# @Time : 2020/9/1 11:37 
# @Author : wangj38
# @File : bid_page_loc.py
# @Software: PyCharm
"""
原则：没有业务上必然的前后操作顺序关系，都分开来写。

# 2、标页面 - 获取用户的  投资前的余额
# 2、标页面 - 获取标的 投资前的标余额
# 2、标页面 - 输入投资金额2000，点击投资按钮。
# 3、标页面 - 点击查看并激活
# 4、标页面 - 获取文本内容
"""

from p_2020_08_25.Common.basepage import BasePage
from p_2020_08_25.PageLocator.bid_page_loc import BidPageLocs as locs
from p_2020_08_25.Common.mylog import logger
class BidPage(BasePage):

	def get_user_left_money(self):
		money = self.get_attribute(locs.user_left_amount,"标页面-获取用户余额","data-amount")
		return float(money)
	def get_bid_left_money(self):
		bid_left_money = float(self.get_text(locs.load_amount,"标页面-获取标余额"))*10000
		logger.info(bid_left_money)
		return bid_left_money

	def invest(self, money):
		self.input_text(locs.user_left_amount,"标页面-输入投资金额",money)
		self.click_element(locs.tou_bid_btn,"标页面-点击投标按钮")

	# 点击成功的弹框里，激活并点击按钮
	def click_activation_button_on_success_popup(self):
		self.click_element(locs.select_and_active_btn,'投标成功页面-点击查看并激活按钮')
