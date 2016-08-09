from django import template

register = template.Library()


@register.filter()
def level_to_gt(level):
    return '>' * (level - 1)
