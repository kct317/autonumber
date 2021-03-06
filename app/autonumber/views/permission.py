#!/usr/bin/env python
#-*- coding: utf-8 -*-
 

from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from app.common.CommonPaginator import SelfPaginator
from app.autonumber.form import PermissionListForm
from app.autonumber.models import User,RoleList,PermissionList
from app.autonumber.config import CONFIG

def PermissionVerify():
    '''权限认证模块,
        此模块会先判断用户是否是管理员（is_superuser为True），如果是管理员，则具有所有权限,
        如果不是管理员则获取request.user和request.path两个参数，判断两个参数是否匹配，匹配则有权限，反之则没有。
    '''
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            iUser = User.objects.get(username=request.user)

            #if not iUser.is_superuser: #判断用户如果是超级管理员则具有所有权限
            if not iUser.is_active: #判断用户是否正常
                if not iUser.role: #如果用户无角色，直接返回无权限
                    return HttpResponseRedirect(reverse('permissiondenyurl'))

                role_permission = RoleList.objects.get(name=iUser.role)
                role_permission_list = role_permission.permission.all()

                matchUrl = []
                for x in role_permission_list:
                    if request.path == x.url or request.path.rstrip('/') == x.url: #精确匹配，判断request.path是否与permission表中的某一条相符
                        matchUrl.append(x.url)
                    elif request.path.startswith(x.url): #判断request.path是否以permission表中的某一条url开头
                        matchUrl.append(x.url)
                    else:
                        pass

                print('%s---->matchUrl:%s' % (request.user, str(matchUrl) ) )
                if len(matchUrl) == 0:
                    return HttpResponseRedirect(reverse('permissiondenyurl'))
            else:
                if not iUser.is_superuser:
                    if 'user' in request.path or 'role' in request.path or 'permission' in request.path:
                        return HttpResponseRedirect(reverse('permissiondenyurl'))

            return view_func(request, *args, **kwargs)
        return _wrapped_view

    return decorator

@login_required
def NoPermission(request):

    kwvars = {
        'request':request,
        'config':CONFIG,
    }

    return render_to_response('autonumber/permission_no.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def AddPermission(request):
    if request.method == "POST":
        form = PermissionListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listpermissionurl'))
    else:
        form = PermissionListForm()

    kwvars = {
        'form':form,
        'request':request,
        'config':CONFIG,
    }

    return render_to_response('autonumber/permission_add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListPermission(request):
    mList = PermissionList.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
        'config':CONFIG,
    }

    return render_to_response('autonumber/permission_list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditPermission(request,ID):
    iPermission = PermissionList.objects.get(id=ID)

    if request.method == "POST":
        form = PermissionListForm(request.POST,instance=iPermission)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listpermissionurl'))
    else:
        form = PermissionListForm(instance=iPermission)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
        'config':CONFIG,
    }

    return render_to_response('autonumber/permission_edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeletePermission(request,ID):
    PermissionList.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('listpermissionurl'))
