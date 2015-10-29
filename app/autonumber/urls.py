from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.autonumber.views',
    url(r'^login/$', 'user.LoginUser', name='loginurl'),
    url(r'^logout/$', 'user.LogoutUser', name='logouturl'),

    url(r'^user/changepwd/$', 'user.ChangePassword', name='changepasswordurl'),
    url(r'^user/resetpwd/(?P<ID>\d+)/$', 'user.ResetPassword', name='resetpasswordurl'),


    url(r'^user/add/$', 'user.AddUser', name='adduserurl'),
    url(r'^user/list/$', 'user.ListUser', name='listuserurl'),
    url(r'^user/edit/(?P<ID>\d+)/$', 'user.EditUser', name='edituserurl'),
    url(r'^user/delete/(?P<ID>\d+)/$', 'user.DeleteUser', name='deleteuserurl'),


    url(r'^role/add/$', 'role.AddRole', name='addroleurl'),
    url(r'^role/list/$', 'role.ListRole', name='listroleurl'),
    url(r'^role/edit/(?P<ID>\d+)/$', 'role.EditRole', name='editroleurl'),
    url(r'^role/delete/(?P<ID>\d+)/$', 'role.DeleteRole', name='deleteroleurl'),


    url(r'^permission/deny/$', 'permission.NoPermission', name='permissiondenyurl'),
    #--------------------------------------------------------------------------------
    url(r'^permission/add/$', 'permission.AddPermission', name='addpermissionurl'),
    url(r'^permission/list/$', 'permission.ListPermission', name='listpermissionurl'),
    url(r'^permission/edit/(?P<ID>\d+)/$', 'permission.EditPermission', name='editpermissionurl'),
    url(r'^permission/delete/(?P<ID>\d+)/$', 'permission.DeletePermission', name='deletepermissionurl'),


    url(r'^(?P<type>\d+)/gaozi/add/$', 'autonumber.AddGaoZi', name='AddGaoZi'),
    url(r'^(?P<type>\d+)/gaozi/list/$', 'autonumber.ListGaoZi', name='ListGaoZi'),
    url(r'^(?P<type>\d+)/gaozi/edit/(?P<ID>\d+)/$', 'autonumber.EditGaoZi', name='EditGaoZi'),
    url(r'^(?P<type>\d+)/gaozi/delete/(?P<ID>\d+)/$', 'autonumber.DeleteGaoZi', name='DeleteGaoZi'),
    #--------------------------------------------------------------------------------
    url(r'^(?P<type>\d+)/tinggaozi/add/$', 'autonumber.AddTingGaoZi', name='AddTingGaoZi'),
    url(r'^(?P<type>\d+)/tinggaozi/list/$', 'autonumber.ListTingGaoZi', name='ListTingGaoZi'),
    url(r'^(?P<type>\d+)/tinggaozi/edit/(?P<ID>\d+)/$', 'autonumber.EditTingGaoZi', name='EditTingGaoZi'),
    url(r'^(?P<type>\d+)/tinggaozi/delete/(?P<ID>\d+)/$', 'autonumber.DeleteTingGaoZi', name='DeleteTingGaoZi'),
    #--------------------------------------------------------------------------------
    url(r'^(?P<type>\d+)/chuzi/add/$', 'autonumber.AddChuZi', name='AddChuZi'),
    url(r'^(?P<type>\d+)/chuzi/list/$', 'autonumber.ListChuZi', name='ListChuZi'),
    url(r'^(?P<type>\d+)/chuzi/edit/(?P<ID>\d+)/$', 'autonumber.EditChuZi', name='EditChuZi'),
    url(r'^(?P<type>\d+)/chuzi/delete/(?P<ID>\d+)/$', 'autonumber.DeleteChuZi', name='DeleteChuZi'),

)

'''
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
'''