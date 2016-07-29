from django import template

register = template.Library()


@register.filter
def save_get_param(value, request):
    # assert request
    dict_ = request.GET.copy()
    dict_['page'] = value
    return dict_.urlencode()
    # return request.GET

# @register.tag
# def save_get_param(context, field, value):
#     request = context['request']
#     dict_ = request.GET.copy()
#     dict_[field] = value
#     return dict_.urlencode()
