from django.http import Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, Categories
from .formater import prepare_data


def product_list(request, **params):
    categories_dict = Categories.objects.all().values('id', 'parent_id', 'name')
    breadcrumbs = []
    is_main = True
    slug = params['slug']
    products = None
    items = None
    current_id = None
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        is_main = False
        breadcrumbs += [('Search: ' + q, None)]
        products = Product.objects.filter(name__icontains=q)
    elif slug:
        is_main = False
        try:
            current_category = Categories.objects.get(slug__iexact=slug)
            current_id = current_category.id
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
            items = paginator.page(page)
            items.next_page_number()
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

    context = dict()
    context['current_id'] = current_id
    context['item_list'] = items
    context['breadcrumbs'] = breadcrumbs
    context['is_main'] = is_main
    context['request'] = request
    context['categories_list'] = prepare_data(categories_dict)
    return render_to_response('product_list.html', context)


def product_details(request, **params):
    if not params:
        raise Http404
    try:
        product = Product.objects.get(id=params['id'])
    except Product.DoesNotExist:
        raise Http404
    context = dict()
    context['current_id'] = None
    context['is_main'] = False
    context['product'] = product
    context['categories_list'] = prepare_data(Categories.objects.all().values('id', 'parent_id', 'name'))
    context['breadcrumbs'] = product.category.get_breadcrumbs() + [(product.name, None)]
    return render_to_response('product_details.html', context)
