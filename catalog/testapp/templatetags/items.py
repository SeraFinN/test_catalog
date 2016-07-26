from testapp.models import Categories, Product
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
register = template.Library()

@register.inclusion_tag('items.html', takes_context=True)
def items(context):
    request = context['request']
    path = filter(bool, request.path.split('/'))[-1].lower()
    category = Categories.objects.get(slug=path)
    ids = get_child_ids(category)

    products = Product.objects.filter(category__in=ids)

    paginator = Paginator(products, 12)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    # assert False, list(items)[0].image

    return {'item_list': items}

def get_child_ids(category):
    ids = []
    childs = Categories.objects.filter(parent=category.id)
    ids.append(category.id)
    for child in childs:
        # ids.append(child.id)
        ids += get_child_ids(child)
    return ids