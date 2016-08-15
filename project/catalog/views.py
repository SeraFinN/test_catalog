# coding=utf-8
from django.http import Http404
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404, render_to_response

from catalog.pagination import get_page
from catalog.models import Product, Categories


def main(request):
    context = {'title': u'Электронный каталог'}
    return render_to_response('sidebar_base.html', context, context_instance=RequestContext(request))


def product_details(request, **params):
    product = get_object_or_404(Product.released.for_user(request.user), pk=params['pk'])
    context = {
        'product': product,
        'title': product.name,
        'breadcrumbs': product.category.get_breadcrumbs() + [{'name': product.name}],
    }
    return render_to_response('product_details.html', context, context_instance=RequestContext(request))


@cache_page(900)
def product_list(request, **params):
    category = get_object_or_404(Categories, slug=params.get('slug').lower())
    if request.path.lower() != category.get_absolute_url():
        raise Http404
    products = Product.released.for_user(request.user)
    context = {
        'title': u'Категория - %s' % category.name,
        'current_category': category,
        'breadcrumbs': category.get_breadcrumbs(),
        'item_list': get_page(products.filter(category=category), request.GET.get('page')),
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))


def search(request):
    query = request.GET.get('q', '')
    products = Product.released.for_user(request.user)
    products = products.filter(name__icontains=query) if query else products.none()
    context = {
        'title': u'Поиск: %s' % query,
        'breadcrumbs': [{'name': u'Поиск: %s' % query}],
        'item_list': get_page(products, request.GET.get('page'), 12),
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))
