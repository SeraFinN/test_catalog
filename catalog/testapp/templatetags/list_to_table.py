from django import template

register = template.Library()


@register.filter
def list_to_table(value, col_count=4):
    return [value[x:x + col_count] for x in range(0, len(value), col_count)]
