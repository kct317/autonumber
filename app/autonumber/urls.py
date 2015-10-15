from django.conf.urls import include, url
from django.contrib import admin
from app.autonumber.views import index, login, logout
from app.autonumber.views import register, forgetpwd, resetpwd
from app.autonumber.views import tasklist, createtask
from app.autonumber.views import entry, index_list
from app.autonumber import models

urlpatterns = [
	# login
	url(r'^login/$',          login.login,         name='login'), # 登陆页
	url(r'^accounts/login/$', login.login,         name='accounts_login'), # 登陆页
	url(r'^register/$',       register.register,   name='register'), # 注册页
	url(r'^logout/$',         logout.logout,       name='logout'), # 注销
	url(r'^index/$',          index.index,         name='index'), # 登陆成功页
	url(r'^forgetpwd/$',      forgetpwd.forgetpwd, name='forgetpwd'), # 忘记密码
	url(r'^resetpwd/$',       resetpwd.resetpwd,   name='resetpwd'), # 重设密码

	# Business
	#url(r'^tasklist/', tasklist.tasklist), # 任务列表
	#url(r'^createtask/', createtask.createtask), # 创建任务
	url(r'^index_list/$', entry.entry , {'model': models.Case, 'func':index_list.index_list}, name='index_list'), # 创建任务
	
]
