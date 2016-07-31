from collections import defaultdict


def prepare_data(items):
    father_childs = defaultdict(list)
    for item in items:
        father_childs[item['parent_id']].append(item)

    def to_list(root):
        l = []
        for category in sorted(father_childs[root]):
            l.append(category)
            sub_list = to_list(category['id'])
            if sub_list:
                l.append(sub_list)
        return l

    return to_list(None)
