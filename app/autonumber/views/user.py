#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from app.common.CommonPaginator import SelfPaginator
from app.autonumber.views.permission import PermissionVerify

from django.contrib import auth
from django.contrib.auth import get_user_model
from app.autonumber.form import LoginUserForm,ChangePasswordForm,AddUserForm,EditUserForm
from app.autonumber.config import CONFIG

from django.core.mail import EmailMultiAlternatives

def LoginUser(request):
    '''用户登录view'''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    #if request.method == 'GET' and next request.GET.has_key('next'):
    if request.method == 'GET' and 'next' in request.GET:
        next = request.GET['next']
    else:
        next = '/'

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())   #将user_id user_backend存储到request的session，然后将这个session的存储到数据库表/缓存/文件系统
            return HttpResponseRedirect(request.POST['next'])
    else:
        form = LoginUserForm(request)

    kwvars = {
        'request':request,
        'form':form,
        'next':next,
    }

    return render_to_response('autonumber/login.html',kwvars,RequestContext(request))

def setEmail(request):
    if request.method == "POST":
        #        参考：https://django-chinese-docs-14.readthedocs.org/en/latest/topics/email.html
        #        方式一：
        #        send_mail('subject', 'this is the message of email', 'pythonsuper@gmail.com', ['1565208411@qq.com','1373763906@qq.com'], fail_silently=True)
        #        方式二：
        #         message1 = ('subject1','this is the message of email1','pythonsuper@gmail.com',['1565208411@qq.com','xinxinyu2011@163.com'])
        #         message2 = ('subject2','this is the message of email2','pythonsuper@gmail.com',['1373763906@qq.com','xinxinyu2011@163.com'])
        #         send_mass_mail((message1,message2), fail_silently=False)
        #        方式三：防止邮件头注入
        #         try:
        #             send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection)
        #         except BadHeaderError:
        #             return HttpResponse('Invaild header fount.')

        #        方式四：EmailMessage()
        #           首先实例化一个EmailMessage()对象
        #         em = EmailMessage('subject','body','from@example.com',['1565208411@qq.com'],['xinxinyu2011@163.com'],header={'Reply-to':'another@example.com'})
        #           调用相应的方法

        #         方式五：发送多用途邮件
        subject,form_email,to = 'hello','from@example.com','413817085@qq.com'
        text_content = 'This is an important message'
        html_content = u'<b>激活链接：</b><a href="http://www.baidu.com">http:www.baidu.com</a>'
        msg = EmailMultiAlternatives(subject,text_content,form_email,[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        
#       发送邮件成功了给管理员发送一个反馈
#       mail_admins(u'用户注册反馈', u'当前XX用户注册了该网站', fail_silently=True)
        return HttpResponse(u'发送邮件成功')
    return render_to_response('common/test.html')


@login_required
def LogoutUser(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def ChangePassword(request):
    if request.method=='POST':
        form = ChangePasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logouturl'))
    else:
        form = ChangePasswordForm(user=request.user)

    kwvars = {
        'form':form,
        'request':request,
        'config':CONFIG,
    }

    return render_to_response('autonumber/password_change.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListUser(request):
    mList = get_user_model().objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
        'config':CONFIG,
    }

    return render_to_response('autonumber/user_list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def AddUser(request):
    if request.method=='POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])

            form.save()
            return HttpResponseRedirect(reverse('listuserurl'))
    else:
        form = AddUserForm()

    kwvars = {
        'form':form,
        'request':request,
        'config':CONFIG,
    }

    return render_to_response('autonumber/user_add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditUser(request,ID):
    user = get_user_model().objects.get(id = ID)

    if request.method=='POST':
        form = EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listuserurl'))
    else:
        form = EditUserForm(instance=user
        )

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
        'config':CONFIG,
    }

    return render_to_response('autonumber/user_edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteUser(request,ID):
    if ID == '1':
        return HttpResponse(u'超级管理员不允许删除!!!')
    else:
        get_user_model().objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('listuserurl'))

@login_required
@PermissionVerify()
def ResetPassword(request,ID):
    user = get_user_model().objects.get(id = ID)

    newpassword = get_user_model().objects.make_random_password(length=10,allowed_chars='abcdefghjklmnpqrstuvwxyABCDEFGHJKLMNPQRSTUVWXY3456789')
    print('====>ResetPassword:%s-->%s' %(user.username,newpassword))
    user.set_password(newpassword)
    user.save()

    kwvars = {
        'object':user,
        'newpassword':newpassword,
        'request':request,
        'config':CONFIG,
    }

    return render_to_response('autonumber/password_reset.html',kwvars,RequestContext(request))
