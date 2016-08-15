from django.core.cache import cache

from catalog.formater import get_categories_list
from local_setting import CATEGORIES_CACHE_NAME


def categories(request):
    categories_list = cache.get(CATEGORIES_CACHE_NAME)
    if not categories_list:
        categories_list = get_categories_list()
        cache.set(CATEGORIES_CACHE_NAME, categories_list)
    return {"categories_list": categories_list}
