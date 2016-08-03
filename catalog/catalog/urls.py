from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from testapp.views import product_list, product_details, search, main

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns((), )
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns((),
                        (r'^admin/', include(admin.site.urls)),
                        url(r'^product/(?P<id>\d+)/?$', product_details, name='product_details'),
                        (r'^$', main),
                        (r'^search/$', search),
                        (r'^(?:(?P<slug>[\w-]+)/)*$', product_list),
                        )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
# from django.contrib import admin
# admin.autodiscover()


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
