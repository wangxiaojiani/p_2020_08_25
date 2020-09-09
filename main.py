# -*- coding: utf-8 -*-
#@Time      :2020/8/25    22:06
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :main.py
#@Software  :PyCharm

import sys
import pytest
sys.path.insert(0, '.')

if __name__ == '__main__':
    print(sys.path)
    pytest.main(['-s','-v','-m','invest','--html=Outputs/reports/report.html','--alluredir=Outputs/reports'])



