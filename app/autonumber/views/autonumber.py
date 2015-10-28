#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from app.common.CommonPaginator import SelfPaginator
from app.autonumber.views.permission import PermissionVerify

from app.autonumber.form import RoleListForm
from app.autonumber.models import case

@login_required
@PermissionVerify()
def AddGaoZi(request):
    if request.method == "POST":
        form = RoleListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = RoleListForm()

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('autonumber/role_add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListGaoZi(request):
    mList = RoleList.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('autonumber/role_list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditGaoZi(request,ID):
    iRole = RoleList.objects.get(id=ID)

    if request.method == "POST":
        form = RoleListForm(request.POST,instance=iRole)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = RoleListForm(instance=iRole)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('autonumber/role_edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteGaoZi(request,ID):
    RoleList.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('listroleurl'))
