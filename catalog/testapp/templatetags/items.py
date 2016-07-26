from testapp.models import Categories, Product
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
register = template.Library()

@register.inclusion_tag('items.html', takes_context=True)
def items(context):
    request = context['request']
    category_list = Categories.objects.filter(fullUrl__istartswith=request.path)

    ids = [category.id for category in category_list]
    products = Product.objects.filter(category__in=ids)

    paginator = Paginator(products, 12)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return {'item_list': items}
