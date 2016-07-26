# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from testapp.models import Product

register = template.Library()

from testapp.models import Categories

register = template.Library()


def product_list(request, *params):
    categories = Categories.objects.all()
    categories = sorted(categories, key=lambda category: (category.get_absolute_url()))


    path = filter(bool, request.path.split('/'))[-1].lower()
    category = Categories.objects.get(slug=path)
    ids = get_child_ids(category)

    products = Product.objects.filter(category__in=ids)

    paginator = Paginator(products, 12)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render_to_response('product_list.html',
                              {'request': request, 'category_list': categories, 'current_path': request.path, 'item_list': items})


def categories(request):
    categories = Categories.objects.all()
    categories = sorted(categories, key=lambda category: (category.get_absolute_url()))
    return {'category_list': categories, 'current_path': request.path}


def items(request):
    path = filter(bool, request.path.split('/'))[-1].lower()
    category = Categories.objects.get(slug=path)
    ids = get_child_ids(category)

    products = Product.objects.filter(category__in=ids)

    paginator = Paginator(products, 12)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return {'item_list': items}


def get_child_ids(category):
    ids = []
    childs = Categories.objects.filter(parent=category.id)
    ids.append(category.id)
    for child in childs:
        # ids.append(child.id)
        ids += get_child_ids(child)
    return ids
