#coding:utf-8
from django.shortcuts import render_to_response,render,get_object_or_404  
from django.http import HttpResponse, HttpResponseRedirect  
from django.contrib.auth.models import User  
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from app.autonumber.form import ForgetPwdForm



def forgetpwd(request):
    if request.method == 'GET':  
        form = ForgetPwdForm()  
        return render_to_response('forgetpwd.html', RequestContext(request, {'form': form,}))
    else:  
        form = ForgetPwdForm(request.POST)  
        if form.is_valid():  
            email = request.POST.get('email', '')
            #将重置密码的特殊链接发邮箱
            return HttpResponseRedirect("/login/")
        else:  
            return render_to_response('forgetpwd.html', RequestContext(request, {'form': form,}))