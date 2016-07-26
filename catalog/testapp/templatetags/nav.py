from django import template
from testapp.models import Categories
register = template.Library()


@register.inclusion_tag('nav.html', takes_context=True)
def nav(context):
    request = context['request']
    categories = Categories.objects.all()
    categories = sorted(
        categories,
        key=lambda category: (category.fullUrl,) +
                             tuple(sub[0] for sub in category.fullUrl.split('/') if sub and category.level > 1)
    )
    return {'categoty_list': categories, 'current_path': request.path}