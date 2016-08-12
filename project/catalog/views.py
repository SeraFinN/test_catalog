# coding=utf-8
from django.http import Http404, HttpRequest
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.cache import get_cache_key, learn_cache_key
from django.core.cache import get_cache
from django.http import HttpResponse

from django.views.decorators.vary import vary_on_headers

from catalog.pagination import get_page
from catalog.models import Product, Categories


def main(request):
    from django.core.cache.backends import locmem
    # for i in [x for x in locmem._caches.values()]:
    cache.get(Categories.__name__)
    print cache.get(Categories.__name__)
    if cache.get(Categories.__name__):
        for i in cache.get(Categories.__name__):
            reque = HttpRequest()
            reque.path = i.get_absolute_url()
            print 'cache_view %s - %s' % (bool(cache.get(get_cache_key(reque))), i.name)
    # cache.clear()
    print 'is_authenticated %s' % request.user.is_authenticated()
    context = {'title': u'Электронный каталог'}
    # print 'main %s' % cache.get('test')
    return render_to_response('sidebar_base.html', context, context_instance=RequestContext(request))


@cache_page(60 * 5)
def product_details(request, **params):

    print 'test  key %s' % get_cache_key(request)
    from django.core.cache.backends import locmem
    for i in [x for x in locmem._caches.values()]:
         print 'keys:%s\nvals:%s\n\n' % (i.keys(), i.values())
    # cache.clear()
    products = Product.objects if request.user.is_authenticated() else Product.released
    product = get_object_or_404(products, pk=params['pk'])
    context = {
        'product': product,
        'title': product.name,
        'breadcrumbs': product.category.get_breadcrumbs() + [{'name': product.name}],
    }
    return render_to_response('product_details.html', context, context_instance=RequestContext(request))


@vary_on_headers('User-Agent', 'Cookie')
@cache_page(60 * 5)
def product_list(request, **params):
    # assert False, request.get_full_path()
    print 'test  key %s' % get_cache_key(request)
    print 'test  key %s' % cache.get(get_cache_key(request))
    from django.core.cache.backends import locmem
    print locmem._caches.values()
    # cache.clear()
    category = get_object_or_404(Categories, slug=params.get('slug').lower())
    if request.path.lower() != category.get_absolute_url():
        raise Http404
    products = Product.objects if request.user.is_authenticated() else Product.released
    context = {
        'title': u'Категория - %s' % category.name,
        'current_category': category,
        'breadcrumbs': category.get_breadcrumbs(),
        'item_list': get_page(products.filter(category=category), request.GET.get('page')),
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))


def search(request):
    query = request.GET.get('q', '')
    products = Product.objects if request.user.is_authenticated() else Product.released
    products = products.filter(name__icontains=query) if query else products.none()
    context = {
        'title': u'Поиск: %s' % query,
        'breadcrumbs': [{'name': u'Поиск: %s' % query}],
        'item_list': get_page(products, request.GET.get('page'), 12),
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))


def test():
    cache.get(Categories.__name__)
    print cache.get(Categories.__name__)
    if cache.get(Categories.__name__):
        for i in cache.get(Categories.__name__):
            reque = HttpRequest()
            reque.path = i.get_absolute_url()
            print 'cache_view %s - %s' % (bool(cache.get(get_cache_key(reque))), i.name)
    # cache.clear()
    reque = HttpRequest()
    reque.path = '/product/1205'
    print 'cache_view_details %s' % cache.get(get_cache_key(reque))
    # print 'is_authenticated %s' % request.user.is_authenticated()