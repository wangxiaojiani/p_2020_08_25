#-*- coding:utf-8 -*-
# @Time : 2020/8/31 16:07 
# @Author : wangj38
# @File : login_datas.py 
# @Software: PyCharm

#登陆失败的数据 - 用户名为空/密码为空/用户格式不正确
invalid_data = [
	{"user":"","passwd":"python","check":"请输入手机号"},
	{"user":"18684720553","passwd":"","check":"请输入密码"},
	{"user":"fafa","passwd":"","check":"请输入正确的手机号"}

]

# 手机号格式正确 但是登陆失败的数据
fomat_right_but_failed_data =[
	{"user":"18684720553","passwd":"dada","check":"帐号或密码错误!"},
	{"user":"18684720552","passwd":"dada","check":"此账号没有经过授权，请联系管理员!"}
]

# 登陆成功的数据
valid_user = ("18684720553","python")



