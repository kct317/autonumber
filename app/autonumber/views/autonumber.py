#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from app.common.CommonPaginator import SelfPaginator
from app.autonumber.views.permission import PermissionVerify
from django.contrib.auth import get_user_model

from app.autonumber.form import CaseForm
from app.autonumber.models import Case,GlobalVar
from app.autonumber.config import CONFIG
import time
#--------------------------告字---------------------------

@login_required
@PermissionVerify()
def AddGaoZi(request, type):
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            osc = form.save(commit=False)
            osc.creater = request.user
            index = int(type) - 1
            osc.documentunit = CONFIG['left_panel'][index]['index']
            glvar = GlobalVar.objects.filter(id=1)[0]
            osc.informnumber = (CONFIG['documentnum'][type] % (time.strftime('%Y'), glvar.casecount1))
            osc.documenttype = '1'
            osc.save()
            glvar.casecount1 += 1
            glvar.save()
            return HttpResponseRedirect(reverse('ListGaoZi', args=(type,)))
    else:
        form = CaseForm()
    
    kwvars = {
        'form':form,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/gaozi_add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListGaoZi(request, type):
    index = int(type) - 1
    mList = Case.objects.filter(documenttype='1', documentunit=CONFIG['left_panel'][index]['index'])

    #分页功能
    lst = SelfPaginator(request, mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/gaozi_list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditGaoZi(request, type, ID):
    iGaozi = Case.objects.get(id=ID)

    if request.method == "POST":
        form = CaseForm(request.POST,instance=iGaozi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListGaoZi', args=(type,)))
    else:
        form = CaseForm(instance=iGaozi)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/gaozi_edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteGaoZi(request, type, ID):
    Case.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('ListGaoZi', args=(type,)))

@login_required
@PermissionVerify()
def SearchListGaoZi(request, type):
    index = int(type) - 1
    mList = Case.objects.filter(documenttype='1', documentunit=CONFIG['left_panel'][index]['index'], casename__contains=request.POST['query'])

    #分页功能
    lst = SelfPaginator(request, mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/gaozi_list.html',kwvars,RequestContext(request))


#---------------------------听告字-------------------------

@login_required
@PermissionVerify()
def AddTingGaoZi(request, type):
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            osc = form.save(commit=False)
            osc.creater = request.user
            index = int(type) - 1
            osc.documentunit = CONFIG['left_panel'][index]['index']
            glvar = GlobalVar.objects.filter(id=1)[0]
            osc.informnumber = (CONFIG['documentnum'][type] % (time.strftime('%Y'), glvar.casecount2))
            osc.documenttype = '2'
            osc.save()
            glvar.casecount2 += 1
            glvar.save()
            return HttpResponseRedirect(reverse('ListTingGaoZi', args=(type,)))
    else:
        form = CaseForm()
    
    kwvars = {
        'form':form,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/tinggaozi_add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListTingGaoZi(request, type):
    index = int(type) - 1
    mList = Case.objects.filter(documenttype='2', documentunit=CONFIG['left_panel'][index]['index'])

    #分页功能
    lst = SelfPaginator(request, mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/tinggaozi_list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditTingGaoZi(request, type, ID):
    iTingGaozi = Case.objects.get(id=ID)

    if request.method == "POST":
        form = CaseForm(request.POST,instance=iTingGaozi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListTingGaoZi', args=(type,)))
    else:
        form = CaseForm(instance=iTingGaozi)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/tinggaozi_edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteTingGaoZi(request, type, ID):
    Case.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('ListTingGaoZi', args=(type,)))

@login_required
@PermissionVerify()
def SearchListTingGaoZi(request, type):
    index = int(type) - 1
    mList = Case.objects.filter(documenttype='2', documentunit=CONFIG['left_panel'][index]['index'], casename__contains=request.POST['query'])

    #分页功能
    lst = SelfPaginator(request, mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/tinggaozi_list.html',kwvars,RequestContext(request))



#---------------------------处字--------------------------

@login_required
@PermissionVerify()
def AddChuZi(request, type):
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            osc = form.save(commit=False)
            osc.creater = request.user
            index = int(type) - 1
            osc.documentunit = CONFIG['left_panel'][index]['index']
            glvar = GlobalVar.objects.filter(id=1)[0]
            osc.informnumber = (CONFIG['documentnum'][type] % (time.strftime('%Y'), glvar.casecount3))
            osc.documenttype = '3'
            osc.save()
            glvar.casecount3 += 1
            glvar.save()
            return HttpResponseRedirect(reverse('ListChuZi', args=(type,)))
    else:
        form = CaseForm()
    
    kwvars = {
        'form':form,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/chuzi_add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListChuZi(request, type):
    index = int(type) - 1
    mList = Case.objects.filter(documenttype='3', documentunit=CONFIG['left_panel'][index]['index'])

    #分页功能
    lst = SelfPaginator(request, mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/chuzi_list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditChuZi(request, type, ID):
    iChuzi = Case.objects.get(id=ID)

    if request.method == "POST":
        form = CaseForm(request.POST,instance=iChuzi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListChuZi', args=(type,)))
    else:
        form = CaseForm(instance=iChuzi)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/chuzi_edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteChuZi(request, type, ID):
    Case.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('ListChuZi', args=(type,)))

@login_required
@PermissionVerify()
def SearchListChuZi(request, type):
    index = int(type) - 1
    mList = Case.objects.filter(documenttype='3', documentunit=CONFIG['left_panel'][index]['index'], casename__contains=request.POST['query'])

    #分页功能
    lst = SelfPaginator(request, mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
        'type':type,
        'config':CONFIG,
    }

    return render_to_response('autonumber/chuzi_list.html',kwvars,RequestContext(request))
