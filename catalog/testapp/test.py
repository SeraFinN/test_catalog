from collections import defaultdict


def test_data(items):
    father_childs = defaultdict(list)
    for item in items:
        father_childs[item['parent_id']].append(item)

    def to_list(root):
        for category in sorted(father_childs[root]):
            yield category
            sub_list = to_list(category['id'])
            if sub_list:
                yield(sub_list)
        # return l

    return to_list(None)
