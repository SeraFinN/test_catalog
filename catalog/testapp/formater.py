from collections import defaultdict

from testapp.models import Categories


def prepare_data(items):
    father_childs = defaultdict(list)
    for item in items:
        father_childs[item['parent_id']].append(item)

    # def to_list(root):
    #     l = []
    #     for category in sorted(father_childs[root]):
    #         l.append(category)
    #         sub_list = to_list(category['id'])
    #         if sub_list:
    #             l.append(sub_list)
    #     return l
    #
    # return to_list(None)

    categories = Categories.objects.all()
    def to_list(root, level):
        l = []
        for category in sorted(father_childs[root]):
            category['url'] = categories.get(id=category['id']).get_absolute_url()
            category['level'] = level
            l.append(category)
            sub_list = to_list(category['id'], level + 1)
            if sub_list:
                l += sub_list
        return l
    # assert False, to_list(None, 0)
    return to_list(None, 0)
