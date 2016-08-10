# coding=utf-8
import random
import string

from django.http import Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect

from catalog.pagination import get_page
from catalog.models import Product, Categories


def main(request):
    context = {
        'title': u'Электронный каталог',
        'breadcrumbs': None,
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))


def product_details(request, **params):
    product = get_object_or_404(Product, pk=params['pk'])
    context = {
        'product': product,
        'title': product.name,
        'breadcrumbs': product.category.get_breadcrumbs() + [{'name': product.name}],
    }
    return render_to_response('product_details.html', context, context_instance=RequestContext(request))


def product_list(request, **params):
    current_category = get_object_or_404(Categories, slug=params.get('slug'))
    if request.path != current_category.get_absolute_url():
        raise Http404
    products = Product.objects.all() if request.user.is_authenticated() else Product.released.all()
    context = {
        'title': u'Категория - %s' % current_category.name,
        'current_category': current_category,
        'breadcrumbs': current_category.get_breadcrumbs(),
        'item_list': get_page(products.filter(category=current_category), request.GET.get('page')),
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))


def search(request):
    query = request.GET.get('q', '')
    user = request.user
    products = Product.objects.all() if request.user.is_authenticated() else Product.released.all()
    products = products.filter(name__icontains=query) if query else Product.objects.none()
    context = {
        'title': u'Поиск: %s' % query,
        'breadcrumbs': [{'name': u'Поиск: %s' % query}],
        'item_list': get_page(products, request.GET.get('page'), 12),
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))


def fill_db(request):
    categories = Categories.objects.all()
    for category in categories:
        if Product.objects.all().filter(category=category).count() == 0:
            for i in range(100):
                description_source = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.whitespace
                token = ''.join(random.choice(description_source) for x in range(1000))
                product = Product(name='%s %s' % (category, i), category=category, image=None, count=1, price=1,
                                  description=token, is_hidden=bool(random.getrandbits(1))
                                  )
                product.save()
    return redirect('/')
