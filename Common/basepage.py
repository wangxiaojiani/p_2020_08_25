#-*- coding:utf-8 -*-
# @Time : 2020/9/1 9:35 
# @Author : wangj38
# @File : basepage.py 
# @Software: PyCharm

"""
1、等待元素可见
2、查找元素
3、点击操作：等待 - 查找 - 点击
4、输入操作：等待 - 查找 - 输入
5、获取元素文本：等待 - 查找 - 获取文本
6、获取元素属性：等待 - 查找 - 获取属性值
节省代码量、记录日志、失败截图
7、窗口切换 -- 让新窗口出现，获取所有句柄，切换到新窗口。
"""
import time,os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from p_2020_08_25.Common.mylog import logger
from p_2020_08_25.Common import load_path
class BasePage:

	def __init__(self,driver:WebDriver):
		self.driver = driver


	def wait_ele_visible(self,locator,page_action,timeout=20,poll_frequency=0.5):
		"""
		等待页面元素课件
		:param locator:元素定位表达式，以元组形式展现
		:param page_action: 对元素操作的注释
		:param timeout: 显示等待最上的超时时间
		:param poll_frequency: 轮询间隔
		:return: 无
		"""
		logger.info("在 【{}】 行为，等待元素：【{}】 可见".format(page_action, locator))
		try:
			start = time.time()
			WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
		except:
			# 输出到日志
			logger.exception("等待元素可见失败！")
			# 失败截图页面
			self.get_page_img(page_action)
			raise
		else:
			end = time.time()
			logger.info("等待耗时为：【{}】".format(end - start))


	def wait_page_contains_element(self, locator, page_action, timeout=20, poll_frequency=0.5):
		"判断元素存在"
		logger.info("在 【{}】 行为，等待元素：【{}】 存在。".format(page_action, locator))
		try:
			start = time.time()
			WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
		except:
			# 输出到日志
			logger.exception("等待元素存在失败！")
			# 失败截取当前页面
			self.get_page_img(page_action)
			raise
		else:
			end = time.time()
			logger.info("等待耗时为：【{}】 ".format(end - start))


	def get_element(self, locator, page_action,timeout=20, poll_frequency=0.5, wait_exist=None):
		# 先等待元素可见或者存在
		if wait_exist:
			self.wait_page_contains_element(locator, page_action, timeout, poll_frequency)
		else:
			self.wait_ele_visible(locator, page_action, timeout, poll_frequency)

		logger.info("在 【{}】 行为，查找元素：【{}】".format(page_action, locator))
		try:
			ele = self.driver.find_element(*locator)
		except:
			# 输出到日志
			logger.exception("查找元素失败！")
			# 失败截取当前页面
			self.get_page_img(page_action)
			raise
		else:
			return ele


	def click_element(self,locator, page_action,timeout=20, poll_frequency=0.5):
		# 等待 - 查找
		ele = self.get_element(locator, page_action, timeout, poll_frequency)
		# 点击
		logger.info("在 【{}】 行为，点击元素：【{}】".format(page_action, locator))
		try:
			ele.click()
		except:
			logger.exception("点击元素失败！")
			self.get_page_img(page_action)
			raise


	def input_text(self, locator, page_action, value, timeout=20, poll_frequency=0.5):
		# 等待 - 查找
		ele = self.get_element(locator, page_action, timeout, poll_frequency)
		logger.info("在 【{}】 行为，给元素：【{}】 输入文本值：【{}】".format(page_action, locator, value))
		try:
			ele.clear()
			ele.send_keys(value)
		except:
			logger.exception("元素输入文本失败！")
			self.get_page_img(page_action)
			raise


	def get_text(self, locator, page_action, timeout=20, poll_frequency=0.5, wait_exist=False):
		"""
		:param locator:
		:param page_action:
		:param timeout:
		:param poll_frequency:
		:return:
		"""
		# 等待元素存在 - 查找
		ele = self.get_element(locator, page_action, timeout, poll_frequency, wait_exist=wait_exist)
		logger.info("在 【{}】 行为，获取元素 【{}】 的文本值。".format(page_action, locator))
		try:
			txt = ele.text
		except:
			logger.exception("获取元素文本失败！")
			self.get_page_img(page_action)
			raise
		else:
			logger.info("文本值为：【{}】".format(txt))
			return txt


	def get_attribute(self, locator, page_action, attr, timeout=20, poll_frequency=0.5, wait_exist=False):
		# 等待元素存在 - 查找
		ele = self.get_element(locator, page_action, timeout, poll_frequency, wait_exist=wait_exist)
		logger.info("在 【{}】 行为，获取元素 【{}】 的 【{}】 属性值。".format(page_action, locator, attr))
		try:
			value = ele.get_attribute(attr)
		except:
			logger.exception("获取元素属性失败！")
			self.get_page_img(page_action)
			raise
		else:
			logger.info("属性值为：【{}】".format(value))
			return value


	def modify_attribute(self, locator, page_action, attr,value, timeout=20, poll_frequency=0.5, wait_exist=False):
		# 等待元素存在 - 查找
		ele = self.get_element(locator, page_action, timeout, poll_frequency, wait_exist=wait_exist)
		logger.info("在 【{}】 行为，修改元素 【{}】 的 【{}】 属性值为【{}】。".format(page_action, locator, attr,value))
		try:
			self.driver.execute_script("arguments[0].arguments[1]=arguments[2];",ele,attr,value)
		except:
			logger.exception("修改元素属性失败！")
			self.get_page_img(page_action)
			raise
		else:
			logger.info("修改元素属性成功!")



	def switch_window(self, name="new"):
		# 等待一下
		time.sleep(1)
		# 获取所有的句柄
		wins = self.driver.window_handles
		if name == "new":
			self.driver.switch_to.window(wins[-1])


	def alert_handLer(self,page_action, action='accept',timeout=20, poll_frequency=0.5):
		# 等待alert元素出现

		logger.info("在 【{}】 行为，alert弹窗中获取文本信息。".format(page_action))
		try:
			WebDriverWait(self.driver, timeout, poll_frequency).until(EC.alert_is_present())
			alert = self.driver.switch_to.alert
			message = alert.text
		except:
			logger.exception("获取alter弹窗文本信息失败！")
			self.get_page_img(page_action)
			raise
		else:
			if action == 'accept':
				alert.accept()
			else:
				alert.dismiss()
			logger.info('alter弹窗文本信息为【{}】'.format(message))
			return message


	def get_page_img(self,page_action):
		# 命令规范: {XX页面_XX操作}_截图时间.png
		cur_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
		file_path = os.path.join(load_path.screenshot_dir,"{}_{}.png".format(page_action,cur_time))
		self.driver.save_screenshot(file_path)
		logger.info("截图保存在：【{}】".format(file_path))
