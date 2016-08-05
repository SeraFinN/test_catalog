from testapp.models import Categories
from testapp.formater import prepare_data


def categories(request):
    return {"categories_list": prepare_data(Categories.objects.all().values('id', 'parent_id', 'name'))}
