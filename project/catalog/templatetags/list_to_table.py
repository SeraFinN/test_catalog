from django import template

register = template.Library()


@register.filter
def list_to_table(value, col_count=4):
    return [value[index:index + col_count] for index in range(0, len(value), 4)]
