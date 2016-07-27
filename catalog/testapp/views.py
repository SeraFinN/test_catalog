from django.http import Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from testapp.models import Product, Categories


def main(request, **params):
    template = "child_category_list.html"
    has_child = True

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
        categories = Categories.objects.filter(id__in=current_category.get_direct_child_ids())
        has_child = bool(categories)
    else:
        categories = Categories.objects.filter(parent__isnull=True)

    items = []
    if not has_child:
        template = 'product_list.html'
        products = Product.objects.filter(category=current_category.id)

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

    return render_to_response(template, context)
