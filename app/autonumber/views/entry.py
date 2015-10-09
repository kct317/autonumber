#coding:utf-8
from django.shortcuts import render_to_response,render,get_object_or_404  
from django.http import HttpResponse, HttpResponseRedirect  
from django.contrib.auth.models import User  
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from .common import SessionExpiredMiddleware
from .index_list import index_list

@login_required
def entry(request, func, model):
    def wrapper(request):
        if SessionExpiredMiddleware.process_request(session=request.session):
            return HttpResponseRedirect("/logout/")
        return func(request, model)
    return wrapper(request)