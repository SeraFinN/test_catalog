from catalog.formater import get_categories_list


def categories(request):
    return {"categories_list": get_categories_list()}
