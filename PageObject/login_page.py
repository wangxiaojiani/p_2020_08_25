# -*- coding: utf-8 -*-
#@Time      :2020/8/25    21:02
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :login_page.py
#@Software  :PyCharm

from p_2020_08_25.Common.basepage import BasePage
from p_2020_08_25.PageLocator.login_page_loc import LoginPageLocs as locs

class Login(BasePage):

    def login(self,user,passwd):
        self.wait_ele_visible(locs.login_btn,'登陆页面_判断登陆页面登陆按钮可见')
        self.input_text(locs.user_loc,'登陆页面_在登陆页面输入用户名',user)
        self.input_text(locs.passwd_loc,'登陆页面_在登陆页面输入密码',passwd)
        self.click_element(locs.login_btn,'登陆页面_点击登陆按钮')

    def get_error_msg_visible_from_login_area(self):
        return self.wait_ele_visible(locs.ts_info,'登陆页面_登陆区域登陆失败提示')

    def get_error_msg_text_from_login_area(self):
        return self.get_text(locs.ts_info,'登陆页面_获取浮窗提示信息文本')

    def get_error_msg_visible_from_fc_area(self):
        return self.wait_ele_visible(locs.fc_info,'登陆页面_登陆页面登陆失败浮窗信息')

    def get_error_msg_text_from_fc_area(self):
        return self.get_text(locs.fc_info,'登陆页面浮窗信息文本')



