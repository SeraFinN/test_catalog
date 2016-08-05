# coding=utf-8
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

from testapp.views import product_details, main, filldb, ProductsListView, SearchListView, ProductDetail

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
urlpatterns = staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
urlpatterns += patterns((),
                        (r'^admin/', include(admin.site.urls)),
                        (r'^login/$',  login, {'template_name': 'login.html',
                                               'extra_context': {'breadcrumbs': (u"Регистрация", None),
                                                                 'title': u'Регистрация'}}),
                        (r'^logout/$', logout),
                        url(r'^product/(?P<pk>\d+)/?$', product_details, name='product_detail'),
                        (r'^$', main),
                        (r'^search/$', SearchListView.as_view()),
                        (r'^filldb/$', filldb),
                        (r'^(?:(?P<slug>[\w-]+)/)*$', ProductsListView.as_view()),
                        )
# from django.contrib import admin
# admin.autodiscover()


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
