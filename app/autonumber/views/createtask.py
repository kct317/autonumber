#coding:utf-8
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def createtask(request):
    if request.method == 'GET':
        form = CreatetaskForm(initial={
        'creater':request.user.last_name + request.user.first_name,
        })
        return render_to_response('createtask.html', RequestContext(request, {'form': form,}))
    else:
        form = CreatetaskForm(request.POST,request.FILES)
        if form.is_valid():
            username = request.user.username
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
            return render_to_response('base.html', RequestContext(request,{'createtask_success':True,}))
        else:
            return render_to_response('createtask.html', RequestContext(request, {'form': form,}))