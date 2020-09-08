# -*- coding: utf-8 -*-
#@Time      :2020/8/25    21:23
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :conftest.py
#@Software  :PyCharm
import time
import pytest
from selenium import webdriver
from p_2020_08_25.PageObject.login_page import Login
from p_2020_08_25.TestDatas import global_datas as gd


@pytest.fixture(scope='class')
def init():
    driver =webdriver.Chrome()
    driver.get(gd.login_url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def login_init(init):
    init.get(gd.login_url)
    yield init

@pytest.fixture(scope='class')
def class_login_init():
    '统一初始化登录入口'
    driver =webdriver.Chrome()
    driver.get(gd.login_url)
    driver.maximize_window()
    print(*gd.user_info)
    Login(driver).login(*gd.user_info)
    yield driver
    # driver.quit()

@pytest.fixture
def back_home(class_login_init):

    class_login_init.get(gd.index_url)
    yield class_login_init
    time.sleep(4)

