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
  
from app.autonumber.form import RegisterForm, LoginForm

def register(request):
    if request.method == 'GET':  
        form = RegisterForm()  
        return render_to_response('register.html', RequestContext(request, {'form': form,}))  
    else:  
        form = RegisterForm(request.POST)
        if form.is_valid():  
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password1"]
            user=User.objects.create_user(username,email,password)
            user.save()#写入数据库
            newform = LoginForm()
            return render_to_response('login.html', RequestContext(request,{'register_success':True, 'form': newform, })) 
        else:  
            return render_to_response('register.html', RequestContext(request, {'form': form,}))