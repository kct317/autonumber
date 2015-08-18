#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from app.autonumber.models import * 
from django.views.generic.list import ListView
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect 
from django.template import RequestContext 

"""
登录相关
"""
#登陆成功
def index(request):
    username = request.COOKIES.get('username','')
    return render(request,'index.html' ,{'username':username})
