__author__ = 'serafinn'
from django import template
from testapp.models import Categories
register = template.Library()


@register.inclusion_tag('nav.html', takes_context=True)
def nav(context):
    request = context['request']
    # address = request.session['address']
    categories = Categories.objects.all()
    # l = [y for x in categories for y in x.url.split('/') if y]
    # assert False, l
    categories = sorted(categories, key=lambda x: (x.url,) + tuple(y[0] for y in x.url.split('/') if y and x.level > 1))
    return {'categoty_list': categories, 'address': request.path}