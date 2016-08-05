# coding=utf-8
import random
import string
from datetime import datetime

from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import ListView

from testapp.models import Product, Categories


class FilteredListView(ListView):
    model = Product
    context_object_name = 'item_list'
    template_name = 'product_list.html'
    paginate_by = 12

    def get_queryset(self):
        products = self.model.objects.all().filter(release_date__lt=datetime.now())
        if not self.request.user.is_authenticated():
            products = self.model.objects.exclude(is_hidden=True)
            return products
        return products


class ProductsListView(FilteredListView):
    def __init__(self):
        super(FilteredListView, self).__init__()
        self.current_category = None

    def get_queryset(self):
        self.current_category = get_object_or_404(Categories, slug=self.kwargs.get('slug'))
        if self.request.path != self.current_category.get_absolute_url():
            raise Http404
        return super(ProductsListView, self).get_queryset().filter(category=self.current_category)

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = u'Категория - %s' % self.current_category.name
        context['current_category'] = self.current_category
        context['breadcrumbs'] = self.current_category.get_breadcrumbs()
        return context


class SearchListView(FilteredListView):
    def __init__(self):
        super(FilteredListView, self).__init__()
        self.query = ''

    def get_queryset(self):
        self.query = self.request.GET.get('q', '')
        searched_product = super(SearchListView, self).get_queryset().filter(name__icontains=self.query)
        products = searched_product if self.query else Product.objects.none()
        return products

    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        context['title'] = u'Категория - %s' % u'Поиск: %s' % self.query
        context['breadcrumbs'] = [(u'Поиск: %s' % self.query, None)]
        return context


def main(request):
    context = {
        'title': u'Электронный каталог',
        'breadcrumbs': None,
    }
    return render_to_response('product_list.html', context, context_instance=RequestContext(request))


def product_details(request, **params):
    product = get_object_or_404(Product, id=params['id'])
    context = {
        'product': product,
        'title': product.name,
        'breadcrumbs': product.category.get_breadcrumbs() + [(product.name, None)],
    }
    return render_to_response('product_details.html', context, context_instance=RequestContext(request))


# def product_list(request, **params):
#     current_category = get_object_or_404(Categories, slug=params.get('slug'))
#     if request.path != current_category.get_absolute_url():
#         raise Http404
#     products = Product.available.filter(category=current_category)
#     if not request.user.is_authenticated():
#         products = products.exclude(is_hidden=True)
#     context = {
#         'title': u'Категория - %s' % current_category.name,
#         'current_category': current_category,
#         'breadcrumbs': current_category.get_breadcrumbs(),
#         'item_list': get_page(products, request.GET.get('page'), 12),
#     }
#     return render_to_response('product_list.html', context, context_instance=RequestContext(request))
#
#
# def search(request):
#     query = request.GET.get('q', None)
#     products = Product.available.filter(name__icontains=query) if query else Product.objects.none()
#     if not request.user.is_authenticated():
#         products = products.exclude(is_hidden=True)
#     context = {
#         'title': u'Категория - %s' % u'Поиск: %s' % query,
#         'breadcrumbs': [(u'Поиск: %s' % query, None)],
#         'item_list': get_page(products, request.GET.get('page'), 12),
#     }
#     return render_to_response('product_list.html', context,  context_instance=RequestContext(request))

def filldb(request):
    categories = Categories.objects.all()
    for category in categories:
        if Product.objects.all().filter(category=category).count() == 0:
            for i in range(100):
                description_sourse = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.whitespace
                token = ''.join(random.choice(description_sourse) for x in range(1000))
                product = Product(name='%s %s' % (category, i), category=category, image=None, count=1, price=1,
                                  description=token, is_hidden=bool(random.getrandbits(1))
                                  )
                product.save()
    return redirect('/')
