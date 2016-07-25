from testapp.models import Categories, Product
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
register = template.Library()

@register.inclusion_tag('items.html', takes_context=True)
def items(context):
    row_count = 3
    col_count = 4
    request = context['request']
    category_list = Categories.objects.filter(fullUrl__istartswith=request.path)

    ids = [category.id for category in category_list]
    products = Product.objects.filter(category__in=ids)

    paginator = Paginator(products, col_count * row_count)
    # assert False, (products, ids)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    # i think is very, very bad. Ask
    items.object_list = [items[x:x + col_count] for x in range(0, len(items), col_count)]

    return {'item_list': items, 'address': request.path}