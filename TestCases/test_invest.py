#-*- coding:utf-8 -*-
# @Time : 2020/9/1 11:41 
# @Author : wangj38
# @File : test_invest.py 
# @Software: PyCharm
from p_2020_08_25.PageObject.home_page import Home
from p_2020_08_25.PageObject.bid_page import BidPage
from p_2020_08_25.PageObject.user_page import UserPage
import pytest

@pytest.mark.invest
class TestInvest:
	def test_invest_success(self,back_home):
		# 前置 - 步骤  - 断言
		# 1、首页 - 选择第1个标，点击抢投标按钮
		Home(back_home).qiang_tou_biao_is_to_be_click()
		# 2、标页面 - 获取用户的  投资前的余额
		OBID =BidPage(back_home)
		invest_before_bid_left_money = OBID.get_bid_left_money()
		# 2、标页面 - 获取标的 投资前的标余额
		invest_before_user_left_money = OBID.get_user_left_money()
		# 2、标页面 - 输入投资金额2000，点击投资按钮。
		OBID.invest(100)
		# 3、标页面 - 点击查看并激活
		OBID.click_activation_button_on_success_popup()
		OUSER = UserPage(back_home)
		invest_after_user_left_money = OUSER.get_user_left_money()
		assert invest_after_user_left_money * 100 + 100 *100 == invest_before_user_left_money * 100
		back_home.back()
		import time
		time.sleep(2)
		back_home.refresh()
		invest_after_bid_left_money = OBID.get_bid_left_money()
		assert round(invest_after_bid_left_money,2)*100 + 100*100 == round(invest_before_bid_left_money,2)*100
		# 1、用户的钱少了没有
		# 投资之前 - 投资之后 = 2000
		# 用户页面 - 得到用户当前余额
		# 2、标的可投余额少了没有
		# 标前 - 标后 = 2000
		# 用户页面 - 回退一次
		# 刷新页面，
		# 标页面 - 获取投资后的标余额
