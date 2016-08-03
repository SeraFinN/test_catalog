from django import template
from testapp.models import Categories

register = template.Library()


@register.filter()
def level_to_gt(level):
    return '>' * level
