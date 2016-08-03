from django.core.paginator import Paginator


def get_page(items, page):
    paginator = Paginator(items, 12)
    page = int(page) if page and page.isdigit() else 1
    if page > paginator.num_pages:
        page = paginator.num_pages
    if page < 0:
        page = 1
    return paginator.page(page)
