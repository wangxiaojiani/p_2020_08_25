# -*- coding: utf-8 -*-
#@Time      :2020/8/25    22:06
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :main.py
#@Software  :PyCharm
import pytest


if __name__ == '__main__':
    pytest.main(['-s','-v','-m','invest','--html=Outputs/reports/report.html'])


