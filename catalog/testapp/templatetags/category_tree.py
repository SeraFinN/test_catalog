from django import template
from django.utils.safestring import mark_safe
from testapp.models import Categories


register = template.Library()


@register.filter()
def category_tree(format_list):
    items = Categories.objects.all()

    def to_tree(list, level):
        out = ''
        for item in list:
            if isinstance(item, type([])):

                out = out + "<ul>" + to_tree(item, level + 1) + "</ul>"
            else:
                list_item = "<li><a href=" + items.get(id=item['id']).get_absolute_url() + ">" + item['name'] + "</a></li>"
                out = out + list_item#">" * level + "<a href=" + items.get(id=item['id']).get_absolute_url() + ">" + item['name'] + "</a><br />"
        return out
    #assert False, to_tree(format_list, 0)
    return mark_safe("<ul>" + to_tree(format_list, 0) + "</ul>")
