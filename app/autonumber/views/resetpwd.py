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

from libs.views.form import ChangepwdForm



@login_required
def resetpwd(request):  
    if request.method == 'GET':  
        form = ChangepwdForm()  
        return render_to_response('resetpwd.html', RequestContext(request, {'form': form,}))  
    else:  
        form = ChangepwdForm(request.POST)  
        if form.is_valid():  
            username = request.user.username  
            oldpassword = request.POST.get('oldpassword', '')  
            user = auth.authenticate(username=username, password=oldpassword)  
            if user is not None and user.is_active:  
                newpassword = request.POST.get('newpassword1', '')  
                user.set_password(newpassword)  
                user.save()  
                return render_to_response('index.html', RequestContext(request,{'changepwd_success':True}))  
            else:  
                return render_to_response('resetpwd.html', RequestContext(request, {'form': form,'oldpassword_is_wrong':True}))  
        else:  
            return render_to_response('resetpwd.html', RequestContext(request, {'form': form,}))