from django import template

register = template.Library()


@register.filter
def add_get_param(value, request):
    params = request.GET.copy()
    params['page'] = value
    return params.urlencode()
