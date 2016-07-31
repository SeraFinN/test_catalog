from django.http import Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, Categories
from .formater import prepare_data

def main(request, **params):
    category_tree = Categories.objects.all()
    # category_tree = sorted(category_tree, key=lambda cat: (cat.get_absolute_url()))

    categories_dict = category_tree.values('id', 'parent_id', 'name')
    # parent_map = defaultdict(list)
    # for item in items:
    #     parent_map[item['parent_id']].append(item)
    #
    # def tree_to_list(root):
    #     l = []
    #     for item in sorted(parent_map[root]):
    #         l.append(item)
    #         sub_list = tree_to_list(item['id'])
    #         if sub_list:
    #             l.append(sub_list)
    #     return l
    #         # if sub_list:
    #             # assert False, sub_list
    #             # return l + [sub_list]
    #     # assert False, l



    # assert False, prepare_data(items)

    current_category = None
    breadcrumbs = []
    is_main = True
    slug = params['slug']
    products = None
    items = None
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        is_main = False
        breadcrumbs += [('Search: ' + q, None)]
        products = Product.objects.filter(name__icontains=q)
    elif slug:
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

    context = dict()
    context['category_list'] = category_tree
    context['current_category'] = current_category
    context['item_list'] = items
    context['breadcrumbs'] = breadcrumbs
    context['is_main'] = is_main
    context['request'] = request
    context['test_data'] = prepare_data(categories_dict)

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
        return render_to_response('product_details.html', context)
    except Product.DoesNotExist:
        raise Http404
