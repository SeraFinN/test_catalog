from django.core.paginator import Paginator


def get_page(items, page, per_page):
    min_page = 1
    paginator = Paginator(items, per_page)
    page = int(page) if page and page.isdigit() else min_page
    if page > paginator.num_pages:
        page = paginator.num_pages
    if page < min_page:
        page = min_page
    return paginator.page(page)
