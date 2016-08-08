from collections import defaultdict


def prepare_data(items):
    father_childs = defaultdict(list)
    for item in items:
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
