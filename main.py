# -*- coding: utf-8 -*-
#@Time      :2020/8/25    22:06
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :main.py
#@Software  :PyCharm
import pytest
import sys


if __name__ == '__main__':
    sys.path.insert(0,'.')
    pytest.main(['-s','-v','-m','invest','--html=Outputs/reports/report.html'])



