from django import template

register = template.Library()


@register.filter
def save_get_param(value, request):
    params = request.GET.copy()
    params['page'] = value
    return params.urlencode()
