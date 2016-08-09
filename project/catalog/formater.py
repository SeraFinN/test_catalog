from collections import defaultdict

from catalog.models import Categories


def get_categories_list():
    father_childs = defaultdict(list)

    for item in Categories.objects.all():
        father_childs[item.parent_id].append(item)

    def to_list(root):
        category_list = []
        for category in sorted(father_childs[root], key=lambda obj: obj.name):
            category_list.append(category)
            sub_list = to_list(category.pk)
            if sub_list:
                category_list += sub_list
        return category_list

    return to_list(None)
