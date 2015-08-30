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

from app.autonumber.config import CONFIG


@login_required
def index_list(request, model, place, type):
    username = request.session.get('username','')
    has_permission = False
    if username != '':
        has_permission = True
    obj_list = model.objects.all()

    pydata = {}
    pydata['username'] = username
    pydata['has_permission'] = has_permission
    pydata['CONFIG'] = CONFIG
    pydata['obj_list'] = obj_list
    return render(request, 'index_list.html', pydata)