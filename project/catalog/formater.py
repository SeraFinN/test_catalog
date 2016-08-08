from collections import defaultdict

from django.core.exceptions import ObjectDoesNotExist

from catalog.models import Categories


def prepare_data(items):
    father_childs = defaultdict(list)
    for item in items:
        father_childs[item['parent_id']].append(item)

    def to_list(root, level):
        category_list = []
        for category in sorted(father_childs[root]):
            try:
                current_category = Categories.objects.get(id=category['id'])
            except ObjectDoesNotExist:
                continue
            category['url'] = current_category.get_absolute_url()
            category['level'] = level
            category_list.append(category)
            sub_list = to_list(category['id'], level + 1)
            if sub_list:
                category_list += sub_list
        return category_list

    return to_list(None, 0)