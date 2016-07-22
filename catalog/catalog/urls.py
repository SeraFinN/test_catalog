from django.conf.urls import patterns, include, url
from testapp.views import hello, hours_ahead

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns((),
                       ('^hello/$', hello),
                       (r'^time/plus/(\d{1,2})/$', hours_ahead),

    # Examples:
    # url(r'^$', 'catalog.views.home', name='home'),
    # url(r'^catalog/', include('catalog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)
