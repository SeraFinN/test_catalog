from django.contrib import admin
from testapp.models import Categories, Images, Product

admin.site.register(Images)
admin.site.register(Categories)
admin.site.register(Product)