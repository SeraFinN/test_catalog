# coding=utf-8
from django.http import Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .formater import prepare_data
from .models import Product, Categories


def product_list(request, **params):
    is_main = True
    breadcrumbs = []
    products_page = None
    products = None
    current_category = None
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        is_main = False
        breadcrumbs += [(u'Поиск: ' + q, None)]
        products = Product.objects.filter(name__icontains=q)
    elif params and params['slug']:
        is_main = False
        try:
            current_category = Categories.objects.get(slug__iexact=params['slug'])
            breadcrumbs = current_category.get_breadcrumbs()
        except Categories.DoesNotExist:
            raise Http404
        if not request.path == current_category.get_absolute_url():
            raise Http404
        products = Product.objects.filter(category=current_category)

    if products:
        paginator = Paginator(products, 12)
        page = request.GET.get('page')

        try:
            products_page = paginator.page(page)
            products_page.next_page_number()
        except PageNotAnInteger:
            products_page = paginator.page(1)
        except EmptyPage:
            products_page = paginator.page(paginator.num_pages)

    context = dict()
    context['current_category'] = current_category
    context['item_list'] = products_page
    context['breadcrumbs'] = breadcrumbs
    context['is_main'] = is_main
    context['get_params'] = request.GET.copy()
    context['categories_list'] = prepare_data(Categories.objects.all().values('id', 'parent_id', 'name'))
    return render_to_response('product_list.html', context)


def product_details(request, **params):
    if not params:
        raise Http404
    try:
        product = Product.objects.get(id=params['id'])
    except Product.DoesNotExist:
        raise Http404
    context = dict()
    context['current_category'] = None
    context['is_main'] = False
    context['product'] = product
    context['categories_list'] = prepare_data(Categories.objects.all().values('id', 'parent_id', 'name'))
    context['breadcrumbs'] = product.category.get_breadcrumbs() + [(product.name, None)]
    return render_to_response('product_details.html', context)
