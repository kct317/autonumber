#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

def index(request):
    return HttpResponse(u"welcome !")
	
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))	

def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def link(request):
    tmp = "<a href=\"{% http://127.0.0.1:8000/ 'add2' 4 5 %}\">link</a>"
    return HttpResponse(tmp)

def home(request):
    return render(request, 'base_ex.html')

def json(request):
    List = ['kct', 'render to template']
    return render(request, 'json.html', {'List': List})

def form_get(request):
    return render(request, 'form_get.html')

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

def form1(request):
    if request.method == 'POST':# 当提交表单时
     
        form = AddForm(request.POST) # form 包含提交的数据
         
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
     
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'form1.html', {'form': form})


def test(request):
    return render(request, 'test.html')


def 11(request):
    return render(request, '11.html')