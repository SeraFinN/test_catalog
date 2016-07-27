from django.http import Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from testapp.models import Product, Categories


def main(request, **params):
    category_tree = Categories.objects.all()
    category_tree = sorted(category_tree, key=lambda cat: (cat.get_absolute_url()))

    current_category = None
    slug = params['slug']
    if slug:
        try:
            current_category = Categories.objects.get(slug__iexact=slug)
        except Categories.DoesNotExist:
            raise Http404
        if not request.path == current_category.get_absolute_url():
            raise Http404
        categories = Categories.objects.filter(id__in=current_category.get_all_level_child_ids() + [current_category.id])
    else:
        categories = Categories.objects.all()

    products = Product.objects.filter(category__in=categories)

    paginator = Paginator(products, 12)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    context = dict()
    context['category_list'] = category_tree
    context['current_category'] = current_category
    context['item_list'] = items
    context['categories'] = categories

    return render_to_response('product_list.html', context)


def product_details(request, **params):
    category_tree = Categories.objects.all()
    category_tree = sorted(category_tree, key=lambda cat: (cat.get_absolute_url()))

    if not params:
        raise Http404
    try:
        product = Product.objects.get(id=params['id'])
        return render_to_response('product_details.html', {'product': product, 'category_list': category_tree})
    except Product.DoesNotExist:
        raise Http404
