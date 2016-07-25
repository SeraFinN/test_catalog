# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import template
from testapp.models import Categories
register = template.Library()


def bd_test(request):
    # c = Categories(name='Мониторы', parent=-1, level=0, url='/monitors/')
    # c.save()
    #
    # c2 = Categories(name='19', parent=c.id, level=c.level + 1, url='/monitors/19/')
    # c2.save()
    # c3 = Categories(name='27', parent=1, level=1, url='/monitors/27/')
    # c3.save()
    # c1 = Categories(name='Процессоры', parent=-1, level=0, url='/cpu/')
    # c1.save()
    #
    # c4 = Categories(name='Intel', parent=c1.id, level=c1.level + 1, url='/cpu/intel/')
    # c4.save()
    # c5 = Categories(name='AMD', parent=c1.id, level=c1.level + 1, url='/cpu/amd/')
    # c5.save()
    #
    # c6 = Categories(name='Notebook', parent=c4.id, level=c4.level + 1, url='/cpu/intel/mobile/')
    # c6.save()


    return HttpResponse(Categories.objects.all())

def product_list(request, *params):
    return render_to_response('main.html', {'request': request})