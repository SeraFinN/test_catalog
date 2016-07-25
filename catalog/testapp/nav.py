__author__ = 'serafinn'
from django import template
from testapp.models import Publisher, Categories
register = template.Library()


@register.inclusion_tag('nav.html')
def nav():
    return {'categoty_list': Categories.objects.all()}