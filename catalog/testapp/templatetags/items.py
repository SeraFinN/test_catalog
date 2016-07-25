from testapp.models import Categories, Product
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
register = template.Library()

@register.inclusion_tag('items.html', takes_context=True)
def items(context):
    request = context['request']
    category_list = Categories.objects.filter(url__istartswith=request.path)
    ids = []
    for category in category_list:
        ids.append(category.id)
    products = Product.objects.filter(category__in=ids)
    paginator = Paginator(products, 2)
    # assert False, (products, ids)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    return {'item_list': items, 'address': request.path}