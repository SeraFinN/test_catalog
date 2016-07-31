from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import *
from django.conf import settings
from django.conf.urls import patterns, include
from django.conf.urls.static import static

from testapp.views import product_list, product_details

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns((), )
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns((),

                        # ('^hello/$', hello),
                        # ('^bd/$', bd_test),
                        # (r'^time/plus/(\d{1,2})/$', hours_ahead),
                        (r'^admin/', include(admin.site.urls)),

                        # (r'^monitors/([(\w*)/]*)(\?page=\d+)?$', product_list),
                        # (r'^cpu/([(\w*)/]*)(\?page=\d+)?$', product_list),

                        # (r'^$', index),

                        # (r'^((?P<slug>[\w-]+)/?)*$', main),
                        url(r'^product/(?P<id>\d+)/?$', product_details, name='product_details'),


                        (r'^search/\?q=\d+$', product_list),
                        # (r'^search/?q=(?P<q>\w+)*(\?page=(?P<page>\d+))?$', main),


                        # (r'^product/(?P<id>\d+)/?$', product_details),
                        (r'^((?P<slug>[\w-]+)/?)*(\?page=(?P<page>\d+))?$', product_list),

                        # (r'^([\w-]*)/?([\w-]*)/?([\w-]*)/?(\?page=\d+)?$', product_list),
                        # (r'^monitors/((\d{1,2})/)*$', monitors),
                        # (r'^cpu/(\d{1,2})/$', monitors)
                        # (r'^cpu/((\w*)/)*$', product_list),
                        # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),




                        # Examples:
                        # url(r'^$', 'catalog.views.home', name='home'),
                        # url(r'^catalog/', include('catalog.foo.urls')),

                        # Uncomment the admin/doc line below to enable admin documentation:
                        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                        # Uncomment the next line to enable the admin:
                        # url(r'^admin/', include(admin.site.urls)),
                        )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
# from django.contrib import admin
# admin.autodiscover()


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
