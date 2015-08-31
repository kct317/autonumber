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
def index_list(request, model):
    username = request.session.get('username','')
    has_permission = False
    if username != '':
        has_permission = True
    show_list = []
    unit = request.GET.get('unit') or 0 
    ntype = request.GET.get('type') or 0
    obj_list = model.objects.filter(documentunit__exact=unit, documenttype__exact=ntype)

    paginator = Paginator(obj_list, 10)
    page = request.GET.get('page')
    try:
        show_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_list = paginator.page(paginator.num_pages)
    pydata = {}
    pydata['username'] = username
    pydata['has_permission'] = has_permission
    pydata['unit'] = unit
    pydata['type'] = ntype
    pydata['CONFIG'] = CONFIG
    pydata['obj_list'] = show_list
    return render(request, 'index_list.html', pydata)
    