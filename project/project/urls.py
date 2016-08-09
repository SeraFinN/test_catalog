# coding=utf-8
from django.contrib import admin
from django.contrib.auth.views import logout, login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from catalog.views import product_details, main, product_list, search

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
urlpatterns = staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
urlpatterns += patterns((),
                        (r'^admin/', include(admin.site.urls)),
                        (r'^login/$', login, {'template_name': 'login.html',
                                              'extra_context': {'title': u'Авторизация',
                                                                'breadcrumbs': [{'name': u'Авторизация'}]
                                                                }}),
                        (r'^logout/$', logout),
                        url(r'^product/(?P<pk>\d+)/?$', product_details, name='product_detail'),
                        (r'^$', main),
                        (r'^search/$', search),
                        (r'^(?:(?P<slug>[\w-]+)/)*$', product_list),
                        )
# from django.contrib import admin
# admin.autodiscover()


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
