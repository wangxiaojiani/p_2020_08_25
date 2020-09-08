#-*- coding:utf-8 -*-
# @Time : 2020/9/1 14:37 
# @Author : wangj38
# @File : bid_page_loc.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
class BidPageLocs:
	#标余额
	load_amount =(By.XPATH,"//div[contains(@class,'left')]//span[text()='剩余：']/following-sibling::span[@class='mo_span4']")
	# 用户余额
	user_left_amount= (By.XPATH,"//input[@class='set-all']/parent::label/preceding::input")
	# 投标按钮
	tou_bid_btn =(By.XPATH,"//button[contains(@class,'btn btn-special')]")
	# 投标成功后查看并激活按钮
	select_and_active_btn =(By.XPATH,"//div[text()='投标成功！']/following-sibling::div/button")
