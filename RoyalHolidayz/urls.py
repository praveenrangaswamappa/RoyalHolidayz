from django.conf.urls import patterns, include, url
from apps.reports.views import candidatereport

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RoyalHolidayz.views.home', name='home'),
    # url(r'^RoyalHolidayz/', include('RoyalHolidayz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', candidatereport),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': '/path/to/media'})
)
