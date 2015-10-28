#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from app.common.CommonPaginator import SelfPaginator
from app.autonumber.views.permission import PermissionVerify

from app.autonumber.form import CaseForm
from app.autonumber.models import Case

@login_required
@PermissionVerify()
def AddGaoZi(request, type):
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = CaseForm()

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('autonumber/role_add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListGaoZi(request, type):
    mList = Case.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('autonumber/role_list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditGaoZi(request, type, ID):
    iRole = RoleList.objects.get(id=ID)

    if request.method == "POST":
        form = CaseForm(request.POST,instance=iRole)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = CaseForm(instance=iRole)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('autonumber/role_edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteGaoZi(request, type, ID):
    Case.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('listroleurl'))
