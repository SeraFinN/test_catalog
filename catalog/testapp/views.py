from collections import defaultdict

from django.http import Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from testapp.models import Product, Categories


def main(request, **params):
    category_tree = Categories.objects.all()
    category_tree = sorted(category_tree, key=lambda cat: (cat.get_absolute_url()))

    # assert False, Categories.objects.annotate(dcount=Count('parent')).values('id', 'slug')

    # assert False, Categories.objects.select_related('parent')
    # cat = Categories.objects.get(pk=3).category.all()

    # items = Categories.objects.all()
    # parent_map = defaultdict(list)
    # for item in items:
    #     parent_map[getattr(item, 'parent')].append(item)
    # l = []
    # for i in parent_map:
    #     child = parent_map[i]
    #     l.append(child)
    #
    # assert False, parent_map
    #
    # l = Categories.objects.filter(parent=None).values_list('id', flat=True)
    # t = [Categories.objects.filter(parent=x).values_list('id', flat=True) for x in l]
    # assert False, t



    # items = Categories.objects.all().values('id', 'parent_id')
    #
    # parent_map = defaultdict(list)
    # for item in items:
    #     #assert False, item['parent_id']
    #     parent_map[item['parent_id']].append(item)




    # assert False, parent_map

    #
    # assert False, list(tree_level(None))
    #
    # def tree_level(parent):
    #     for item in parent_map[parent]:

    # def tree_level(parent):
    #     for item in parent_map[parent]:
    #         yield item
    #         sub_items = list(tree_level(item['id']))
    #         if sub_items:
    #             sub_items
    # l = []
    # for i in tree_level(None):
    #     l.append(i)
    # assert False, l
    # items = Categories.objects.all()
    # parent_map = defaultdict(list)
    # for item in items:
    #     parent_map[getattr(item, 'parent')].append(item)

    # def tree_level(parent):
    #     for item in parent_map[parent]:
    #         # assert False, item
    #         yield item
    #
    #         sub_items = list(tree_level(item['id']))
    #         if sub_items:
    #             yield sub_items
    #
    # assert False, list(tree_level(None))


    # test_data = tree_level(None)


    # assert False, cat.category.all()
    current_category = None
    breadcrumbs = []
    is_main = True
    slug = params['slug']
    products = None
    items = None
    # assert False, slug
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        is_main = False
        breadcrumbs += [('Search: ' + q, None)]
        products = Product.objects.filter(name__icontains=q)
    elif slug:
        # assert False, request.GET['q']
        is_main = False
        try:
            current_category = Categories.objects.get(slug__iexact=slug)
            breadcrumbs = current_category.get_breadcrumbs()
        except Categories.DoesNotExist:
            raise Http404
        if not request.path == current_category.get_absolute_url():
            raise Http404
        products = Product.objects.filter(category=current_category)

    if products:
        paginator = Paginator(products, 12)
        page = request.GET.get('page')

        try:
            items = paginator.page(page)
            items.next_page_number()
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

    # assert False, list(items)
    context = dict()
    context['category_list'] = category_tree
    context['current_category'] = current_category
    context['item_list'] = items
    context['breadcrumbs'] = breadcrumbs
    context['is_main'] = is_main
    # context['test_data'] = list(test_data)

    return render_to_response('product_list.html', context)


def product_details(request, **params):
    category_tree = Categories.objects.all()
    category_tree = sorted(category_tree, key=lambda cat: (cat.get_absolute_url()))

    if not params:
        raise Http404
    try:
        product = Product.objects.get(id=params['id'])
        context = dict()
        context['is_main'] = False
        context['product'] = product
        context['category_list'] = category_tree
        context['breadcrumbs'] = product.category.get_breadcrumbs() + [(product.name, None)]
        # assert False, context['breadcrumbs']
        return render_to_response('product_details.html', context)
    except Product.DoesNotExist:
        raise Http404