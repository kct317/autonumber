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
from .common import SessionExpiredMiddleware, GetCaseSerialNumber
from libs.views.form import CreateCaseForm

@login_required
def index_list(request, model):
    if SessionExpiredMiddleware.process_request(session=request.session):
        return HttpResponseRedirect("/logout/")
    username = request.session.get('username','')
    has_permission = False
    if username != '':
        has_permission = True

    unit = request.GET.get('unit') or 0 
    ntype = request.GET.get('type') or 0

    if request.method == 'GET':
        serialnum = GetCaseSerialNumber.get(unit)
        form = CreateCaseForm(initial={'creater':username, 'casename':serialnum})
    else:
        form = CreateCaseForm(request.POST, request.FILES)
        if form.is_valid():
            t = Task.objects.create(
                creater = User.objects.get(username=username),
                manager = form.cleaned_data['manager'],
                dba = Dba.objects.get(id=1),
                state = State.objects.get(statename='Open'),
                sql = form.cleaned_data['sql'],
                desc = form.cleaned_data['desc'],
                createdtime = datetime.datetime.now(),
                lastupdatedtime = datetime.datetime.now(),
                attachment = form.cleaned_data['attachment'],
            )
            databaselist = form.cleaned_data['databases']
            for db in databaselist:
                t.databases.add(db)
            t.save()

    show_list = []
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
    pydata['form'] = form
    return render(request, 'index_list.html', pydata)
    