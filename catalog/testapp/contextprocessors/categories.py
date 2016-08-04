from testapp.formater import prepare_data
from testapp.models import Categories


def categories(request):
    return {"categories_list": prepare_data(Categories.objects.all().values('id', 'parent_id', 'name'))}
