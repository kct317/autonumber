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
    return render(request, 'test.html', 
        {'categories':
            [{'name':'aaaa',},
            {'name':'bbbb',},
            ],
        })

def view1(request, num):
    return render(request, 'foo.html', {'num': int(num), 'key':"hello"})

def view2(request, num):
    return render(request, 'foo.html', {'num': int(num)**2, 'key':"hello"})

def foo(request, func, Month, Day):
    def footest(request):
        num = int(Month) + int(Day)
        return func(request, num)
    return footest(request)

"""
class ArticleListView(ListView):
    model = Article
    #queryset = Article.objects.filter(content_icontains="aaa")
    queryset = Article.objects.all
    template_name = "foo.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        return context
"""

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


def templateview(request):
    return render(request, 'base.html', {'has_permission':True, 'site_url':True,} )

"""
登录相关
"""
class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

    def as_myp(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = '<div class="form-group">%(label)s</div> <div class="form-group">%(field)s</div>',
            #normal_row = '<p%(html_class_attr)s>%(label)s</p> <p%>(field)s</p>',
            error_row = '%s',
            row_ender = '</p>',
            help_text_html = ' <span class="helptext">%s</span>',
            errors_on_separate_row = True)

    def as_plain(self):
        "Returns this form rendered as HTML <tr>s -- excluding the <table></table>."
        return self._html_output(
            normal_row = '%(label)s%(errors)s%(field)s%(help_text)s',
            error_row = '%s',
            row_ender = ' ',
            help_text_html = '<br /><span class="helptext">%s</span>',
            errors_on_separate_row = False)

#登陆
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render(request,'login.html', {'uf':uf}, context_instance=RequestContext(request))

#注册
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username=username,password=password)
            return HttpResponse('register success!!')
    else:
        uf = UserForm()
    return render(request,'register.html',{'uf':uf}, context_instance=RequestContext(request))

#登陆成功
def index(request):
    username = request.COOKIES.get('username','')
    return render(request,'index.html' ,{'username':username})

#退出
def logout(request):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response
