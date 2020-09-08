# -*- coding: utf-8 -*-
#@Time      :2020/8/25    21:22
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :test_login.py
#@Software  :PyCharm

from p_2020_08_25.PageObject.login_page import Login
from p_2020_08_25.PageObject.home_page import Home
import pytest
from p_2020_08_25.TestDatas import login_datas as td
import pytest

# @pytest.mark.usefixtures('login_init')
class TestLogin:

    @pytest.mark.parametrize('case',td.invalid_data)
    def test_login_failed_user_or_passwd_empty(self,case,login_init):
        login_ob = Login(login_init)
        login_ob.login(case['user'], case['passwd'])
        login_ob.get_error_msg_visible_from_login_area()
        assert login_ob.get_error_msg_text_from_login_area() == case['check']

    @pytest.mark.parametrize('case',td.fomat_right_but_failed_data)
    def test_format_right_but_failed(self, case,login_init):
        login_ob = Login(login_init)
        login_ob.login(case['user'],case['passwd'])
        login_ob.get_error_msg_visible_from_fc_area()
        assert login_ob.get_error_msg_text_from_fc_area() == case['check']

    def test_login_success(self,login_init):
        login_ob = Login(login_init)
        login_ob.login(*td.valid_user)
        home_ob = Home(login_init)
        assert home_ob.quit_is_visible() is None
        home_ob.quit()
