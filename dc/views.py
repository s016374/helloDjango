from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import datetime
from django.template import Context, Template

# Create your views here.
from django.template.loader import get_template


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" %now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def current_datetime_by_temp(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})

def hours_ahead_by_temp(request, offset, add):
    offset = int(offset)
    add = int(add)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('hours_ahead.html')
    html = t.render(Context({'offset': offset, 'dt': dt, 'add': add}))
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def hours_ahead_by_temp_by_render_to_response(request, offset, add):
    offset = int(offset)
    add = int(add)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'offset': offset, 'dt': dt, 'add': add})

def hello(request):
    now = datetime.datetime.now()
    # render_to_response('current_datetime.html', {'current_date': now})
    t = get_template('current_datetime.html')
    t.render(Context({'current_date': now}))
    return render(request,'index/hello.html')
    # return render_to_response(request, 'index/hello.html', {'current_date': now})

def page1(request):
    c = {'person_name': 'Sam', 'company': 'DdD', 'item_list':{'A','B','C'}, 'ordered_warranty': True, 'ship_date': '2015,4,8', 'section': 's'}
    return render(request, 'page1.html', c)

def sample(request):
    return render(request, 'sample.html')
    pass

def carol(request):
    return render(request, 'carol/index.html')
    pass