from django import template
from django.utils.safestring import mark_safe

from testapp.models import Categories

register = template.Library()


@register.filter()
def to_tree(format_list, current_category):
    items = Categories.objects.all()

    def gt_simbols(categories, level):
        out = ''
        for item in categories:
            if isinstance(item, type([])):
                out += gt_simbols(item, level + 1)
            else:
                if current_category and item['id'] == current_category.id:
                    out = out + ">" * level + item['name'] + "<br />"
                else:
                    link = "<a href=" + items.get(id=item['id']).get_absolute_url() + ">" + item['name'] + "</a><br />"
                    out = out + ">" * level + link
        return out

    return mark_safe(gt_simbols(format_list, 0))
