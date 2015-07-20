#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from autonumber.models import * 
from  django.views.generic.list import ListView
from django.core.cache import cache
from django.views.decorators.cache import cache_page

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

def view1(request, num):
    return render(request, 'foo.html', {'num': int(num), 'key':"hello"})

def view2(request, num):
    return render(request, 'foo.html', {'num': int(num)**2, 'key':"hello"})

def foo(request, func, Month, Day):
    def footest(request):
        num = int(Month) + int(Day)
        return func(request, num)
    return footest(request)

class ArticleListView(ListView):
    model = Article
    #queryset = Article.objects.filter(content_icontains="aaa")
    queryset = Article.objects.all
    template_name = "foo.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        return context

"""
局部缓存，下面只缓存变量article
"""
def view3(request):
    if cache.get('article'):
        b = cache.get('article')
    else:
        b = Article.objects.all
        cache.set('article', b)
    return render(request, 'foo.html', {'object_list':b})

"""
对整个视图进行缓存
"""
@cache_page(60*15)
def view4(request):
    b = Article.objects.all
    return render(request, 'foo.html', {'object_list':b})



