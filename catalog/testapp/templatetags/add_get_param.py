from django import template

register = template.Library()


@register.filter
def add_get_param(value, params):
    params['page'] = value
    return params.urlencode()
