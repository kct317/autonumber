#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

@login_required
def tasklist(request):
    username=request.user.username
    if len(Dba.objects.filter(username=username)) == 0: #User is not DBA, only shows his/her own tasklist
        userid=User.objects.filter(username=username)
        lines = Task.objects.filter(creater=userid).order_by("-id")
    else:   #User is DBA, shows all tasklist
        lines = Task.objects.order_by("-id")
    paginator = Paginator(lines, 10)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return render_to_response('autonumber/tasklist.html', RequestContext(request, {'lines': show_lines,}))