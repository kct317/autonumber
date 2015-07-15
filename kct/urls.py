from django.conf.urls import include, url
from django.contrib import admin
from autonumber import views as autoviews
from  django.views.generic.list import ListView

"""
配置方法
	http://www.cnblogs.com/whscfan/p/4524376.html
"""

"""
通用视图
1、
    from  django.views.generic import TemplateView
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
2、
	from  django.views.generic.list import ListView
	book_info = {
		'queryset' : Book.object.all,  # all()是静态加载==一次性==不改变    all会动态加载
 		'template_name' : "about.html"
	}
	url(r'^about/', ListView.as_view(**book_info)),
	然后在相应的模板文件about.html ：
		{% for b in object_list %}
			{{ b.title }}
		{% endfor %}
"""

urlpatterns = [
    # Examples:
    # url(r'^$', 'kct.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), # admin目录下site.py的urls函数  http://127.0.0.1:8000/admin   admin:admin
	
	# test
	url(r'^$', autoviews.index), # http://127.0.0.1:8000/
	url(r'^add/$', autoviews.add), # http://127.0.0.1:8000/add/?a=4&b=5
	url(r'^add2/(\d+)/(\d+)/$', autoviews.add2), # http://127.0.0.1:8000/add2/4/5/
	url(r'^link/$', autoviews.link), # http://127.0.0.1:8000/link
	url(r'^home/$', autoviews.home), # http://127.0.0.1:8000/home
	url(r'^json/$', autoviews.json), # http://127.0.0.1:8000/json
	url(r'^form_get/$', autoviews.form_get), # http://127.0.0.1:8000/form_get
	url(r'^form1/$', autoviews.form1), # http://127.0.0.1:8000/form1
	url(r'^test/$', autoviews.test), # http://127.0.0.1:8000/test
	url(r'^foo1/(?P<Month>\d+)/(?P<Day>\d+)/$', autoviews.foo, {'func':autoviews.view1}), # http://127.0.0.1:8000/foo1/7/12
	url(r'^foo2/(?P<Month>\d+)/(?P<Day>\d+)/$', autoviews.foo, {'func':autoviews.view2}), # http://127.0.0.1:8000/foo2/7/12
	url(r'^foo3/', autoviews.ArticleListView.as_view(), {'func':autoviews.view1}), # http://127.0.0.1:8000/foo3/   通用视图
	url(r'^view3/', autoviews.view3), # http://127.0.0.1:8000/view3/   使用缓存

	# login


	# logout


]
