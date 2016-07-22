# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime


def hello(request):
    print(request)
    return HttpResponse("Hello world")


def hours_ahead(request, offset):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': hours_ahead1('dasdasdasd')})


def hours_ahead1(ttt):
    now = datetime.datetime.now()
    return 'test1' + ttt