from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'kct.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), # admin目录下site.py的urls函数  http://127.0.0.1:8000/admin   admin:admin
	
	url(r'^$', 'autonumber.views.index', name='index'), # http://127.0.0.1:8000/
	url(r'^add/$', 'autonumber.views.add', name='add'), # http://127.0.0.1:8000/add/?a=4&b=5
	url(r'^add2/(\d+)/(\d+)/$', 'autonumber.views.add2', name='add2'), # http://127.0.0.1:8000/add2/4/5/
	url(r'^link/$', 'autonumber.views.link', name='link'), # http://127.0.0.1:8000/link
	url(r'^home/$', 'autonumber.views.home', name='home'), # http://127.0.0.1:8000/home
	url(r'^json/$', 'autonumber.views.json', name='json'), # http://127.0.0.1:8000/json
]
