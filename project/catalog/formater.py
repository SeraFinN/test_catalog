from collections import defaultdict

from catalog.models import Categories


def get_categories_list():
    father_childs = defaultdict(list)

    for item in Categories.objects.all():
        values = {'id': item.id, 'parent_id': item.parent_id, 'name': item.name, 'url': item.get_absolute_url()}
        father_childs[values['parent_id']].append(values)

    def to_list(root, level):
        category_list = []
        for category in sorted(father_childs[root]):
            category['level'] = level
            category_list.append(category)
            sub_list = to_list(category['id'], level + 1)
            if sub_list:
                category_list += sub_list
        return category_list

    return to_list(None, 0)

# 
def prepare_data():
    father_childs = defaultdict(list)
    items = Categories.objects.select_related().values('id', 'parent_id', 'name')
    cat = Categories.objects.select_related()
    for item in items:
        father_childs[item['parent_id']].append(item)

    # assert False, items
    def to_list(root, level):
        category_list = []
        for category in sorted(father_childs[root]):
            category['url'] = cat.get(id=category['id']).get_absolute_url()
            category['level'] = level
            category_list.append(category)
            sub_list = to_list(category['id'], level + 1)
            if sub_list:
                category_list += sub_list

        return category_list
    return to_list(None, 0)
