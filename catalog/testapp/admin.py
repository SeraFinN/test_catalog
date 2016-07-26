from django.contrib import admin

from testapp.models import Categories, Images, Product


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Images)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Product)
