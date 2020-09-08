# -*- coding: utf-8 -*-
#@Time      :2020/8/25    21:02
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :home_page.py
#@Software  :PyCharm

from p_2020_08_25.Common.basepage import BasePage
from p_2020_08_25.PageLocator.home_page_loc import HomePageLocs as locs

class Home(BasePage):

    def quit_is_visible(self):
        self.wait_ele_visible(locs.quit_loc,'首页-退出按钮可见')

    def quit(self):
        self.click_element(locs.quit_loc,'首页-点击退出按钮')

    def qiang_tou_biao_is_to_be_click(self):
        self.click_element(locs.qiang_tou_biao_btn,'首页-点击抢投标按钮')

