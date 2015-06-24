#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")
	
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
    List = ['自强学堂', '渲染Json到模板']
    return render(request, 'json.html', {'List': List})