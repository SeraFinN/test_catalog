# coding=utf-8
import random
import string

from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from testapp.models import Product, Categories
from testapp.pagination import get_page


def main(request):
    context = {
        'title': u'Электронный каталог',
        'breadcrumbs': None,
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))


def product_details(request, **params):
    product = get_object_or_404(Product, id=params['pk'])
    context = {
        'product': product,
        'title': product.name,
        'breadcrumbs': product.category.get_breadcrumbs() + [(product.name, None)],
    }
    return render_to_response('product_details.html', context, context_instance=RequestContext(request))


def product_list(request, **params):
    current_category = get_object_or_404(Categories, slug=params.get('slug'))
    if request.path != current_category.get_absolute_url():
        raise Http404

    products = Product.released.for_user(request.user).filter(category=current_category)
    context = {
        'title': u'Категория - %s' % current_category.name,
        'current_category': current_category,
        'breadcrumbs': current_category.get_breadcrumbs(),
        'item_list': get_page(products, request.GET.get('page'), 12),
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))


def search(request):
    query = request.GET.get('q', None)
    user = request.user
    products = Product.released.for_user(user).filter(name__icontains=query) if query else Product.objects.none()
    if not request.user.is_authenticated():
        products = products.exclude(is_hidden=True)
    context = {
        'title': u'Категория - %s' % u'Поиск: %s' % query,
        'breadcrumbs': [(u'Поиск: %s' % query, None)],
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
