# coding=utf-8
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response

from .formater import prepare_data
from .models import Product, Categories
from pagination import get_page


def product_list(request, **params):
    current_category = get_object_or_404(Categories, slug__iexact=params.get('slug'))
    if request.path != current_category.get_absolute_url():
        raise Http404
    products = Product.objects.filter(category=current_category)
    context = dict()
    context['item_list'] = get_page(products, request.GET.get('page'), 12)
    context['get_params'] = request.GET.copy()
    context['current_category'] = current_category
    context['breadcrumbs'] = current_category.get_breadcrumbs()
    context['categories_list'] = prepare_data(Categories.objects.all().values('id', 'parent_id', 'name'))
    return render_to_response('product_list.html', context)


def search(request):
    q = request.GET.get('q', None)
    products = Product.objects.filter(name__icontains=q) if q else Product.objects.none()
    context = dict()
    context['get_params'] = request.GET.copy()
    context['breadcrumbs'] = [(u'Поиск: %s' % q, None)]
    context['item_list'] = get_page(products, request.GET.get('page'), 12)
    context['categories_list'] = prepare_data(Categories.objects.all().values('id', 'parent_id', 'name'))
    return render_to_response('product_list.html', context)


def main(request):
    context = dict()
    context['is_main'] = True
    context['categories_list'] = prepare_data(Categories.objects.all().values('id', 'parent_id', 'name'))
    return render_to_response('product_list.html', context)


def product_details(request, **params):
    if not params:
        raise Http404
    product = get_object_or_404(Product, id=params['id'])
    context = dict()
    context['product'] = product
    context['categories_list'] = prepare_data(Categories.objects.all().values('id', 'parent_id', 'name'))
    context['breadcrumbs'] = product.category.get_breadcrumbs() + [(product.name, None)]
    return render_to_response('product_details.html', context)
