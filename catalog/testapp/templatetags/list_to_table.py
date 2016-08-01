from math import ceil

from django import template

register = template.Library()


@register.filter
def list_to_table(value, col_count=4):
    row_count = int(ceil(len(value) / float(col_count)))
    return [value[x:x + col_count] for x in range(row_count)]
