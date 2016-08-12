from catalog.formater import get_categories_list
from django.core.cache import cache

from catalog.models import Categories


def categories(request):
    categories_list = cache.get(Categories.__name__)
    print 'cache %s' % categories_list
    print 'cache_bool %s' % bool(categories_list)
    if not categories_list:
        print 'calc'
        # assert False, 'test'
        categories_list = get_categories_list()
        cache.set(Categories.__name__, categories_list)
    # print 'cache %s' % cache.get(Categories.__name__)
    return {"categories_list": categories_list}
